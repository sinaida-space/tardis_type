![Tardis Type](tardis_type.png)

# Tardis&nbsp;Type

A typography and prose-quality skill for Claude Code. Small file, bigger on
the&nbsp;inside.

## Why this exists

Most AI-generated prose reads the same way, and it fails on two separate levels of
the&nbsp;text.

<!-- typocheck: off -->

The typesetting gives it away first: em&nbsp;dashes doing the work of real syntax,
"not&nbsp;X, it's&nbsp;Y" contrastive framing, straight quotes, `...` instead of an
ellipsis, no non-breaking spaces, and single words stranded alone on the last line of a
paragraph.

The sentences give it away next: a pivotal moment that underscores a vibrant tapestry,
three parallel items in every list, a participle clause bolted onto every claim, experts
who argue without names, and a closing paragraph about how the future looks&nbsp;bright.

None of that is a style choice. It is the fastest way to signal "a&nbsp;model wrote this,"
and it makes text harder to read, not easier.

<!-- typocheck: on -->

Tardis&nbsp;Type is a house style, encoded as a Claude&nbsp;Code skill, that fixes both
layers on every piece of prose, in Russian and&nbsp;English.

## Who it's for

Anyone using Claude Code, or another Claude-Code-compatible agent, to write prose that
will be read by a real human: artists, writers, and anyone tired of text that reads
like it was generated. It applies to websites, emails, captions, decks, README files, artist
statements, and UI copy. It does not touch code, commands, URLs, or file paths.

## What it does

<!-- typocheck: off -->

- **Bans em&nbsp;dash rhetoric.** No dash used as a dramatic pause or a punchline beat, in
  either language.
- **Bans "not&nbsp;A, but&nbsp;B" framing**, in Russian and English, in every form.
- **Inserts non-breaking spaces** after short prepositions, conjunctions, and articles,
  between a number and its unit, before Russian particles, and after initials and titles.
- **Eliminates widows and orphans** by gluing the last two words of every heading,
  button, and list item, and by rewriting any paragraph that leaves a single word alone
  on its last line.
- **Fixes glyphs**: «ёлочки» in Russian, curly quotes in English, `…` instead of `...`,
  `–` for ranges, `×` for dimensions, `’` for apostrophes.
- **Strips AI slop at sentence level** (§7): the vocabulary (`delve`, `tapestry`,
  `pivotal`, `погрузиться в`, `ключевую роль`), copula avoidance, inflated significance,
  participle tails, forced triads, false ranges, vague attribution, stacked hedging,
  filler, signposting, authority tropes, aphorism formulas, sycophancy, and generic
  upbeat endings. Both languages, with a Russian list that is not a translation of the
  English&nbsp;one.
- **Refuses to invent facts.** No name, number, date, quote, or citation may enter a text
  that was not in the source. A vague claim gets cut, never&nbsp;decorated.
- **Knows when to stop editing** (§8): polish, dry prose, a lone `however`, one short
  emphatic sentence and curly quotes are not tells. It protects the things that mark a
  human writer instead of flattening&nbsp;them.
- Ships a **verification script** (`scripts/typocheck.py`) that scans a file for straight
  quotes, `...`, missing nbsp, widows and all of the above, and reports what still needs a
  manual&nbsp;pass.

<!-- typocheck: on -->

## How to install

Copy this skill into your Claude&nbsp;Code skills directory:

```bash
git clone https://github.com/sinaida-space/tardis_type.git
mkdir -p ~/.claude/skills/typography
cp tardis_type/SKILL.md ~/.claude/skills/typography/SKILL.md
cp -r tardis_type/scripts ~/.claude/skills/typography/scripts
```

Claude&nbsp;Code picks it up automatically once it sits in `~/.claude/skills/typography/`.
To check a file by hand:

```bash
python3 ~/.claude/skills/typography/scripts/typocheck.py path/to/file.md
```

## The checker

```
typocheck.py FILE [FILE ...] [--lang ru|en|auto] [--fix] [--html]
                             [--no-slop] [--slop-only]
```

`--fix` writes back only the mechanical transforms: nbsp insertion, quotes, ellipsis,
`×`, minus, range dashes, double spaces. Dash rewrites, widow rewrites and every
prose-quality hit are reported and never auto-fixed, because they need a rewritten
sentence rather than a&nbsp;substitution.

`--no-slop` runs typography only. `--slop-only` runs the prose pass only. Code fences,
inline code, URLs, paths and HTML are masked out before any check runs, and a document
that quotes bad examples on purpose can wrap them&nbsp;in:

```html
<!-- typocheck: off -->
...examples that are supposed to be wrong...
<!-- typocheck: on -->
```

## Credits

The typography layer is Sinaida's house style. The prose-quality layer (§7–§9) is adapted
from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
maintained by WikiProject AI&nbsp;Cleanup, by way of the MIT-licensed
[blader/humanizer](https://github.com/blader/humanizer) skill, rewritten for two
languages and for prose that gets published rather than&nbsp;edited into an
encyclopedia.

Where the two disagree, §9 of the skill records which one wins and why. Curly quotes
and en&nbsp;dashes stay here: a typeset text is not a&nbsp;typewritten&nbsp;one.

## About

Made by [Sinaida&nbsp;Krivchenko](https://sinaida.eu), a new media artist working in
interactive projections, TouchDesigner, and generative web pieces, currently based in
Prague.

Instagram: [@sin.ai.da](https://www.instagram.com/sin.ai.da/)
Website: [sinaida.eu](https://sinaida.eu)
