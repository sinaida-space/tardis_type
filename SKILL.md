---
name: typography
description: Professional typography and prose-quality pass for every text written for Sinaida in Russian or English — non-breaking spaces, no widows/orphans, correct quotes/dashes/ellipses/units, the hard ban on em-dash rhetoric and "not A, but B" constructions, and the full anti-slop pass that strips AI vocabulary, inflated significance, rule-of-three padding, hedging, signposting, and sycophancy. Apply to ALL prose everywhere: websites, decks, emails, Instagram captions, .docx, README, artist statements, UI copy, and chat replies. Never applies to code, commands, URLs, or file paths.
---

# Typography — Sinaida's house rules

This skill is **always on** for prose. It has three layers:

1. **Micro-typography** — what characters go where (nbsp, quotes, dashes, units).
2. **Line-breaking hygiene** — no widows, no orphans, nothing dangling at a line end.
3. **Prose quality** (§7) — the sentence-level tells that mark a text as machine-written:
   inflated significance, AI vocabulary, forced triads, hedging, signposting, sycophancy.

Plus a hard **ban list** that overrides everything, including grammar convenience.

Layer 3 is the one that decides whether a reader trusts the text. Correct nbsp on a
sentence that says "this pivotal moment underscores the vibrant tapestry of her practice"
is a well-set piece of slop. Fix the sentence first, then the spaces.

---

## 0. Scope — where this applies

