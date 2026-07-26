![Tardis Type](tardis_type.png)

# Tardis&nbsp;Type

A typography skill for Claude Code. Small file, bigger on the&nbsp;inside.

## Why this exists

Most AI-generated prose reads the same: em&nbsp;dashes doing the work of real syntax,
"not&nbsp;X, it's&nbsp;Y" contrastive framing, straight quotes, `...` instead of an
ellipsis, no non-breaking spaces, and single words stranded alone on the last line of a
paragraph. None of that is a style choice. It is the fastest way to signal "a&nbsp;model
wrote this," and it makes text harder to read, not easier.

Tardis&nbsp;Type is a house style, encoded as a Claude&nbsp;Code skill, that fixes all of
it automatically, on every piece of prose, in Russian and English.

## Who it's for

Anyone using Claude Code, or another Claude-Code-compatible agent, to write prose that
will be read by a real human — artists, writers, and anyone tired of text that reads like
it was generated. It applies to websites, emails, captions, decks, README files, artist
statements, and UI copy. It does not touch code, commands, URLs, or file paths.

## What it does

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
- Ships a **verification script** (`scripts/typocheck.py`) that scans a file for
  straight quotes, `...`, missing nbsp, and reports what still needs a manual pass.

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

## About

Made by [Sinaida&nbsp;Krivchenko](https://sinaida.eu), a new media artist working in
interactive projection, TouchDesigner, GLSL shaders, and generative web pieces, based in
Prague.

Instagram: [@sin.ai.da](https://www.instagram.com/sin.ai.da/)
Website: [sinaida.eu](https://sinaida.eu)
