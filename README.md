# Oleksandr Yukhno — personal website

[![Publish website](https://github.com/ayukhno/ayukhno.github.io/actions/workflows/pages.yml/badge.svg)](https://github.com/ayukhno/ayukhno.github.io/actions/workflows/pages.yml)
[![CodeQL](https://github.com/ayukhno/ayukhno.github.io/actions/workflows/codeql.yml/badge.svg)](https://github.com/ayukhno/ayukhno.github.io/actions/workflows/codeql.yml)
[![License: MIT (code)](https://img.shields.io/badge/license-MIT%20(code)-blue.svg)](LICENSE)

Source of **<https://ayukhno.github.io/>**: an online CV that tells the path from electronics and software through project delivery and retail operations to applied AI.

> **Build your own CV from this one.** To read my CV, the site is all you need. The rest of this README is for anyone who wants to repeat it: the structure, local preview, PDF and AI-search versions generated from one source of facts, checks, publishing and security. The code is MIT, so fork it and replace my texts and photo with your own.

| Language | Address |
|---|---|
| English | [`/`](https://ayukhno.github.io/) |
| Ukrainian | [`/uk.html`](https://ayukhno.github.io/uk.html) |

The site is static HTML, CSS and a little JavaScript. It has no framework, no build step, no runtime dependencies, no external fonts, no cookies and no analytics.

## Project structure

```text
dist/                      published as-is to GitHub Pages
├── index.html             CV in English (default)
├── uk.html                CV in Ukrainian
├── en.html                redirect from the old English address
├── story.css, story.js    styles and section highlighting
├── assets/                portrait, site mark, social preview image
├── cv/                    downloadable CV (PDF, EN/UA) and Markdown versions for AI systems
├── llms.txt               summary and links for AI assistants
├── story/                 redirects from the old /story/ addresses
├── 404.html, robots.txt, sitemap.xml
└── .well-known/security.txt
server.mjs                 local preview server (Node.js, no dependencies)
tools/cv/                  builds dist/cv/* and dist/llms.txt from one source of facts
.github/workflows/         checks, deploy, CodeQL
```

## Run locally

Requires Node.js; the version is in [`.nvmrc`](.nvmrc).

```sh
npm start      # preview at http://127.0.0.1:4173 (PORT=… to change)
```

You can also open `dist/index.html` or `dist/uk.html` directly in a browser.

## Downloadable CV

The PDF and Markdown CVs come from one source of facts in [`tools/cv/build_cv.py`](tools/cv/build_cv.py). After changing facts on the site, update that file too and rebuild:

```sh
python3 tools/cv/build_cv.py   # Markdown versions and llms.txt
sh tools/cv/render_pdf.sh      # PDFs (needs the gstack headless browser)
```

## Checks

```sh
npm ci         # installs only the linters
npm test       # JavaScript syntax, HTML validation (html-validate), CSS lint (Stylelint)
```

CI runs the same checks and a link check ([lychee](https://github.com/lycheeverse/lychee)) on every pull request and before every deploy.

## Publishing

A push to `main` runs [`pages.yml`](.github/workflows/pages.yml): checks first, then the `dist/` folder is uploaded to GitHub Pages. Nothing outside `dist/` is published.

## Security

- Every page sets a strict Content Security Policy: only same-origin scripts, styles and images.
- GitHub Actions are pinned to full commit SHAs and run with least-privilege permissions; Dependabot keeps them and the linters up to date.
- CodeQL scans the JavaScript and the workflows; secret scanning with push protection is on.

To report a vulnerability, see [SECURITY.md](SECURITY.md).

## Contributing

Corrections and accessibility reports are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md). Changes are listed in [CHANGELOG.md](CHANGELOG.md).

## License

- **Code** (HTML structure, CSS, JavaScript, workflows, scripts): [MIT](LICENSE).
- **Content** (texts, career facts, portrait photo, social preview image): © 2026 Oleksandr Yukhno, all rights reserved. Please do not reuse the texts or the photo without permission.