| Apply | Never touch |
|---|---|
| Web copy, HTML/JSX text nodes, UI strings | Code, identifiers, variable names |
| Emails, letters, pitches, proposals | Shell commands, CLI flags |
| Instagram/LinkedIn posts, captions | URLs, slugs, file paths, filenames |
| .docx / .pptx / PDF deliverables | JSON keys, YAML keys, env vars |
| README, docs, artist statements | Git commit messages and branch names |
| Chat replies to Sinaida | Alt text of decorative images (nbsp fine, but don't fuss) |
| Subtitles, video captions | Anything inside a fenced code block |

If a string is both (a UI label that is also a translation key value) — typography the
displayed value, leave the key alone.

---

<!-- typocheck: off -->

## 1. Ban list — non-negotiable, all languages, all channels

### 1.1 Em dash `—` as a rhetorical device: forbidden

No `—` used as a parenthetical break, a dramatic pause, an appositive, or a "and here
comes the punchline" beat. That pattern is the single loudest AI-slop signal and Sinaida
hates it.

**Do not "fix" it by swapping in ` – ` or ` - ` in the same slot.** Same crime, thinner
glyph. Rewrite the sentence so no dash is wanted:

- split into two sentences
- use a colon when the second half explains the first
- use a comma or parentheses when it is a genuine aside
- use "because / so / and" and let the syntax carry the load
- cut the aside entirely (usually the best answer)

| Wrong | Right |
|---|---|
| `AI is a prosthetic — it restores capacity, it doesn't create.` | `AI is a prosthetic. It restores capacity. It doesn't create.` |
| `Она работает с проекциями — светом, который живёт в пространстве.` | `Она работает с проекциями: со светом, который живёт в пространстве.` |
| `The move to Prague — unplanned, disruptive — is still being metabolised.` | `The move to Prague was unplanned and disruptive. It is still being metabolised.` |

### 1.2 Em dash `—` where Russian grammar genuinely requires it: allowed, but last resort

Russian has three places a dash is a grammatical norm, not a stylistic flourish:

- subject–predicate link with a zero copula: `Прага — не дом.`
- direct speech: `— Я не знаю.`
- ellipsis of a sentence member: `Я живу в Праге, она — в Амстердаме.`

In those slots a dash is not slop. **Still restructure first**: add a copula (`Прага не
стала домом`), turn the noun into a verb clause, or reorder. Reach for `—` only when
every rewrite is worse than the dash. Aim for zero dashes per text; one is a compromise,
two is a failure of the rewrite.

When a dash does survive: `слово&nbsp;— слово` (nbsp before, ordinary space after, so
the dash can never start a line).

English gets **no exception**. English does not need the dash grammatically, so English
prose written for Sinaida contains zero `—`.

### 1.3 "Not A, but B" contrastive framing: forbidden

Every shape of it, both languages:

- `not just X, it's Y` · `X, not Y` · `less about X, more about Y`
- `isn't about X. It's about Y.` · `X isn't decoration, it's structure`
- `не просто X, а Y` · `не X, а Y` · `дело не в X, дело в Y`

State what the thing **is**, directly, in the first clause. If the contrast carries real
information, give the rejected option its own sentence with its own reason, or drop it.

| Wrong | Right |
|---|---|
| `This isn't a filter, it's a generative shader.` | `This is a generative shader. Nothing is sampled from the source image.` |
| `Это не декорация, это инфраструктура.` | `Это инфраструктура: без неё эстетика не выживает.` |

### 1.4 The rest of the anti-voice (carried from her global rules)

Banned: "thrilled to announce", "passionate about", "excited to share", "grateful for
the opportunity", "in today's fast-paced world", "delve", "unlock", "elevate",
"seamless", "game-changer", emoji spray, hashtag walls, "girlboss"/"female founder"
framing, uncritical AI hype.

The full vocabulary and rhetoric ban lives in §7. §1 is the part that is never negotiable
in any register; §7 is the part that needs judgement.

---

<!-- typocheck: on -->

## 2. Non-breaking space — the core mechanic

The character is **U+00A0**. How to encode it depends on the target; see §6.
Everything below is written as `&nbsp;` for legibility only.

### 2.1 The one governing principle

> A line must never end on a word that has no meaning of its own, and must never begin
> with a fragment that belongs to the word before it.

Everything in this section is that rule, itemised.

### 2.2 Russian — nbsp AFTER these (glue forward)

- **Prepositions and conjunctions of 1–3 letters** at the start of a phrase:
  `в&nbsp;`, `на&nbsp;`, `с&nbsp;`, `к&nbsp;`, `по&nbsp;`, `за&nbsp;`, `из&nbsp;`,
  `от&nbsp;`, `до&nbsp;`, `для&nbsp;`, `при&nbsp;`, `над&nbsp;`, `под&nbsp;`,
  `про&nbsp;`, `без&nbsp;`, `и&nbsp;`, `а&nbsp;`, `но&nbsp;`, `да&nbsp;`, `что&nbsp;`,
  `как&nbsp;`, `или&nbsp;`, `не&nbsp;`, `ни&nbsp;`
- **Any single-letter word, always**: `в&nbsp;Праге`, `я&nbsp;не`, `о&nbsp;свете`
- **Initials and titles**: `А.&nbsp;С.&nbsp;Пушкин`, `г-н&nbsp;Новак`,
  `тов.&nbsp;Иванов`
- **Number + unit / noun**: `10&nbsp;кг`, `60&nbsp;fps`, `1920&nbsp;px`,
  `5&nbsp;млн`, `300&nbsp;₽`, `25&nbsp;мая`, `2026&nbsp;г.`, `XX&nbsp;в.`,
  `3&nbsp;часа`
- **Abbreviation + number**: `№&nbsp;5`, `§&nbsp;3`, `с.&nbsp;12`, `стр.&nbsp;40`,
  `рис.&nbsp;4`, `табл.&nbsp;2`, `гл.&nbsp;7`
- **Geographic / address abbreviations**: `г.&nbsp;Прага`, `ул.&nbsp;Каприкорн`,
  `д.&nbsp;12`, `кв.&nbsp;5`
- **Multi-part abbreviations**: `и&nbsp;т.&nbsp;д.`, `и&nbsp;т.&nbsp;п.`,
  `т.&nbsp;е.`, `и&nbsp;др.`, `см.&nbsp;выше`, `P.&nbsp;S.`

### 2.3 Russian — nbsp BEFORE these (glue backward)

- **Particles**: `&nbsp;же`, `&nbsp;бы`, `&nbsp;б`, `&nbsp;ли`, `&nbsp;ль`,
  `&nbsp;уж`, `&nbsp;ж`
- **A dash that survived §1.2**: `слово&nbsp;—`
- **Short final word (1–2 letters) at the end of a sentence**: `остался&nbsp;он.`
- **Units after a number** (same rule as 2.2, stated from the other side)

### 2.4 English — nbsp AFTER these

- **Articles and one/two-letter words**: `a&nbsp;`, `an&nbsp;`, `the&nbsp;`,
  `I&nbsp;`, `to&nbsp;`, `of&nbsp;`, `in&nbsp;`, `on&nbsp;`, `at&nbsp;`, `by&nbsp;`,
  `is&nbsp;`, `as&nbsp;`, `it&nbsp;`, `we&nbsp;`, `or&nbsp;`, `if&nbsp;`, `so&nbsp;`
- **Titles and initials**: `Mr.&nbsp;Novak`, `Dr.&nbsp;Herd`,
  `J.&nbsp;R.&nbsp;R.&nbsp;Tolkien`
- **Number + unit**: `60&nbsp;fps`, `10&nbsp;km`, `4&nbsp;GB`, `1920&nbsp;px`,
  `25&nbsp;°C`, `€500`, `$5` (currency symbol touches the digits, no space)
- **Reference + number**: `Fig.&nbsp;3`, `p.&nbsp;12`, `No.&nbsp;5`,
  `Chapter&nbsp;4`, `WCAG&nbsp;2.1&nbsp;AA`
- **Venue/place name + numbered unit**, even when the number sign is the Cyrillic `№`
  inside otherwise-English prose (a loanword venue name like "Sklad" keeps its native
  numbering convention): `Sklad&nbsp;№3`, `Studio&nbsp;№2`, `Hall&nbsp;№12`,
  `Gate&nbsp;№7`. The glue sits between the name and `№3`, not inside `№3` itself —
  that pair stays solid, no space, matching how it prints on the venue's own signage.
- **Dates**: `May&nbsp;25`, `25&nbsp;May&nbsp;2026`
- **Never split**: `COVID-19`, `WWII`, `TouchDesigner&nbsp;2023`, version numbers

### 2.5 English — nbsp BEFORE these

- **The last word of a heading, button, link, or list item** (widow prevention, §3.2)
- **A trailing short word**: `and it&nbsp;is.`
- **Percent, units, and closing references**: `50&nbsp;%` if spaced at all (see §4.6)

### 2.6 Never put nbsp

- Between more than two words in a row (freezes the line, causes overflow on mobile)
- Inside anything in the "never touch" column of §0
- Around long words on narrow mobile layouts — a 320&nbsp;px viewport breaks before it
  honours your typography

---

## 3. Widows and orphans

Definitions, so the fix is the right one:

- **Widow** — the last line of a paragraph left alone at the top of the next column/page,
  or (loose usage, and the one that matters most on the web) a single word alone on the
  last line of a paragraph.
- **Orphan** — the first line of a paragraph left alone at the bottom of a column/page.

### 3.1 Prose level (works everywhere, including plain text)

- Read every paragraph's last line. One word alone: rewrite. Add or cut two or three
  words earlier in the paragraph so the line fills. This is a **writing** fix, and it is
  the only one that survives a copy-paste into any medium.
- Never end a line with: a preposition, a conjunction, a particle, an initial, `№`, `§`,
  an opening quote or bracket, a hyphenated fragment.
- Never begin a line with: a closing quote or bracket, a punctuation mark, a unit, `%`,
  a dash that belongs to the previous phrase.
- **Headings, buttons, CTAs, nav items, card titles, list items**: glue the last two
  words with nbsp, always, without checking. These are short and high-visibility, and a
  one-word second line in a heading is the most visible typographic failure there is.

### 3.2 CSS (web output)

```css
/* body copy: avoid a single-word last line, browser-side */
p, li, dd, blockquote, figcaption {
  text-wrap: pretty;
  hyphens: auto;           /* requires lang="ru" / lang="en" on the element or <html> */
  hyphenate-limit-chars: 6 3 3;
}

/* short headings: even line lengths beat ragged ones */
h1, h2, h3, h4, .cta, .btn, .card__title {
  text-wrap: balance;      /* browsers apply it up to ~4 lines */
}

/* print / PDF: real widow & orphan control */
@media print {
  p, li { orphans: 3; widows: 3; }
  h1, h2, h3, h4 { break-after: avoid; page-break-after: avoid; }
  figure, table, blockquote { break-inside: avoid; }
}

/* atomic units that must never break */
.nowrap, .price, .measure { white-space: nowrap; }

/* optical margin alignment, opt-in */
.prose { hanging-punctuation: first last; }
```

`text-wrap: pretty` is a browser hint, not a guarantee. It never replaces the nbsp in a
heading or the paragraph rewrite in §3.1.

### 3.3 .docx / .pptx / PDF output

- Turn on widow/orphan control (`w:widowControl`) — it is the Word default; do not
  disable it.
- `Keep with next` on every heading paragraph.
- `Keep lines together` on short blocks: pull quotes, captions, addresses, signatures.
- Never fix a bad break with a manual line break or an empty paragraph. Reflow kills it.
- Table rows: disallow row splitting across pages for rows under ~4 lines.

### 3.4 Terminal / plain text / Markdown

Widows are invisible until they are not — the reader's window width is unknown. So:
keep paragraphs short, keep lines under ~90 characters when you control the wrap, and
still write out the single-word last lines. Literal U+00A0 works in Markdown, .docx,
email, and chat, and it renders as a normal space in a terminal.

---

## 4. Micro-typography reference

### 4.1 Quotes

| Context | Outer | Nested |
|---|---|---|
| Russian | `«ёлочки»` | `„лапки"` |
| English | `"curly"` | `'single'` |

Straight `"` and `'` are forbidden in prose. Apostrophe is always `'` (`don't`, not
`don't`). Russian keeps the outer `«»` even when the quoted string is English:
`«TouchDesigner»`.

### 4.2 Dashes and hyphens

| Character | Use |
|---|---|
| `-` hyphen | compound words, `какой-то`, `full-time`, phone numbers |
| `–` en dash | numeric and date ranges, **no spaces**: `2010–2015`, `10–20&nbsp;fps`, `с&nbsp;10 до&nbsp;20` |
| `—` em dash | only per §1.2, only Russian, only grammatically forced |
| `−` U+2212 minus | negative numbers and arithmetic: `−5&nbsp;°C`, not a hyphen |

If a range's endpoints already contain spaces or dashes, use `с … до …` / `from … to …`
instead of a dash.

### 4.3 Ellipsis

`…` (U+2026), never `...`. Russian order with other marks: `?..` `!..` `…?` — and never
`....`.

### 4.4 Numbers and math

- Thin space or nbsp as thousands separator: `1 000 000` (never a comma in Russian).
- Decimal separator: `,` in Russian, `.` in English.
- Multiplication sign `×`, not `x`: `1920×1080`, `2×2`. No spaces in dimensions.
- Fractions: `½ ¼ ¾` where they exist.
- Degrees: RU `25&nbsp;°C` (space, per GOST), EN `25°C` (no space). Angles never take a
  space in either: `45°`.

### 4.5 Symbols

`©` `®` `™` `№` `§` `→` `←` `•` — real characters, never `(c)`, `(tm)`, `->`, `No.` in
Russian. `№` is Russian-only; English uses `No.&nbsp;5`.

### 4.6 Percent

Set solid in both languages: `50%`, `+25%`. (GOST specifies `50&nbsp;%`; use the spaced
form only in a document that is explicitly GOST-conforming, and then keep it nbsp.)

### 4.7 Spacing hygiene

- No double spaces, ever.
- No space before `. , ; : ! ? ) ] » …`; one space after.
- No space after `( [ «`.
- No space before or after `/` in `и/или`, `and/or`.
- No trailing whitespace at end of lines.
- One space after a sentence-ending period, never two.

---

## 5. Language-specific extras

### Russian
- `ё` — write it in art/poetic/personal texts and in names (`Королёв`); optional in
  dry technical copy, but be consistent within a document.
- Comma before `а` and `но`, always.
- `!?` is wrong; write `?!`.
- No `!!!` or `???`. One mark.
- Direct speech uses `—` at the line start with a following space, and that dash is
  exempt from §1.1 (it is punctuation, not rhetoric). Prefer quoted speech when possible.
- Cyrillic/Latin homoglyph check: `с о е а р х у к`, `М Н О Р С Т Х А В Е К` — never mix
  alphabets inside one word.

### English
- Serial (Oxford) comma: on.
- Sentence case for headings and buttons, not Title Case, unless the surrounding design
  system already uses Title Case.
- `%` `&` spelled out in body prose (`and`), symbols kept in labels and data.
- Non-breaking hyphen U+2011 for things like `e‑mail`, `re‑render` when a break there
  would read badly.

---

## 6. How to encode U+00A0 per target

| Target | Write |
|---|---|
| HTML, JSX text, Markdown-in-HTML | `&nbsp;` (or the literal character) |
| Markdown, plain text, email body, chat, .docx, .pptx | the literal U+00A0 character |
| JS/TS/Python string literal | the literal character, or ` ` |
| JSON / YAML values | the literal character |
| CSS `content:` | `"\00a0"` |
| LaTeX | `~` |
| CSV | avoid; use `white-space: nowrap` at render time instead |

In HTML also available: `&thinsp;` (thin space, for thousands separators),
`&#8209;` (non-breaking hyphen), `&shy;` (soft hyphen, for known long compounds).

Never emit a literal U+00A0 into code, a command, a URL, or a filename. It is invisible
and it breaks things.

---

<!-- typocheck: off -->

## 7. Prose quality: the anti-slop pass

Adapted from Wikipedia's *Signs of AI writing* (WikiProject AI Cleanup) and the
`blader/humanizer` skill, rewritten for Sinaida's registers and for Russian as well as
English.

Two rules govern this whole section:

- **Information wins over shape.** Every claim in the draft survives the rewrite, but
  depth does not have to be uniform. Compress the dull parts, dwell where a human would,
  merge or split paragraphs freely.
- **Never invent a fact to fix a sentence.** No name, number, date, quote, venue, or
  citation may enter the text that was not in the source or given by Sinaida. A vague
  claim gets cut, never decorated. (Fiction and concept texts for art pieces are exempt:
  there, invented detail is the work.)

### 7.1 Overused AI vocabulary

**English, cut on sight:** delve, tapestry, testament, landscape (figurative), realm,
myriad, pivotal, crucial, vital, robust, seamless, leverage (verb), foster, cultivate,
navigate (figurative), embark, unlock, elevate, enhance, showcase, underscore (verb),
highlight (verb), intricate, interplay, garner, align with, resonate with, ever-evolving,
groundbreaking, cutting-edge, meticulous, comprehensive, holistic, transformative,
immersive (unless the piece is literally immersive), vibrant, rich (figurative), profound,
boasts, nestled, in the heart of, renowned, breathtaking, stunning, must-visit.

**Russian, cut on sight:** ключевую роль, играет важную роль, неотъемлемой частью,
поистине, уникальный (когда ничего уникального нет), богатое наследие, глубоко укоренён,
подчёркивает значимость, отражает более широкий, знаковый момент, в современном мире,
в эпоху цифровых технологий, погрузиться в, раскрыть потенциал, вывести на новый уровень,
бесшовный, инновационный, передовой, комплексный подход, важно отметить, что,
стоит отметить, что, нельзя не отметить, таким образом, следует подчеркнуть,
захватывающий, впечатляющий, потрясающий.

These co-occur. One of them is a slip; three in a paragraph is a machine.

**Before:** `An enduring testament to Italian influence is the widespread adoption of
pasta in the local culinary landscape, showcasing how these dishes integrated.`
**After:** `Pasta arrived with Italian colonisation and is still common in the south.`

### 7.2 Copula avoidance

**Watch:** serves as, stands as, marks, represents, constitutes, boasts, features,
offers · служит, является (там, где хватает тире или нуля), выступает в качестве,
представляет собой.

Say **is**. `Gallery 825 serves as the exhibition space` → `Gallery 825 is the exhibition
space`. In Russian, prefer the zero copula and then rewrite the dash away per §1.2:
`Прага не стала домом`, not `Прага — не дом`.

### 7.3 Inflated significance, legacy, and broader trends

**Watch:** a pivotal/crucial/key moment, marks a shift, setting the stage for, reflects a
broader, contributing to, leaving an indelible mark, symbolising its enduring, part of a
wider movement, underscores its importance · знаковый момент, поворотная точка,
оставил неизгладимый след, вписывается в более широкий контекст.

The tell is a sentence that explains why the previous sentence mattered. Delete it. If
the significance is real, it is already visible in the fact.

**Before:** `The institute was established in 1989, marking a pivotal moment in the
evolution of regional statistics.`
**After:** `The institute was established in 1989.`

### 7.4 Superficial "-ing" tails

A participle clause bolted onto the end of a sentence to fake depth: `…, highlighting the
community's connection to the land`, `…, ensuring a smooth experience`, `…, reflecting
her practice`, `…, fostering collaboration`. Russian equivalent: деепричастные хвосты
(`…, подчёркивая связь с местом`, `…, отражая её практику`).

Cut the tail. If it carried real information, give it its own sentence with a subject.

### 7.5 Rule of three

Three parallel items, over and over, because triads sound complete. `Innovation,
inspiration, and industry insights.` `Свет, звук и движение.`

Break the rhythm: two items, or four, or one item with a real qualifier. Keep a triad
only when the three things genuinely exist and are genuinely parallel.

### 7.6 Negative parallelism and tailing negations

Beyond §1.3, this covers the clipped fragment stuck on the end: `no guessing`,
`no wasted motion`, `никаких компромиссов`, `без лишних движений`. Write the real clause
or cut it.

### 7.7 Elegant variation (synonym cycling)

`The protagonist… the main character… the central figure… the hero.` Repetition-penalty
behaviour. Repeat the plain noun, or use a pronoun. In Russian this shows up as
`художница… автор… создательница… она`. Pick one and stay.

### 7.8 False ranges

`from X to Y` where X and Y are not endpoints of any scale: `from the Big Bang to the
cosmic web`, `от пикселя до философии`. Replace with a plain list of what is actually
covered.

### 7.9 Vague attribution and weasel words

**Watch:** experts argue, observers have noted, industry reports suggest, some critics,
several publications, it is widely believed · эксперты считают, наблюдатели отмечают,
принято считать, многие специалисты.

Name the source or cut the claim. Never invent an attribution to make a sentence sound
sourced.

### 7.10 Hedging stacks and filler

`It could potentially possibly be argued that…` → `The policy may affect outcomes.`
One hedge maximum per sentence, and only when the uncertainty is real.

| Filler | Write |
|---|---|
| In order to achieve this | To do this |
| Due to the fact that | Because |
| At this point in time | Now |
| In the event that | If |
| Has the ability to | Can |
| It is important to note that the data shows | The data shows |
| В связи с тем, что | Потому что |
| На данный момент времени | Сейчас |
| Обладает возможностью | Может |
| Важно отметить, что исследование показывает | Исследование показывает |

### 7.11 Signposting and meta-announcements

`Let's dive in`, `let's explore`, `here's what you need to know`, `now let's look at`,
`without further ado` · `давайте разберёмся`, `рассмотрим подробнее`, `итак, начнём`.

Announcing the thing is not doing the thing. Delete the announcement and start.

### 7.12 Persuasive authority tropes

`The real question is`, `at its core`, `in reality`, `what really matters`,
`fundamentally`, `the deeper issue` · `на самом деле`, `по сути`, `главный вопрос в том`,
`если копнуть глубже`.

These pretend to cut through noise before restating an ordinary point. Say the point.

### 7.13 Aphorism formulas

`X is the Y of Z`, `X becomes a trap`, `the language of…`, `the architecture of…`,
`the currency of…` · `X — это язык Y`, `новая валюта внимания`.

Reusable-sounding profundity with no precision behind it. Replace with the concrete claim
it is gesturing at. Sinaida's artist statements are the highest-risk surface for this:
they invite it, and it is exactly where it reads worst.

### 7.14 Fake-candid openers

`Honestly?`, `Look,`, `Here's the thing`, `Let's be honest`, `Real talk` ·
`Честно говоря`, `Скажем прямо`, `Давайте начистоту` used as a theatrical pause before an
ordinary claim. A person being honest just says the thing. (Mid-sentence `honestly` in
casual writing is fine; the standalone hook is the tell.)

### 7.15 Manufactured punchlines and staccato drama

Every sentence landing like a quotable closer, or a run of short fragments stacked to
manufacture tension: `Then it arrived. No symmetry. No nostalgia. The old rules were
gone.` One short sentence for emphasis is good writing. Four in a row is a machine
imitating one.

### 7.16 Sycophancy and chatbot artifacts

`Great question!`, `You're absolutely right`, `I hope this helps`, `Let me know if…`,
`Would you like me to…`, `Here is a…`, `Of course!`, `Certainly!` These belong to
conversation, not to a delivered text, and they should not appear in one. In chat replies
to Sinaida they are also just noise: answer, do not flatter.

### 7.17 Generic positive conclusions

`The future looks bright.` `Exciting times lie ahead.` `A major step in the right
direction.` `Впереди много интересного.` `Это только начало.`

Cut the paragraph. End on the last concrete fact. A send-off is not a conclusion.

### 7.18 Knowledge gaps and speculative filler

`While specific details are limited…`, `based on available information`,
`maintains a low profile`, `keeps personal details private`, `likely studied`,
`it is believed that` · `информация не представлена в открытых источниках, что говорит
о…`, `вероятно, она…`

Two failures at once: a paragraph about not finding a source, then invented filler to
cover the gap. Say plainly what is not known, or cut the sentence. Never guess a
biography.

### 7.19 Structural tells

- **Boldface spray.** Bold is for a term being defined, not for every noun phrase the
  model thought was important. In body prose, a paragraph with three bold runs has none.
- **Inline-header lists.** `- **Performance:** Performance has been improved.` Either
  write real prose, or write list items that are not restatements of their own labels.
- **Title Case Headings.** Sentence case in English (§5). Russian never title-cases.
- **Emoji in headings and bullets.** Zero, in every deliverable. §1.4.
- **Fragmented headers.** A heading followed by a one-line restatement of the heading
  before the real content starts. Delete the warm-up line.
- **Diff-anchored writing.** Docs and comments narrating a change instead of describing
  the thing: `This replaces the previous approach of…`. Unless the document is
  version-scoped (changelog, release notes), describe what is, not what changed.
- **"Challenges and future prospects" sections.** Formulaic and usually contentless.
  If there are real problems, name them in the body.

---

## 8. What NOT to flag

Good human prose hits some of these patterns. Over-editing produces text that is clean,
voiceless, and just as obviously machine-handled. None of the following is a tell on its
own:

- **Polish.** Perfect grammar means an editor, not a model.
- **Mixed registers.** Casual and technical in one paragraph is a person in a technical
  field, which is exactly what Sinaida is.
- **Dry prose.** AI has *specific* tells. Dryness without them is just dry.
- **Formal vocabulary.** §7.1 bans specific words, not all long ones. Do not flatten
  `ostensibly` or `констатировать` because they sound bookish.
- **One transition word.** A single `however` or `таким образом` is not a confession. A
  pile-up is.
- **A single short emphatic sentence.** §7.15 is about runs, not instances.
- **`honestly` or `look` mid-sentence.** The standalone theatrical opener is the tell.
- **Unsourced claims.** Most writing is unsourced.
- **Curly quotes.** Required here (§4.1). They are a Word/macOS artifact everywhere else,
  never evidence of anything.

Look for **clusters**. One triad means nothing. A triad plus `vibrant tapestry` plus a
`Conclusion` section plus three bold runs is a confession.

### Signs of a human wrote it (protect these)

When these appear, edit less:

- **Specific, hard-to-fabricate detail.** A real address, a strange quote, a named
  street in Prague. Models round specifics off; people hoard them.
- **Mixed feelings, unresolved.** "I think it works and it still bothers me."
- **Dated references.** Slang and in-jokes that pin to a year and a scene.
- **Real variation in sentence length.** Machines drift to an even mid-length cadence.
- **Genuine asides and self-corrections.** "(I keep wanting to write *almost* here.)"
- **An editorial choice the writer can defend.** If she can say why the word is that
  word, it stays, including if it violates something above.

---

## 9. Where this skill overrules the humanizer source

The upstream skill optimises for "does not look AI-written" on English Wikipedia. This
one optimises for Sinaida's published prose in two languages. Three deliberate conflicts:

| Upstream says | Here | Why |
|---|---|---|
| Use straight quotes `"..."`; curly quotes are a ChatGPT tell | Curly quotes and «ёлочки» are **mandatory** (§4.1) | Straight quotes are a typewriter limitation. Her texts are typeset, not typed. |
| Ban en dashes `–` along with em dashes | En dash **required** for numeric ranges, unspaced (§4.2) | A range dash is punctuation, not rhetoric. §1 bans the *rhetorical* dash only. |
| Drop hyphens in predicate position (`the report is high quality`) | Follow standard orthography in each language | Russian compound rules are not English ones, and inconsistent hyphens read as errors, not as voice. |

Everything else in §7 stands as written.

---

<!-- typocheck: on -->

## 10. Workflow

When writing any prose:

1. **Write for meaning first.** Typography is a pass, not a constraint on drafting.
2. **Run the anti-slop pass** (§7) on the draft, before any character-level work.
   Ask the two audit questions out loud:
   - *What makes this obviously AI-generated?*
   - *Does the rewrite state any fact, name, number, date, or citation that was not in
     the source?* A fabrication is a defect even when it reads better.
   Then check the result against §8 and put back anything you flattened.
3. **Rewrite every dash out** (§1.1–1.2) and every "not A, but B" (§1.3). Do this before
   touching spaces; rewriting changes the line breaks anyway.
4. **Run the nbsp pass** (§2) over the final wording.
5. **Read the last line of every paragraph, heading, and button** (§3). Fix widows by
   rewriting, then by gluing.
6. **Fix micro-typography** (§4–5): quotes, ellipses, ranges, units, symbols.
7. **Encode for the target** (§6).
8. **Verify** with the checker below and fix what it reports.

```bash
python3 ~/.claude/skills/typography/scripts/typocheck.py path/to/file.md
```

`--lang ru|en|auto` (default `auto`), `--fix` writes back the mechanical fixes
(nbsp insertion, quotes, ellipsis, `×`, double spaces). Dash rewrites, widow rewrites and
every §7 hit are reported only, never auto-fixed: they need a human sentence, not a
substitution. `--no-slop` silences §7 checks, `--slop-only` runs nothing else.

Do not report a text as finished until the checker is clean or every remaining hit has a
stated reason.

### 10.1 Voice sample beats every rule here

If Sinaida supplies a sample of her own writing, read it first and match its habits:
sentence length, paragraph openings, punctuation density, recurring phrases. A real
sample outranks §7 and §8 entirely, and it outranks §1.1 for that text only if she is
plainly using dashes on purpose. Matching the author beats scrubbing the tell. §1.3, §2,
§3 and §4 still apply: those are typesetting, not voice.

### 10.2 Invocation modes

- **Pasted text.** Deliver the rewrite plus a short list of what was changed and why.
- **File.** Read it, run the whole loop internally, write the final text back in place,
  and report a summary in chat instead of pasting the file. Prose only: frontmatter,
  code blocks, data and link targets stay untouched.
- **Embedded** (this skill running as one step of a larger task). Output the final prose
  only. No draft, no audit list, no summary.
