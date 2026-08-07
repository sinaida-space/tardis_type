#!/usr/bin/env python3
"""
typocheck — typography linter for Sinaida's RU/EN prose.

Usage:
    python3 typocheck.py FILE [FILE ...] [--lang ru|en|auto] [--fix] [--html]
    cat text.md | python3 typocheck.py - [--lang ru]

Checks (report-only unless --fix):
    hard   em-dash rhetoric, "not A but B" constructions, straight quotes,
           double spaces, "..." , Cyrillic/Latin homoglyph mixing
    soft   missing non-breaking spaces, one-word paragraph endings (widows),
           lines ending on a preposition/particle, wrong range dashes
    prose  (§7 of SKILL.md) AI vocabulary, copula avoidance, inflated
           significance, "-ing" tails, vague attribution, hedging, filler,
           signposting, authority tropes, sycophancy, generic endings,
           speculative gap-filling, emoji, Title Case, boldface spray,
           rule-of-three density. Never auto-fixed; use --no-slop to silence,
           --slop-only to run nothing else.

--fix applies only the mechanical, unambiguous transforms:
    nbsp insertion, curly quotes, ellipsis, ×, minus, double-space collapse.
Dash rewrites and widow fixes are never automated: they need a rewritten
sentence, not a substitution.

Fenced code blocks, inline code, URLs, HTML tags and file paths are masked out
before any check runs. A document that quotes bad examples on purpose can wrap
them in `<!-- typocheck: off -->` … `<!-- typocheck: on -->`.
"""

import argparse
import re
import sys
import unicodedata

NBSP = " "
NNBSP = " "
THINSP = " "
SHY = "­"
EMDASH = "—"
ENDASH = "–"
MINUS = "−"
NBHYPHEN = "‑"
ELLIPSIS = "…"

# ---------------------------------------------------------------- word lists

RU_GLUE_AFTER = """
в на с к по за из от до для при над под про без о об у и а но да что как или не ни
же ли бы то во со ко из-за из-под их её его им ей мы вы он она они я ты
""".split()
RU_SHORT_AFTER = {w for w in RU_GLUE_AFTER if len(w) <= 3}

RU_PARTICLES_BEFORE = "же бы б ли ль уж ж".split()

RU_ABBR_BEFORE_NUM = "№ § с. стр. рис. табл. гл. п. пп. т. г. ул. д. кв. корп.".split()

RU_UNITS = """
кг г мг т км м см мм мкм л мл ч мин сек с ч. руб. коп. ₽ $ € %
млн млрд тыс шт чел px пкс fps кадр/с Гц кГц МГц ГГц Кб Мб Гб Тб бит байт
""".split()

EN_GLUE_AFTER = """
a an the I to of in on at by is as it we or if so be do no up my he
and for but nor yet per via from with into onto over than that this
""".split()
EN_SHORT_AFTER = {w for w in EN_GLUE_AFTER if len(w) <= 3}

EN_UNITS = """
kg g mg t km m cm mm l ml h min s ms fps px pt em rem dpi ppi Hz kHz MHz GHz
KB MB GB TB bit byte bits bytes % °C °F cd lm lux nm
""".split()

EN_TITLES = "Mr. Mrs. Ms. Dr. Prof. St. Mt. No. Fig. Eq. Ch. Vol. p. pp.".split()

# ---------------------------------------------------------------- slop rules

