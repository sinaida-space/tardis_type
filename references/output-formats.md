# Output formats: CSS, .docx/.pptx/PDF, nbsp encoding

Loaded from SKILL.md when the target is a web page, document or slide file.

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
