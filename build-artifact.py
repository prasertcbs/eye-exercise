#!/usr/bin/env python3
"""Build artifact.html from index.html.

The Claude Artifact host supplies its own <!doctype>/<html>/<head>/<body> wrapper and
stamps the viewer's theme on the root element, so the published build is index.html with
the document scaffolding removed. Everything else -- markup, styles, script -- is shared,
which keeps the standalone file and the published page from drifting apart.

Usage:  python build-artifact.py
"""

import io
import re
import sys

SRC = "index.html"
DST = "artifact.html"

# The host owns the page chrome, so an in-page skip-link has nothing to skip to.
SKIP_LINK = '<a class="skip" href="#main" data-i18n="skip">Skip to content</a>\n\n'

# Dropped: the "— evidence-based routines" tail. The gallery shows the publish
# description under the title, so the title itself stays a bare product name.
TITLE = "<title>Eye Exercise Coach</title>"


def grab(pattern, text, what):
    m = re.search(pattern, text, re.S)
    if not m:
        sys.exit(f"build-artifact: could not find {what} in {SRC}")
    return m.group(len(m.groups()))


def main():
    src = io.open(SRC, encoding="utf-8").read()

    style = grab(r"<style>.*?</style>", src, "the <style> block")
    early = grab(r"<script>\n  /\* Set theme/lang.*?</script>", src, "the early theme script")
    body = grab(r"<body>\n(.*)\n</body>", src, "the <body> contents")

    out = "\n".join([TITLE, style, early, body.replace(SKIP_LINK, "")]) + "\n"

    # The wrapper must not be duplicated, or the page ends up with nested documents.
    leaked = re.findall(r"</?\s*(?:html|head|body|meta|!doctype)\b[^>]*>", out, re.I)
    if leaked:
        sys.exit(f"build-artifact: document wrapper leaked into the build: {leaked}")
    if not out.startswith("<title>"):
        sys.exit("build-artifact: build must open with <title> so the artifact is named")
    if out.count("<script>") != out.count("</script>"):
        sys.exit("build-artifact: unbalanced <script> tags")

    io.open(DST, "w", encoding="utf-8").write(out)
    print(f"{DST}: {len(out):,} chars")


if __name__ == "__main__":
    main()
