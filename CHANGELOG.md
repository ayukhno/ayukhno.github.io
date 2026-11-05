# Changelog

All notable changes to this website are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Social preview image with the new positioning (operational transformation · PMO · AI in processes, one accent colour); source in `tools/og/og.html`.
- Ukrainian CV page: search title, description and social preview tags.

## [2.0.0] - 2026-11-05

### Changed

- Two views: the CV is the base and the Story is its extension, with the same sections in the same order (where I can help, first 100 days, experience, AI in practice, education, skills, contact). The Brief view is gone; its old addresses redirect to the CV.
- The home page `/` is now the English CV; the English Story moved to `/story.html`. Ukrainian: `/uk-cv.html` (CV) and `/uk.html` (Story). `/cv.html`, `/brief.html`, `/uk-brief.html` and `/story/` redirect.
- New positioning: operational transformation, PMO and change management, AI in processes. "Next-generation PMO" and FlipManager removed everywhere; new meta title and description; Silpo and Ciklum without quotes.
- PDF CVs rebuilt from the new CV in both languages: two A4 pages each, larger 10pt type. Markdown versions, llms.txt and the sitemap updated; the P.S. with the cost figure removed.

### Added

- "Where I can help": four tasks from Silpo experience (P&L tools, balanced scorecard, staff productivity, system change and PMO) and AI as a new challenge ("Digital Management").
- CV sections: first 100 days, "Now: applied AI" with open projects and own systems, education, skills with personal qualities confirmed by assessments and an outside view by Claude, contact.
- Experience: PMO project portfolio, four business transformation programmes, projects with McKinsey, PwC and KPMG.
- The CV menu highlights the current section.

## [1.5.0] - 2026-11-01

### Changed

- Headings: section headings balance their lines so the last word is not left alone; "Education and professional development" fits on one line, the contact heading on two; "What I have built / with AI" breaks the same way in both languages. Stylesheet version bumped so browsers load the new styles.
- English is now the default page at `/`; Ukrainian moved to `/uk.html`. The old `/en.html` redirects to `/`, and `/story/` and `/story/uk.html` redirect to the new addresses.
- Ukrainian text proofread with Gemini paragraph by paragraph; the owner's content edits carried over to English and checked by Gemini.
- Facts: PMO office reporting to the Retail Director; PMO Hub started as the tool for DPA development; 14 major and minor skill releases; the skill also runs in Codex and Antigravity; Ernst & Young year removed.
- CV PDFs, Markdown versions and llms.txt rebuilt; long jobs may now break across pages so each PDF stays at two pages.
- README opens with a note for anyone who wants to build their own CV from this repository.
- Social preview image updated to the current wording (next-generation PMO, banking software).

### Changed

- Language pass: humanizer rules for English, a native-editor pass for Ukrainian; owner-approved rewording ("Currently in Poland", four challenges, how the tuning method was built, security as a possible task of its own, "What I have built with AI", a career-long change of view in the Experience intro, a plainer P.S.).

### Added

- "This website" case in AI in practice: a timeline (idea on Wednesday, Codex prototype, eight hours to a proofread site), about $40 of AI usage, Codex prototype, Claude build, Gemini review and translation.

### Changed

- CV files: the P.S. now says how the site and file were made and who did what.

### Added

- Downloadable CV in PDF (English and Ukrainian) in the classic HR format, with download buttons by the portrait and in the contact section.
- Markdown CVs and `llms.txt` so AI assistants and answer engines can read the CV; richer schema.org data (name variants, positions, education, languages, skills) and search descriptions.

### Added

- Offer line under the hero facts: projects and roles with ownership of the result.
- Work terms under the portrait: remote, hybrid, travel, open to relocation within Europe, working English.
- IMD Business School in education.

### Changed

- "My view of what business needs today" and "My view of the first 100 days" (no timelines; data-security readiness is assessed first).

### Changed

- "How I would start in a new role" shown as four steps in two columns; "Education and training" is its own section (05), contact moves to 06.
- Removed the line "Each one is backed by the story below."

### Changed

- "Software for banks" runs to 2002 and includes ProFIX 1999–2002; "Projects and clients" starts in 2002 with management at ProFIX.

## [1.4.0] - 2026-10-31

### Removed

- The classic version (old slogan page, diagram, its styles, script and the 2.7 MB portrait). The story CV is now the whole site.

### Added

- Ukrainian story version at `/story/uk.html` (translated with Gemini, edited by hand); language switch inside the story; the Ukrainian classic page links to it.

### Changed

- Story: first chapter is now "Electronics and programming" (1987–1996); "Software for banks" starts in 1995.
- Story: chapters show only their years, without numbers that repeated the section numbering.
- Story: the main button now sits right under the headline; LinkedIn stays as one link next to the portrait.
- Story: items in "Where I can help" start with their own line icons (eye, linked nodes, shield, four blocks); item four now covers operations, commerce, finance and IT, with Silpo's promotions, pricing, markdown and assortment projects.
- Story: "What I bring" renamed "Where I can help"; the duplicate number above its first item removed.
- Story: AI now maintains and develops the smart-home setup; TCC can use different AI models directly or through OMP; the contact call adds weighing AI costs and benefits with data security in mind.
- Story: AI projects reordered (DPA, PMO Hub, Autosound); the tuning skill and TCC shown as one project, with TCC as the app on top of the skill.
- Story: the Autosound case now explains the skill as a deterministic, multi-factor process and TCC as a multilingual, cross-platform application.
- Story: "Scaling AI" step explains the three ways to roll out AI (new solutions, personal work, a company-wide tool).

### Changed (structure)

- `/` is the Ukrainian CV and `/en.html` the English CV; `/story/` and `/story/uk.html` redirect there.

## [1.3.1] - 2026-10-31

### Changed

- Story: contact by LinkedIn only; email and phone numbers removed from the page.
- Story: Scanvaegt role marked as outstaffed from Ciklum; the smart homes run Home Assistant.

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

[Unreleased]: https://github.com/ayukhno/ayukhno.github.io/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.5.0...v2.0.0
[1.5.0]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.3.1...v1.4.0
[1.3.1]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.3.0...v1.3.1
[1.3.0]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/ayukhno/ayukhno.github.io/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/ayukhno/ayukhno.github.io/releases/tag/v1.0.0
