# Changelog

All notable changes to this website are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.3.0] - 2026-10-31

### Added

- Repository standards: MIT license for code, security policy, contributing guide, code of conduct, issue and pull request templates, code owners, EditorConfig.
- CI workflow with JavaScript syntax check, HTML validation, CSS lint and link check; the deploy workflow now runs these checks first.
- CodeQL code scanning and Dependabot updates for GitHub Actions and npm.
- Content Security Policy and referrer policy on every page.
- Canonical URLs, language alternates, Open Graph and Twitter cards with a social preview image, and schema.org `Person` data.
- `robots.txt`, `sitemap.xml`, `/.well-known/security.txt` and a 404 page.

### Changed

- Story, chapter 01: smart homes (house and apartment) on a Raspberry Pi server, managed remotely.
- Story: contacts next to the portrait and in the contact section (email, Polish phone, messengers).
- Story: banking years (Escape, Avan, Bank Ukraina, ProFIX) grouped as "Software for banks"; Ciklum growth from about 50 to 250 people; Scanvaegt industrial plant projects.
- Story: PMO Hub added as a case; DPA described as an assistant for work and life; next-generation PMO in "What I bring" and the contact call; four-step "How I would start".
- Story: hero facts now say which company each number belongs to.
- GitHub Actions pinned to full commit SHAs with least-privilege permissions.
- Classic stylesheet normalised by the CSS linter (modern colour notation, quoted URLs); no visual change.

### Fixed

- The classic pages' language switch kept the section anchor again (it had started to pick up the Story button).
- Raw `&` characters and an invalid `aria-label` on the classic pages.

## [1.2.0] - 2026-10-31

### Added

- Story version of the CV at `/story/` (English): what I bring, the career story, AI projects with links, first steps.
- **Story** button next to the language switch on both classic pages.
- FlipManager and its four products in the story's chapter 05.

### Changed

- The local preview server serves `index.html` for directory URLs, like GitHub Pages.

## [1.1.0] - 2026-10-31

### Added

- Ukrainian version as the default page, English at `/en.html`, with a language switch.

### Changed

- English copy polished; location updated to Poland.

## [1.0.0] - 2026-10-31

### Added

- First public version of the personal website, deployed to GitHub Pages.

[Unreleased]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/ayukhno/ayukhno.github.io/releases/tag/v1.0.0