SLOP_PATTERNS = [
    (
        "not-a-but-b",
        re.compile(
            r"\b(?:"
            r"not\s+just\s+\w[\w\s]{0,30}?,\s*(?:it(?:'|’)s|but|it\s+is)"
            r"|isn(?:'|’)t\s+(?:about\s+)?\w[\w\s]{0,30}?[,.]\s*it(?:'|’)s"
            r"|less\s+about\s+\w[\w\s]{0,25}?,\s*more\s+(?:about|of)"
            r"|\w+,\s+not\s+(?:decoration|noise|a\s+\w+|just\s+\w+)"
            r")",
            re.I,
        ),
        'contrastive "not A, but B" framing is banned; state what it is, directly',
    ),
    (
        "ne-a-a-b",
        re.compile(
            r"(?:\bне\s+просто\s+[^,.;]{1,40},\s*а\b"
            r"|\bэто\s+не\s+[^,.;]{1,40},\s*(?:это|а)\b"
            r"|\bдело\s+не\s+в\s+[^,.;]{1,40},\s*(?:дело|а)\b)",
            re.I,
        ),
        'конструкция «не А, а Б» запрещена; скажи прямо, что это есть',
    ),
    (
        "ai-cliche",
        re.compile(
            r"\b(?:thrilled\s+to\s+announce|excited\s+to\s+share|passionate\s+about"
            r"|grateful\s+for\s+the\s+opportunity|delve\s+into|unlock\s+the\s+power"
            r"|game[-\s]chang(?:er|ing)|seamless(?:ly)?|in\s+today(?:'|’)s\s+"
            r"fast[-\s]paced\s+world|elevate\s+your)\b",
            re.I,
        ),
        "banned corporate/AI filler phrase",
    ),
]

# ------------------------------------------------------- prose quality (§7)
#
# Everything below is report-only, always. These need a rewritten sentence,
# never a substitution, so --fix does not touch them.

def _alt(words):
    return "|".join(re.escape(w) for w in words)


# §7.1 — vocabulary that is wrong on sight, both languages
HARD_VOCAB = [
    "delve", "tapestry", "testament to", "ever-evolving", "ever evolving",
    "groundbreaking", "cutting-edge", "must-visit", "breathtaking",
    "nestled", "in the heart of", "boasts a", "boasts an", "boasts over",
    "unlock the", "elevate your", "embark on", "navigate the landscape",
    "rich cultural heritage", "rich history", "vibrant tapestry",
    "underscores the importance", "underscores its", "highlights the importance",
    "leaving an indelible mark", "deeply rooted in", "resonates with",
    "in today's fast-paced", "in today’s fast-paced",
    "погрузиться в", "раскрыть потенциал", "вывести на новый уровень",
    "богатое наследие", "богатая история", "глубоко укоренён",
    "глубоко укоренен", "неизгладимый след", "в современном мире",
    "в эпоху цифровых технологий", "играет ключевую роль", "ключевую роль",
    "играет важную роль", "неотъемлемой частью", "подчёркивает значимость",
    "подчеркивает значимость", "отражает более широкий", "знаковый момент",
    "поворотной точкой", "комплексный подход", "бесшовн",
]

# §7.1 — words that are fine once and damning in a cluster
SOFT_VOCAB_EN = """
crucial pivotal vital robust seamless leverage foster fostering cultivate
cultivating realm myriad intricate intricacies interplay garner landscape
showcase showcases showcasing underscore underscores enhance enhances
enhancing meticulous comprehensive holistic transformative immersive vibrant
profound renowned stunning innovative revolutionary
""".split()

SOFT_VOCAB_RU = """
уникальный уникальная уникальное поистине инновационный инновационная
передовой передовая захватывающий захватывающая впечатляющий впечатляющая
потрясающий потрясающая значимый значимость целостный масштабный
всеобъемлющий революционный
""".split()

