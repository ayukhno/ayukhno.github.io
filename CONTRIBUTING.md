# Contributing

This is a personal website, so the text describes one person's career and is edited only by its owner. Issues, pull requests and comments from outside the repository are turned off.

## How to report a problem

- **Corrections and accessibility problems**: a broken link, a typo, a layout problem on your device, anything hard to use with a screen reader, keyboard or zoom. Write to me on [LinkedIn](https://www.linkedin.com/in/oleksandryukhno/).
- **Security problems**: follow [SECURITY.md](SECURITY.md).

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
