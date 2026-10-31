# Security policy

This repository publishes a static personal website to GitHub Pages. It has no server, no forms, no cookies, no analytics and no third-party scripts. Every page ships a strict Content Security Policy that allows only same-origin scripts, styles and images.

## Supported versions

Only the live site at <https://ayukhno.github.io/> and the `main` branch are supported. Older tags are not patched.

## Reporting a vulnerability

Please report privately. Do not open a public issue.

1. Open [a private security advisory](https://github.com/ayukhno/ayukhno.github.io/security/advisories/new) in this repository.
2. Describe the issue, the affected page or file, and the steps to reproduce it.

You can expect a first reply within 5 working days. Confirmed issues are fixed on `main` and published by the deploy workflow; the fix is noted in [CHANGELOG.md](CHANGELOG.md).

The same contact is published in machine-readable form at [`/.well-known/security.txt`](https://ayukhno.github.io/.well-known/security.txt).

## In scope

- Cross-site scripting or content injection on any page of the site
- Weaknesses in the Content Security Policy or other page metadata
- Supply-chain risks in the GitHub Actions workflows or development dependencies

## Out of scope

- Missing HTTP response headers that GitHub Pages does not let site owners set (for example `X-Frame-Options`)
- Reports produced only by automated scanners without a working proof of concept
- Social engineering or physical attacks