PROSE_PATTERNS = [
    ("copula-avoidance",
     re.compile(r"\b(?:serves?\s+as|stands?\s+as|represents?\s+a|constitutes?\s+a"
                r"|boasts?|is\s+home\s+to)\b"
                r"|\b(?:является|служит|выступает\s+в\s+качестве"
                r"|представляет\s+собой)\b", re.I | re.U),
     "copula avoidance: write “is” (§7.2)"),

    ("inflated-significance",
     re.compile(r"\b(?:a\s+(?:pivotal|crucial|key|defining)\s+(?:moment|role|part)"
                r"|marks?\s+a\s+(?:shift|turning\s+point)"
                r"|setting\s+the\s+stage\s+for"
                r"|reflect(?:s|ing)\s+(?:a\s+)?broader"
                r"|contributing\s+to\s+the"
                r"|part\s+of\s+a\s+(?:wider|broader)\s+movement)\b"
                r"|\b(?:поворотн\w+\s+точк\w+|вписывается\s+в\s+более\s+широкий"
                r"|оставил\w?\s+неизгладимый)\b", re.I | re.U),
     "inflated significance: delete the sentence explaining why it mattered (§7.3)"),

    ("ing-tail",
     re.compile(r",\s+(?:highlighting|underscoring|emphasi[sz]ing|ensuring|reflecting"
                r"|symboli[sz]ing|contributing|cultivating|fostering|encompassing"
                r"|showcasing|demonstrating|illustrating|allowing|enabling|creating)\b",
                re.I),
     "superficial “-ing” tail: cut it or give it a subject (§7.4)"),

    ("false-range",
     re.compile(r"\bfrom\s+(?:the\s+)?\w[\w\s]{2,25}\s+to\s+(?:the\s+)?\w[\w\s]{2,25}"
                r",\s*from\b"
                r"|\bот\s+\w[\w\s]{2,25}\s+до\s+\w[\w\s]{2,25},\s*от\b", re.I | re.U),
     "false range: “from X to Y” where X and Y share no scale (§7.8)"),

    ("vague-attribution",
     re.compile(r"\b(?:experts?\s+(?:say|argue|believe|note)|observers?\s+have"
                r"|industry\s+reports?|some\s+critics|several\s+(?:sources|publications)"
                r"|it\s+is\s+(?:widely\s+)?believed|studies\s+suggest)\b"
                r"|\b(?:эксперты\s+(?:считают|полагают|отмечают)|наблюдатели\s+отмечают"
                r"|принято\s+считать|многие\s+специалисты)\b", re.I | re.U),
     "vague attribution: name the source or cut the claim (§7.9)"),

    ("hedge-stack",
     re.compile(r"\b(?:could\s+potentially|might\s+possibly|may\s+potentially"
                r"|it\s+could\s+be\s+argued\s+that|somewhat\s+of\s+a"
                r"|arguably\s+one\s+of\s+the)\b"
                r"|\b(?:возможно,\s+вероятно|скорее\s+всего,\s+можно\s+сказать)\b",
                re.I | re.U),
     "stacked hedging: one hedge maximum, and only if the doubt is real (§7.10)"),

    ("filler",
     re.compile(r"\b(?:in\s+order\s+to|due\s+to\s+the\s+fact\s+that"
                r"|at\s+th(?:is|at)\s+point\s+in\s+time|in\s+the\s+event\s+that"
                r"|has\s+the\s+ability\s+to|it\s+is\s+important\s+to\s+note\s+that"
                r"|it\s+(?:is|should\s+be)\s+worth\s+noting\s+that)\b"
                r"|\b(?:в\s+связи\s+с\s+тем,\s+что|на\s+данный\s+момент\s+времени"
                r"|обладает\s+возможностью|важно\s+отметить,\s+что"
                r"|стоит\s+отметить,\s+что|нельзя\s+не\s+отметить)\b", re.I | re.U),
     "filler phrase: see the table in §7.10"),

    ("signposting",
     re.compile(r"\b(?:let(?:'|’)s\s+(?:dive|explore|break\s+this\s+down|look\s+at|begin)"
                r"|here(?:'|’)s\s+what\s+you\s+need\s+to\s+know"
                r"|without\s+further\s+ado|now\s+let(?:'|’)s)\b"
                r"|\b(?:давайте\s+разберёмся|давайте\s+разберемся|итак,\s+начнём"
                r"|итак,\s+начнем|рассмотрим\s+подробнее)\b", re.I | re.U),
     "signposting: doing the thing replaces announcing it (§7.11)"),

    ("authority-trope",
     re.compile(r"\b(?:the\s+real\s+question\s+is|at\s+its\s+core|in\s+reality"
                r"|what\s+really\s+matters|the\s+deeper\s+issue"
                r"|the\s+heart\s+of\s+the\s+matter)\b"
                r"|\b(?:на\s+самом\s+деле,|по\s+сути,|главный\s+вопрос\s+в\s+том"
                r"|если\s+копнуть\s+глубже)", re.I | re.U),
     "persuasive authority trope: just say the point (§7.12)"),

    ("fake-candid",
     re.compile(r"(?:^|(?<=[.!?]\s))(?:Honestly\?|Look,|Here(?:'|’)s\s+the\s+thing"
                r"|The\s+thing\s+is,|Let(?:'|’)s\s+be\s+honest|Real\s+talk"
                r"|Честно\s+говоря,|Скажем\s+прямо,|Давайте\s+начистоту)", re.U),
     "fake-candid opener: a person being honest just says the thing (§7.14)"),

    ("sycophancy",
     re.compile(r"\b(?:great\s+question|you(?:'|’)re\s+absolutely\s+right"
                r"|i\s+hope\s+this\s+helps|let\s+me\s+know\s+if"
                r"|would\s+you\s+like\s+me\s+to|excellent\s+point)\b"
                r"|\b(?:отличный\s+вопрос|надеюсь,\s+это\s+поможет"
                r"|дайте\s+знать,\s+если)\b", re.I | re.U),
     "chatbot artifact: belongs to conversation, not to a delivered text (§7.16)"),

    ("generic-ending",
     re.compile(r"\b(?:the\s+future\s+looks\s+bright|exciting\s+times\s+(?:lie\s+)?ahead"
                r"|a\s+(?:major\s+)?step\s+in\s+the\s+right\s+direction"
                r"|journey\s+toward\s+excellence|the\s+possibilities\s+are\s+endless)\b"
                r"|\b(?:впереди\s+много\s+интересного|это\s+только\s+начало\."
                r"|остаётся\s+только\s+пожелать)\b", re.I | re.U),
     "generic upbeat ending: end on the last concrete fact (§7.17)"),

    ("speculative-gap",
     re.compile(r"\b(?:while\s+specific\s+details|based\s+on\s+available\s+information"
                r"|maintains?\s+a\s+low\s+profile|keeps?\s+personal\s+details\s+private"
                r"|is\s+not\s+publicly\s+available|likely\s+(?:grew\s+up|studied|began))\b"
                r"|\b(?:информаци\w+\s+не\s+представлена\s+в\s+открытых"
                r"|предположительно,\s+она)\b", re.I | re.U),
     "speculative gap-filling: say what is unknown, never guess it (§7.18)"),

    ("tailing-negation",
     re.compile(r"[,;]\s+no\s+(?:guessing|wasted\s+\w+|fuss|compromises?|surprises)\b"
                r"|[,;]\s+(?:никаких\s+компромиссов|без\s+лишних\s+\w+)\b", re.I | re.U),
     "tailing negation fragment: write the real clause (§7.6)"),

    ("hard-vocab",
     re.compile(r"(?:\b|(?<=\W))(?:" + _alt(HARD_VOCAB) + r")", re.I | re.U),
     "AI vocabulary, cut on sight (§7.1)"),

    ("emoji",
     re.compile("[\U0001F300-\U0001FAFF☀-➿️⬀-⯿]"),
     "emoji in a deliverable: zero, always (§1.4, §7.19)"),

]

