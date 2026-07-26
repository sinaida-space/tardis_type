---
name: typography
description: Professional typography pass for every text written for Sinaida in Russian or English — non-breaking spaces, no widows/orphans, correct quotes/dashes/ellipses/units, and the hard ban on em-dash rhetoric and "not A, but B" constructions. Apply to ALL prose everywhere: websites, decks, emails, Instagram captions, .docx, README, artist statements, UI copy, and chat replies. Never applies to code, commands, URLs, or file paths.
---

# Typography — Sinaida's house rules

This skill is **always on** for prose. It has two layers:

1. **Micro-typography** — what characters go where (nbsp, quotes, dashes, units).
2. **Line-breaking hygiene** — no widows, no orphans, nothing dangling at a line end.

Plus a hard **ban list** that overrides everything, including grammar convenience.

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

---

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

Straight `"` and `'` are forbidden in prose. Apostrophe is always `’` (`don’t`, not
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
| JS/TS/Python string literal | the literal character, or ` ` |
| JSON / YAML values | the literal character |
| CSS `content:` | `"\00a0"` |
| LaTeX | `~` |
| CSV | avoid; use `white-space: nowrap` at render time instead |

In HTML also available: `&thinsp;` (thin space, for thousands separators),
`&#8209;` (non-breaking hyphen), `&shy;` (soft hyphen, for known long compounds).

Never emit a literal U+00A0 into code, a command, a URL, or a filename. It is invisible
and it breaks things.

---

## 7. Workflow

When writing any prose:

1. **Write for meaning first.** Typography is a pass, not a constraint on drafting.
2. **Rewrite every dash out** (§1.1–1.2) and every "not A, but B" (§1.3). Do this before
   touching spaces; rewriting changes the line breaks anyway.
3. **Run the nbsp pass** (§2) over the final wording.
4. **Read the last line of every paragraph, heading, and button** (§3). Fix widows by
   rewriting, then by gluing.
5. **Fix micro-typography** (§4–5): quotes, ellipses, ranges, units, symbols.
6. **Encode for the target** (§6).
7. **Verify** with the checker below and fix what it reports.

```bash
python3 ~/.claude/skills/typography/scripts/typocheck.py path/to/file.md
```

`--lang ru|en|auto` (default `auto`), `--fix` writes back the mechanical fixes
(nbsp insertion, quotes, ellipsis, `×`, double spaces). Dash rewrites and widow rewrites
are reported only, never auto-fixed: they need a human sentence, not a substitution.

Do not report a text as finished until the checker is clean or every remaining hit has a
stated reason.
