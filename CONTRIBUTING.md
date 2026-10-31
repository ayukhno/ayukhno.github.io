# Contributing

This is a personal website, so the text describes one person's career and is edited only by its owner. Help is still welcome in a few forms.

## What you can send

- **Corrections**: a broken link, a typo, a layout problem on your device. Use the [content correction](https://github.com/ayukhno/ayukhno.github.io/issues/new?template=content_correction.yml) or [bug report](https://github.com/ayukhno/ayukhno.github.io/issues/new?template=bug_report.yml) form.
- **Accessibility problems**: anything that is hard to use with a screen reader, keyboard or zoom. These get priority.
- **Small code fixes**: a pull request is fine for HTML, CSS, JavaScript or workflow fixes. Please open an issue first for anything larger.

Security problems go through [SECURITY.md](SECURITY.md), not through issues.

## Local setup

You need Node.js (see [`.nvmrc`](.nvmrc)).

```sh
npm ci          # install the linters (the site itself has no dependencies)
npm start       # preview at http://127.0.0.1:4173
npm test        # JavaScript syntax, HTML validation, CSS lint
```

## Rules for changes

- Keep the site dependency-free at runtime: no external scripts, fonts, trackers or CDNs. The Content Security Policy in each page blocks them anyway.
- Keep colours as tokens at the top of a stylesheet; no raw colour values further down.
- Check every page at a phone width (360–390 px) and on a desktop (1440 px), in light and dark mode.
- `npm test` must pass. CI runs the same checks plus a link check.
- Write commit messages in the imperative mood ("Fix…", "Add…") and describe the user-visible change.

By contributing you agree that your code is released under the [MIT License](LICENSE) and that you follow the [Code of Conduct](CODE_OF_CONDUCT.md).