# An inline-header list item is only a tell when the body restates the label.
# "- **File.** Read it, run the loop" is a normal glossary line and stays.
BOLD_LIST_ITEM = re.compile(r"^\s*[-*+]\s+\*\*([^*\n]{2,60}?):?\*\*:?\s*(.+)$")


def is_restating_list_item(line):
    m = BOLD_LIST_ITEM.match(line)
    if not m:
        return None
    label, body = m.groups()
    label_words = {w.lower() for w in re.findall(r"[\w’'-]{4,}", label)}
    body_words = {w.lower() for w in re.findall(r"[\w’'-]{4,}", body)}
    return m.group(0)[:60] if label_words & body_words else None

TRIAD = re.compile(
    r"\b\w[\w’'-]*,\s+\w[\w’'-]*,?\s+(?:and|или|и)\s+\w[\w’'-]*\b", re.U)

TITLE_CASE_HEADING = re.compile(r"^#{1,6}\s+(.*)$")


def check_prose(text, lang):
    """§7 checks. Report-only, line-level plus two document-level counts."""
    issues = []
    lines = text.split("\n")

    for i, line in enumerate(lines, 1):
        clean = re.sub(r"\x00+", "￼", line)
        if not clean.strip():
            continue
        for code, pat, msg in PROSE_PATTERNS:
            m = pat.search(clean)
            if m:
                issues.append((i, code, msg, m.group(0).strip()))

        # Title Case Headings, English only
        if lang == "en":
            hm = TITLE_CASE_HEADING.match(clean)
            if hm:
                words = [w for w in re.findall(r"[A-Za-z][\w’'-]*", hm.group(1))]
                caps = [w for w in words if w[0].isupper()]
                if len(words) >= 4 and len(caps) >= len(words) - 1:
                    issues.append((i, "title-case",
                                   "Title Case heading: use sentence case (§5, §7.19)",
                                   hm.group(1)[:60]))

        restated = is_restating_list_item(clean)
        if restated:
            issues.append((i, "bold-header-list",
                           "inline-header list item restating its own label: "
                           "write prose or drop the label (§7.19)", restated))

        # boldface spray: three or more bold runs in one line of body prose
        if len(re.findall(r"\*\*[^*\n]+\*\*", clean)) >= 3 and not clean.lstrip().startswith("|"):
            issues.append((i, "bold-spray",
                           "boldface spray: bold everything and nothing is emphasised "
                           "(§7.19)", clean[:60]))

    # document-level: soft vocabulary cluster
    soft = SOFT_VOCAB_RU if lang == "ru" else SOFT_VOCAB_EN
    body = re.sub(r"\x00+", " ", text).lower()
    hits = sorted({w for w in soft if re.search(r"\b" + re.escape(w), body)})
    if len(hits) >= 3:
        issues.append((1, "vocab-cluster",
                       f"{len(hits)} soft AI-vocabulary words in one text: "
                       "one is a slip, a cluster is a machine (§7.1)",
                       ", ".join(hits[:8])))

    # document-level: rule of three
    triads = TRIAD.findall(re.sub(r"\x00+", " ", text))
    if len(triads) >= 4:
        issues.append((1, "rule-of-three",
                       f"{len(triads)} parallel triads: break the rhythm, "
                       "two items or four (§7.5)", triads[0][:60]))

    return issues


