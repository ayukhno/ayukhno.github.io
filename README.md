# Oleksandr Yukhno — Make complexity useful.

Personal website: **https://ayukhno.github.io/**

A static website with editorial typography, a warm monochrome portrait, and an interactive systems drawing. No framework, installation, external fonts, analytics, cookies, or runtime network dependencies.

## Local preview

Run `npm start` and open http://127.0.0.1:4173. Stop with Ctrl+C. You can also open `dist/index.html` directly.

`npm run check` checks JavaScript syntax. No build is required.

## Edit and publish

- `dist/index.html`: copy, sections, and links.
- `dist/style.css`: typography, colors, and responsive layouts.
- `dist/script.js`: interactive diagram, clipboard, and reading progress.
- `dist/assets/`: portrait and site mark.

Push changes to `main` to publish automatically through `.github/workflows/pages.yml`. Only `dist/` is uploaded to GitHub Pages. Local research notes and design drafts are excluded from this repository.

## Diagram

Choose **See what changes** to reveal the connected system. **Processes**, **People**, and **AI** highlight different contributions. **Show the tangle** resets the drawing.

**People:** Context → People → Analysis → Decisions → Outcome.

**AI:** Context → Analysis → Decisions → Processes → Outcome, with AI marked on Context → Analysis. People → Decisions is solid; Context → People and Analysis → People are dashed.
