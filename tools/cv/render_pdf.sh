#!/usr/bin/env sh
# Renders tools/cv/out/print-<lang>.html to dist/cv/*.pdf with the gstack headless browser.
set -eu
cd "$(dirname "$0")/../.."
B="${BROWSE_BIN:-$HOME/.claude/skills/gstack/browse/dist/browse}"
for pair in "en:EN" "uk:UA"; do
  lang=${pair%%:*}; tag=${pair##*:}
  "$B" goto "file://$PWD/tools/cv/out/print-$lang.html" >/dev/null
  "$B" pdf "$PWD/dist/cv/Oleksandr-Yukhno-CV-$tag.pdf" --format a4 --prefer-css-page-size --print-background --tagged --outline >/dev/null
  echo "dist/cv/Oleksandr-Yukhno-CV-$tag.pdf"
done