# ------------------------------------------------------------------- masking


def mask_protected(text):
    """Replace regions typography must not touch with same-length placeholders."""
    spans = []
    patterns = [
        # explicit opt-out region, for docs that quote bad examples on purpose
        re.compile(r"<!--\s*typocheck:\s*off\s*-->.*?"
                   r"(?:<!--\s*typocheck:\s*on\s*-->|\Z)", re.S | re.I),
        re.compile(r"^```.*?^```", re.S | re.M),      # fenced code
        re.compile(r"^~~~.*?^~~~", re.S | re.M),
        re.compile(r"`[^`\n]+`"),                     # inline code
        re.compile(r"^(?: {4}|\t).*$", re.M),         # indented code
        re.compile(r"<[^>\n]{1,200}>"),               # html tags
        re.compile(r"&[a-zA-Z]{2,10};|&#x?[0-9a-fA-F]{2,6};"),
        re.compile(r"\b(?:https?|ftp|mailto|file)://\S+"),
        re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b"),   # emails
        re.compile(r"(?<![\w])[~./]?[\w.-]*/[\w./-]+"),  # paths
        re.compile(r"\$\{[^}\n]*\}|\{\{[^}\n]*\}\}"),  # templating
    ]
    for pat in patterns:
        for m in pat.finditer(text):
            spans.append((m.start(), m.end()))
    if not spans:
        return text, []
    spans.sort()
    merged = [list(spans[0])]
    for a, b in spans[1:]:
        if a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    chars = list(text)
    for a, b in merged:
        for i in range(a, b):
            if chars[i] != "\n":
                chars[i] = "\x00"
    return "".join(chars), merged


def split_protected(text):
    """Split into [(is_protected, chunk), ...] so fixes only touch free text."""
    _, spans = mask_protected(text)
    out, pos = [], 0
    for a, b in spans:
        if a > pos:
            out.append((False, text[pos:a]))
        out.append((True, text[a:b]))
        pos = b
    if pos < len(text):
        out.append((False, text[pos:]))
    return out


def apply_to_free_text(text, fn):
    """Run fn over every unprotected chunk, leaving code/URLs/paths untouched."""
    return "".join(chunk if prot else fn(chunk)
                   for prot, chunk in split_protected(text))


# ------------------------------------------------------------ language guess


def detect_lang(text):
    cyr = len(re.findall(r"[а-яёА-ЯЁ]", text))
    lat = len(re.findall(r"[a-zA-Z]", text))
    return "ru" if cyr > lat else "en"


# ------------------------------------------------------------------- fixers


def fix_spaces(t):
    t = re.sub(r"[ \t]+\n", "\n", t)                      # trailing ws
    t = re.sub(r"(?<=\S)[ ]{2,}(?=\S)", " ", t)           # double spaces
    t = re.sub(r"[ ]+([,.;:!?%)\]»…])", r"\1", t)         # space before punct
    t = re.sub(r"([«(\[])[ ]+", r"\1", t)                 # space after opener
    return t


def fix_glyphs(t, lang):
    t = t.replace("...", ELLIPSIS)
    t = re.sub(r"\.{3,}", ELLIPSIS, t)
    t = t.replace("(c)", "©").replace("(C)", "©")
    t = re.sub(r"\((?:tm|TM)\)", "™", t)
    t = re.sub(r"\((?:r|R)\)", "®", t)
    t = t.replace("->", "→").replace("<-", "←")
    t = t.replace("!?", "?!")
    # dimensions: 1920x1080 -> 1920×1080
    t = re.sub(r"(?<=\d)\s?[xх]\s?(?=\d)", "×", t)
    # minus before a number after a space or start
    t = re.sub(r"(?<=[\s(])-(?=\d)", MINUS, t)
    # numeric ranges take an en dash, unspaced
    t = re.sub(r"(?<=\d)\s*[-—]\s*(?=\d)", ENDASH, t)
    return t


def fix_quotes(t, lang):
    if lang == "ru":
        # outer «ёлочки»
        def ru(m):
            return "«" + m.group(1) + "»"

        t = re.sub(r'"([^"\n]{1,200})"', ru, t)
    else:
        def en(m):
            return "“" + m.group(1) + "”"

        t = re.sub(r'"([^"\n]{1,200})"', en, t)
        t = re.sub(r"(?<=\w)'(?=\w)", "’", t)        # don't -> don’t
        t = re.sub(r"'([^'\n]{1,80})'", "‘\\1’", t)
    return t


def fix_nbsp(t, lang):
    glue_after = RU_SHORT_AFTER if lang == "ru" else EN_SHORT_AFTER
    units = RU_UNITS if lang == "ru" else EN_UNITS

    # 1. short words / prepositions glue forward
    words = sorted(glue_after, key=len, reverse=True)
    pat = re.compile(
        r"(?<![\w ])(" + "|".join(re.escape(w) for w in words) + r")[ ](?=[\w«\"(“])",
        re.I if lang == "en" else re.U,
    )
    prev = None
    while prev != t:                       # repeat: "и в лесу"
        prev = t
        t = pat.sub(lambda m: m.group(1) + NBSP, t)

    # 2. number + unit
    upat = re.compile(
        r"(?<=\d)[ ](" + "|".join(re.escape(u) for u in units) + r")(?![\w])"
    )
    t = upat.sub(NBSP + r"\1", t)

    # 3. number + any following word of <= 4 chars (кг, руб., years)
    t = re.sub(r"(?<=\d)[ ](?=(?:г\.|гг\.|в\.|вв\.|мая|июня|июля))", NBSP, t)

    if lang == "ru":
        # 4. particles glue backward
        t = re.sub(
            r"[ ](?=(?:" + "|".join(RU_PARTICLES_BEFORE) + r")(?![\w]))", NBSP, t
        )
        # 5. № § abbreviations before a number
        t = re.sub(r"(№|§)[ ](?=\d)", r"\1" + NBSP, t)
        t = re.sub(r"\b(с|стр|рис|табл|гл|п|г|ул|д|кв)\.[ ](?=[\dА-ЯЁ])",
                   r"\1." + NBSP, t)
        # 6. initials
        t = re.sub(r"\b([А-ЯЁ])\.[ ]?([А-ЯЁ])\.[ ]?(?=[А-ЯЁ][а-яё])",
                   r"\1." + NBSP + r"\2." + NBSP, t)
        # 7. и т. д. / т. е.
        t = re.sub(r"\bт\.[ ]?([депк])\.", "т." + NBSP + r"\1.", t)
        # 8. dash that survived: nbsp before it
        t = re.sub(r"[ ]" + EMDASH, NBSP + EMDASH, t)
    else:
        titles = "|".join(re.escape(x) for x in EN_TITLES)
        t = re.sub(r"\b(" + titles + r")[ ](?=[\dA-Z])", r"\1" + NBSP, t)
        t = re.sub(r"\b([A-Z])\.[ ](?=[A-Z]\.)", r"\1." + NBSP, t)

    return t


def fix_headings_and_widows(t):
    """Glue the last two words of every Markdown heading and list item."""
    def glue(line):
        stripped = line.rstrip()
        m = re.match(r"^(\s*(?:#{1,6}|[-*+]|\d+\.)\s+)(.*)$", stripped)
        if not m:
            return line
        head, body = m.groups()
        if body.count(" ") < 2:
            return line
        body = re.sub(r"[ ](?=\S+\s*$)", NBSP, body, count=1)
        return head + body + line[len(stripped):]

    return "\n".join(glue(l) for l in t.split("\n"))


# ------------------------------------------------------------------ checkers


def check(text, lang, path):
    issues = []

    def add(lineno, code, msg, snippet=""):
        issues.append((lineno, code, msg, snippet.strip()))

    lines = text.split("\n")

    for i, line in enumerate(lines, 1):
        if "\x00" in line and line.strip("\x00 ") == "":
            continue
        # keep masked regions as a single non-space glyph so removing them
        # cannot fabricate " ," style false positives
        clean = re.sub(r"\x00+", "￼", line)

        for code, pat, msg in SLOP_PATTERNS:
            m = pat.search(clean)
            if m:
                add(i, code, msg, m.group(0))

        for m in re.finditer(r"\S*" + EMDASH + r"\S*", clean):
            add(i, "em-dash", "em dash: rewrite the sentence so no dash is needed",
                m.group(0))

        if re.search(r"(?<=\w) - (?=\w)", clean):
            add(i, "hyphen-as-dash",
                "spaced hyphen used as a dash: same crime, thinner glyph", clean[:60])

        if '"' in clean or re.search(r"(?<=\s)'|'(?=\s)", clean):
            add(i, "straight-quotes",
                "straight quotes: use «» in Russian, “” in English", clean[:60])

        if "..." in clean:
            add(i, "ellipsis", "use … (U+2026), not three periods", "...")

        if re.search(r"(?<=\S)  +(?=\S)", clean):
            add(i, "double-space", "double space", clean[:60])

        if re.search(r"\s+[,.;:!?%](?!\S)", clean):
            add(i, "space-before-punct", "space before punctuation", clean[:60])

        # homoglyphs: a word containing both alphabets
        for w in re.findall(r"[\w­]{2,}", clean):
            if re.search(r"[а-яёА-ЯЁ]", w) and re.search(r"[a-zA-Z]", w):
                add(i, "homoglyph", "Cyrillic and Latin mixed inside one word", w)

        # line ends on a glue word (only meaningful when the author controls wraps)
        last = re.findall(r"[\w’'-]+", clean)
        if last:
            tail = last[-1].lower()
            glue = RU_SHORT_AFTER if lang == "ru" else EN_SHORT_AFTER
            if tail in glue and len(clean) > 40:
                add(i, "dangling-word",
                    f"line ends on “{tail}”: glue it forward with a nbsp", tail)

    # widow check: one-word final line of a paragraph, measured at 72 cols
    for para_start, para in iter_paragraphs(lines):
        plain = re.sub(r"\s+", " ", re.sub(r"\x00+", "￼", para)).strip()
        if not plain or plain.startswith(("|", ">", "#", "-", "*")):
            continue
        wrapped = simple_wrap(plain, 72)
        if len(wrapped) > 1 and len(wrapped[-1].split()) == 1:
            issues.append((para_start, "widow",
                           "paragraph ends on a single word at 72 cols: "
                           "rewrite to fill the line", wrapped[-1]))

    return issues


def iter_paragraphs(lines):
    buf, start = [], 1
    for i, line in enumerate(lines, 1):
        if line.strip():
            if not buf:
                start = i
            buf.append(line)
        elif buf:
            yield start, " ".join(buf)
            buf = []
    if buf:
        yield start, " ".join(buf)


def simple_wrap(text, width):
    out, cur = [], ""
    for word in text.split(" "):
        cand = (cur + " " + word).strip()
        if len(cand) > width and cur:
            out.append(cur)
            cur = word
        else:
            cur = cand
    if cur:
        out.append(cur)
    return out


# --------------------------------------------------------------------- main


def process(path, args):
    if path == "-":
        original = sys.stdin.read()
    else:
        with open(path, encoding="utf-8") as fh:
            original = fh.read()

    lang = args.lang if args.lang != "auto" else detect_lang(original)
    text = original

    if args.fix:
        def one_pass(chunk):
            chunk = fix_spaces(chunk)
            chunk = fix_glyphs(chunk, lang)
            chunk = fix_quotes(chunk, lang)
            chunk = fix_nbsp(chunk, lang)
            return chunk

        text = apply_to_free_text(original, one_pass)
        text = apply_to_free_text(text, fix_headings_and_widows)
        if args.html:
            text = apply_to_free_text(text, lambda c: c.replace(NBSP, "&nbsp;"))
        if path == "-":
            sys.stdout.write(text)
        else:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
            print(f"fixed  {path}  [{lang}]", file=sys.stderr)

    masked, _ = mask_protected(text)
    issues = [] if args.slop_only else check(masked, lang, path)
    if not args.no_slop:
        issues += check_prose(masked, lang)
    label = path if path != "-" else "<stdin>"
    if not issues:
        print(f"ok     {label}  [{lang}]  no typography issues")
        return 0
    print(f"\n{label}  [{lang}]  {len(issues)} issue(s)")
    for lineno, code, msg, snippet in sorted(issues):
        loc = f"{label}:{lineno}"
        print(f"  {loc:<40} {code:<18} {msg}")
        if snippet:
            print(f"  {'':<40} {'':<18} → {snippet[:70]!r}")
    return 1


def main():
    ap = argparse.ArgumentParser(description="RU/EN typography linter")
    ap.add_argument("files", nargs="+", help="files to check, or - for stdin")
    ap.add_argument("--lang", choices=["ru", "en", "auto"], default="auto")
    ap.add_argument("--fix", action="store_true",
                    help="apply mechanical fixes in place (nbsp, quotes, glyphs)")
    ap.add_argument("--html", action="store_true",
                    help="with --fix, emit &nbsp; entities instead of U+00A0")
    ap.add_argument("--no-slop", action="store_true",
                    help="skip the §7 prose-quality checks")
    ap.add_argument("--slop-only", action="store_true",
                    help="run only the §7 prose-quality checks")
    args = ap.parse_args()
    if args.slop_only:
        args.no_slop = False

    rc = 0
    for path in args.files:
        rc |= process(path, args)
    return rc


if __name__ == "__main__":
    sys.exit(main())
