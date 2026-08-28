#!/usr/bin/env python3
"""
Builds profile/banner.svg -- the whole Credda org profile page.

WHY THIS SCRIPT EXISTS AT ALL
-----------------------------
The banner carries no live text. Every letterform in it is a filled PATH,
outlined from the same two families the product ships (IBM Plex Sans for the
thesis, JetBrains Mono for the instrument). GitHub renders the banner through
an <img>, and an <img>-embedded SVG may not fetch anything: no @font-face, no
Google Fonts, no @import. A `font-family` declaration would therefore be a
suggestion, and on a machine without Plex installed -- which is nearly all of
them -- the headline would silently fall back to Arial and the mono column
would lose its grid. Outlining removes the question.

Outlines are not free: they cannot be re-flowed, and a copy edit means running
this script again. That is the trade, and it is the right way round for a
banner whose entire job is one fixed sentence.

Licensing: IBM Plex Sans and JetBrains Mono are both SIL OFL 1.1, which permits
embedding. The two subset .woff2 files under tools/fonts/ came out of the web
app's own next/font build, so the profile and the site are cut from literally
the same outlines.

Usage:  python tools/build_banner.py
"""

from __future__ import annotations

import re
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(__file__).resolve().parent.parent
FONTS = Path(__file__).resolve().parent / "fonts"
OUT = ROOT / "profile" / "banner.svg"

# --------------------------------------------------------------------------
# canvas
# --------------------------------------------------------------------------
# 880 x 480. 880 is the README content column, so at full width one viewBox
# unit is one CSS pixel and every hairline lands on a whole pixel. 11:6 is
# shallow enough that a 375px phone still gets 205px of height rather than a
# postage stamp.
W, H = 880, 480

# --------------------------------------------------------------------------
# fonts
# --------------------------------------------------------------------------


class Face:
    """One weight of one family, reduced to what a renderer needs: outlines."""

    def __init__(self, path: Path, weight: float, prefix: str):
        font = TTFont(path)
        if "fvar" in font:
            font = instancer.instantiateVariableFont(font, {"wght": weight})
        self.font = font
        self.upem = font["head"].unitsPerEm
        self.cmap = font.getBestCmap()
        self.hmtx = font["hmtx"]
        self.glyphset = font.getGlyphSet()
        self.prefix = prefix
        self.used: dict[str, str] = {}  # char -> path id

    def gname(self, ch: str) -> str:
        cp = ord(ch)
        if cp not in self.cmap:
            raise KeyError(f"{self.prefix}: no glyph for {ch!r}")
        return self.cmap[cp]

    def advance(self, ch: str) -> float:
        return self.hmtx[self.gname(ch)][0]

    def path_id(self, ch: str) -> str | None:
        """Register a glyph and return its <defs> id, or None if it is blank."""
        if ch in self.used:
            return self.used[ch]
        gname = self.gname(ch)
        pen = SVGPathPen(self.glyphset, ntos=lambda v: _num(v))
        self.glyphset[gname].draw(pen)
        d = pen.getCommands()
        if not d.strip():
            self.used[ch] = ""
            return ""
        gid = f"{self.prefix}{len(self.used)}"
        self.used[ch] = gid
        self._defs[gid] = d
        return gid

    _defs: dict[str, str] = {}


def _num(v: float) -> str:
    """Round to whole font units. At 1000upm that is ~0.04px at our sizes."""
    return str(int(round(v)))


Face._defs = {}
DEFS: dict[str, str] = {}
Face._defs = DEFS

SANS600 = Face(FONTS / "plexsans.woff2", 600, "s")
MONO400 = Face(FONTS / "jbmono.woff2", 400, "m")
MONO600 = Face(FONTS / "jbmono.woff2", 600, "b")


# --------------------------------------------------------------------------
# text -> paths
# --------------------------------------------------------------------------

Run = tuple[Face, str, str]  # face, string, css class


def measure(face: Face, text: str, size: float, track: float = 0.0) -> float:
    scale = size / face.upem
    w = sum(face.advance(c) for c in text) * scale
    return w + track * max(len(text) - 1, 0)


def measure_runs(runs: list[Run], size: float, track: float = 0.0) -> float:
    return sum(measure(f, t, size, track) for f, t, _ in runs)


def draw(
    runs: list[Run],
    x: float,
    baseline: float,
    size: float,
    track: float = 0.0,
    anchor: str = "start",
    wrap: str = "",
) -> str:
    """Emit one line of text as <use> references into a shared glyph table.

    Glyph outlines live once in <defs> at their native em size; each line is a
    <g> that translates to the baseline and flips y (font space is y-up, SVG is
    y-down). That keeps a 400-character banner in the low tens of kilobytes
    instead of inlining every outline at every size.
    """
    total = measure_runs(runs, size, track)
    if anchor == "end":
        x -= total
    elif anchor == "middle":
        x -= total / 2

    scale = size / SANS600.upem  # all three faces are 1000upm; asserted below
    parts: list[str] = []
    pen_x = 0.0  # in font units, relative to the group origin
    for face, text, cls in runs:
        assert face.upem == 1000
        for ch in text:
            gid = face.path_id(ch)
            if gid:
                cx = _num(pen_x)
                href = f'#{gid}'
                attrs = f' class="{cls}"' if cls else ""
                parts.append(
                    f'<use href="{href}" xlink:href="{href}" x="{cx}"{attrs}/>'
                )
            pen_x += face.advance(ch) + (track / scale)

    # The positioning transform lives on an INNER group. Any animated class
    # goes on an outer wrapper, because a CSS `transform` property replaces the
    # SVG transform= presentation attribute outright rather than composing with
    # it -- animating the positioned group directly would fling the line off the
    # card at the first keyframe.
    inner = (
        f'<g transform="translate({_n(x)} {_n(baseline)}) '
        f'scale({_n(scale, 5)} {_n(-scale, 5)})">' + "".join(parts) + "</g>"
    )
    return f"<g {wrap}>{inner}</g>" if wrap else inner


def _n(v: float, places: int = 2) -> str:
    s = f"{v:.{places}f}".rstrip("0").rstrip(".")
    return s if s not in ("", "-0") else "0"


def t(text: str, cls: str = "", face: Face = MONO400) -> Run:
    return (face, text, cls)


# --------------------------------------------------------------------------
# copy
# --------------------------------------------------------------------------
# Nothing here is a metric, a count or a benchmark score. Those move, and a
# banner is outlined paths that only change when somebody regenerates them.
#
# Nothing here dates either. Two versions of this file have now gone stale for
# the same reason, and the second is the instructive one.
#
# The first ended on "it does not write the fix" -- a build order written as
# though it were the product (ADR 0018).
#
# The second was worse, because nothing in it was false. It was headed
# AUTONOMOUS BUG REPRODUCTION, its command was `reproduce`, its four checks all
# described establishing that a failure is real, and its panel settled on
# REPRODUCED, with evidence attached, not a fix. Every one of those was an
# accurate description of what shipped, and together they sold the wrong
# product: reproduction is the part of the job a customer did not want done for
# them. They wanted the fix.
#
# So the copy below describes the product -- find the security risk or the bug,
# write the patch, prove it, open the pull request -- and STATUS lives in the
# alt text, which is one line to edit and needs no regeneration. That split is
# the whole reason this banner carries no dated claim.
#
# The closing line is the one invariant that holds in every version of Credda
# there will ever be, and it is a boundary rather than a boast: Credda proposes,
# and a person merges.

HEAD_1 = "Finds it. Fixes it."
HEAD_2 = "Proves it."

STEPS = [
    "reproduce the failure",
    "find what actually caused it",
    "write the patch",
    "prove it with a test",
]

# --------------------------------------------------------------------------
# geometry
# --------------------------------------------------------------------------
PAD = 32
RIGHT = W - PAD

HEAD_RULE_Y = 56
HEAD_SIZE = 42
HEAD_BASE_1 = 134
HEAD_BASE_2 = 184
MID_RULE_Y = 216

CMD_BASE = 256
STEP_0 = 296
STEP_DY = 32
BOX = 11  # side of the check box
LABEL_X = 62

DIV_X = 498
PANEL = (520, 234, 328, 168)  # x, y, w, h
FOOT_RULE_Y = 428
FOOT_BASE = 456

STEP_DELAY = 0.30  # seconds between one check resolving and the next


def build() -> str:
    body: list[str] = []

    # ---------------------------------------------------------------- header
    body.append(
        f'<rect class="mark" x="{PAD}" y="27" width="9" height="9"/>'
    )
    body.append(draw([t("CREDDA", "fg", MONO600)], PAD + 20, 36, 14, track=2.4))
    body.append(
        draw(
            [t("SECURITY RISKS AND BUGS, FIXED", "dim")],
            RIGHT,
            36,
            11.5,
            track=1.8,
            anchor="end",
        )
    )
    body.append(f'<path class="rule" d="M1 {HEAD_RULE_Y}.5H{W - 1}"/>')

    # -------------------------------------------------------------- headline
    # Two flat colours and no gradient anywhere: the turn between the lines is
    # carried by value alone, which is the only emphasis a drafting sheet has.
    body.append(
        draw([t(HEAD_1, "head-a", SANS600)], PAD, HEAD_BASE_1, HEAD_SIZE,
             wrap='class="a-h1"')
    )
    body.append(
        draw([t(HEAD_2, "head-b", SANS600)], PAD, HEAD_BASE_2, HEAD_SIZE,
             wrap='class="a-h2"')
    )
    body.append(f'<path class="rule" d="M1 {MID_RULE_Y}.5H{W - 1}"/>')

    # -------------------------------------------------- the run: command line
    cmd_runs = [
        t("$ ", "dim"),
        t("credda fix", "fg", MONO600),
        t("  issue-1284", "mid"),
    ]
    body.append(draw(cmd_runs, PAD, CMD_BASE, 15.5, wrap='class="a-cmd"'))

    cmd_w = measure_runs(cmd_runs, 15.5)
    # The type-on is a cover panel painted in the card colour that retracts to
    # the right, carrying a caret at its leading edge. Only translateX is
    # animated -- no geometry property, no clip-path, nothing a renderer might
    # decline -- so the effect degrades to "already typed" rather than to
    # "permanently blanked" if the animation never runs.
    body.append(
        f'<g class="a-type" style="--tx:{_n(cmd_w + 10)}px">'
        f'<rect class="cover" x="{PAD - 2}" y="240" '
        f'width="{_n(cmd_w + 6)}" height="22"/>'
        f'<rect class="caret" x="{PAD - 2}" y="241" width="8" height="19"/></g>'
    )

    # ------------------------------------------------------ the run: checks
    for i, label in enumerate(STEPS):
        y = STEP_0 + i * STEP_DY
        delay = 2.13 + i * STEP_DELAY
        g = f'<g class="step" style="--d:{delay:.2f}s">'
        # The empty box is drawn once and stays; the tick lands inside it.
        g += (
            f'<rect class="box" x="{PAD + 0.5}" y="{_n(y - BOX + 1.5)}" '
            f'width="{BOX}" height="{BOX}" rx="2"/>'
        )
        g += (
            f'<path class="tick" d="M{PAD + 3} {_n(y - 4.6)}'
            f'l{_n(2.6)} {_n(2.6)}l{_n(5.4)} {_n(-6.2)}"/>'
        )
        g += draw([t(label, "mid")], LABEL_X, y, 15)
        g += "</g>"
        body.append(g)

    # The wavefront: one hairline sweeping down the check column, arriving at
    # each box a beat before that box resolves. It is the only moving mark on
    # the sheet and it leaves nothing behind.
    body.append(
        f'<rect class="wave" x="{PAD}" y="{STEP_0 - 14}" '
        f'width="{DIV_X - PAD - 28}" height="1"/>'
    )

    body.append(f'<path class="rule" d="M{DIV_X}.5 236V{PANEL[1] + PANEL[3] - 4}"/>')

    # ---------------------------------------------------------------- verdict
    px, py, pw, ph = PANEL
    body.append(f'<g class="a-panel">')
    body.append(
        f'<rect class="v-bg" x="{px}" y="{py}" width="{pw}" height="{ph}" rx="8"/>'
    )
    # The border draws itself round the rect in one pass: the verdict closing.
    body.append(
        f'<rect class="v-edge" x="{px}.5" y="{py}.5" width="{pw - 1}" '
        f'height="{ph - 1}" rx="7.5"/>'
    )
    body.append(draw([t("RESULT", "dim")], px + 28, py + 40, 11, track=2.2))
    body.append(
        draw([t("PULL REQUEST", "verdict", MONO600)], px + 28, py + 84, 25,
             wrap='class="a-word"')
    )
    body.append(
        f'<path class="v-rule" d="M{px + 28} {py + 106}.5H{px + pw - 28}"/>'
    )
    body.append(
        draw([t("patch, and the test that proves it", "mid")], px + 28, py + 134, 12,
             wrap='class="a-word"')
    )
    body.append("</g>")

    # ----------------------------------------------------------------- footer
    body.append(f'<path class="rule" d="M1 {FOOT_RULE_Y}.5H{W - 1}"/>')
    body.append(draw([t("credda.io", "dim")], PAD, FOOT_BASE, 12, track=0.6))
    body.append(
        draw(
            [t("Credda proposes. A person merges.", "dim")],
            RIGHT,
            FOOT_BASE,
            12,
            track=0.6,
            anchor="end",
        )
    )

    defs = "".join(
        f'<path id="{gid}" d="{d}"/>' for gid, d in DEFS.items()
    )

    # SVG is XML, and <style> in XML is NOT a CDATA section the way it is in
    # HTML: a "<" anywhere inside it -- including inside a CSS comment -- is
    # parsed as the start of a tag and the whole document fails to load. The
    # rationale comments therefore live in THIS file and are stripped on the way
    # out, which also keeps the shipped asset lean.
    css = re.sub(r"/\*.*?\*/", "", CSS, flags=re.S)
    css = re.sub(r"\n\s*\n+", "\n", css).strip()

    svg = TEMPLATE.format(
        w=W, h=H, defs=defs, body="".join(body), css=css
    )
    return svg


CSS = """
/*
 * No scripting, no @font-face, no @import, no external URL of any kind. An
 * SVG embedded through an img element is loaded under a sandbox that would
 * refuse all of them, and GitHub strips executable content from SVG besides.
 * Everything below is inert paint.
 */
:root {
  --bg: #0A0A0A;        /* --w-surface-base   */
  --panel: #1A1A1A;     /* --w-surface-overlay */
  --edge: #333333;      /* --w-border-default */
  --hair: #212121;      /* --w-border-subtle  */
  --strong: #454545;    /* --w-border-strong  */
  --fg: #F2F2F2;        /* --w-text-primary   */
  --mid: #A3A3A3;       /* --w-text-secondary */
  --dim: #848484;       /* --w-text-tertiary  */
  --brand: #787878;     /* --w-brand-500      */
  --v-fg: #3FCF8E;      /* --w-state-verified-fg     */
  --v-bg: #091E15;      /* --w-state-verified-bg     */
  --v-edge: #1B4D35;    /* --w-state-verified-border */
}

/*
 * BOTH GITHUB THEMES, AND WHY THE CARD IS OPAQUE.
 *
 * prefers-color-scheme inside an <img>-embedded SVG reads the OS setting, not
 * the host page's theme, and Safari does not honour it in that position at
 * all. So a banner that trusted the media query alone would be wrong for any
 * reader whose GitHub theme differs from their OS, and wrong for every Safari
 * reader. This card therefore paints its OWN ground edge to edge and never
 * borrows the page's: it cannot go invisible on either theme, in any browser,
 * because it is never transparent. The media query below is the courtesy on
 * top -- where it is honoured the card sits in the same key as the page, and
 * where it is not the card is still a framed, fully legible instrument.
 */
@media (prefers-color-scheme: light) {
  :root {
    --bg: #FBFBFB;
    --panel: #FFFFFF;
    --edge: #E1E1E1;
    --hair: #EAEAEA;
    --strong: #C6C6C6;
    --fg: #0B0B0B;
    --mid: #5A5A5A;
    --dim: #6C6C6C;
    --brand: #787878;
    --v-fg: #96218C;
    --v-bg: #FCF0FA;
    --v-edge: #EFC8E9;
  }
}

.card { fill: var(--bg); stroke: var(--edge); }
.rule { stroke: var(--hair); stroke-width: 1; fill: none; }
.mark { fill: var(--brand); }
.fg { fill: var(--fg); }
.mid { fill: var(--mid); }
.dim { fill: var(--dim); }
.head-a { fill: var(--mid); }
.head-b { fill: var(--fg); }
.cover { fill: var(--bg); }
.caret { fill: var(--brand); }
.box { fill: none; stroke: var(--strong); stroke-width: 1; }
.tick { fill: none; stroke: var(--mid); stroke-width: 1.6;
        stroke-linecap: round; stroke-linejoin: miter; }
.wave { fill: var(--brand); }
.v-bg { fill: var(--v-bg); }
.v-edge { fill: none; stroke: var(--v-edge); stroke-width: 1; }
.v-rule { stroke: var(--v-edge); stroke-width: 1; fill: none; }
.verdict { fill: var(--v-fg); }

/*
 * MOTION
 *
 * One pass, ~4.4s, then it holds forever on the frame that carries the
 * message. Nothing loops, nothing strobes, nothing pulses at a reader who has
 * already got the point -- a profile banner is read for four seconds and then
 * sat next to for minutes.
 *
 * Every rule below is written so that the ELEMENT'S RESTING STYLE IS ALREADY
 * THE FINAL FRAME, and the keyframes only describe where it comes FROM. Kill
 * the animations and the banner is simply finished. That is what makes the
 * reduced-motion block at the bottom a one-liner rather than a second design.
 */
.a-h1, .a-h2, .a-cmd, .a-panel { animation: rise .5s ease-out both; }
.a-h1 { animation-delay: .10s; }
.a-h2 { animation-delay: .30s; }
.a-cmd { animation-delay: .70s; animation-duration: .01s; }

@keyframes rise {
  from { opacity: 0; transform: translateY(7px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* The cover retracts across the command, then leaves. */
/*
 * --tx is the exact width of the command line, written onto the element by the
 * generator. It must NOT be a percentage: transform-box defaults to view-box
 * for CSS transforms on SVG content, so translateX(120%) resolves against the
 * 880-unit viewBox rather than the 290-unit cover, and the panel scythes across
 * the whole card and through the verdict.
 */
.a-type { transform: translateX(var(--tx)); opacity: 0; }
.a-type { animation: type 1.13s steps(20, end) .72s both; }
@keyframes type {
  0%   { transform: translateX(0); opacity: 1; }
  86%  { transform: translateX(var(--tx)); opacity: 1; }
  100% { transform: translateX(var(--tx)); opacity: 0; }
}

/* The wavefront crosses the four boxes once and is gone. */
.wave { opacity: 0; }
.wave { animation: sweep 1.05s linear 1.95s both; }
@keyframes sweep {
  0%   { opacity: 0;   transform: translateY(0); }
  12%  { opacity: .55; }
  85%  { opacity: .55; transform: translateY(112px); }
  100% { opacity: 0;   transform: translateY(112px); }
}

/* Each check resolves just after the wavefront reaches it. */
.step { animation: land .34s ease-out var(--d) both; }
@keyframes land {
  from { opacity: 0; }
  to   { opacity: 1; }
}
.step .tick { stroke-dasharray: 13; stroke-dashoffset: 0;
              animation: mark .22s linear var(--d) both; }
@keyframes mark {
  from { stroke-dashoffset: 13; }
  to   { stroke-dashoffset: 0; }
}

/* The verdict lands last and its border closes around it. */
.a-panel { animation-delay: 3.35s; animation-duration: .45s; }
.v-edge { stroke-dasharray: 992; stroke-dashoffset: 0;
          animation: close .9s cubic-bezier(.4,0,.2,1) 3.5s both; }
@keyframes close {
  from { stroke-dashoffset: 992; }
  to   { stroke-dashoffset: 0; }
}
.a-word { animation: rise .45s ease-out 3.85s both; }

@media (prefers-reduced-motion: reduce) {
  /*
   * Land on the final frame immediately. Because every resting style above is
   * already the settled one, switching the animations off is the whole fix --
   * except for the type-on cover, whose resting position must be stated here
   * since its job is to be gone.
   */
  .a-h1, .a-h2, .a-cmd, .a-panel, .a-type, .wave, .step, .step .tick, .v-edge,
  .a-word { animation: none !important; }
  .a-type, .wave { opacity: 0 !important; }
}
"""

TEMPLATE = (
    '<svg xmlns="http://www.w3.org/2000/svg" '
    'xmlns:xlink="http://www.w3.org/1999/xlink" '
    'viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
    'role="img" aria-labelledby="t d" fill="none">'
    "<title id=\"t\">Credda &#8212; finds it, fixes it, proves it.</title>"
    "<desc id=\"d\">A terminal-style panel. A command, credda fix, runs against "
    "an issue; four checks resolve in turn &#8212; reproduce the failure, find "
    "what actually caused it, write the patch, prove it with a test &#8212; and "
    "a result panel settles on PULL REQUEST, carrying the patch and the test "
    "that proves it.</desc>"
    "<style>{css}</style>"
    "<defs>{defs}</defs>"
    '<rect class="card" x=".5" y=".5" width="{w1}" height="{h1}" rx="12"/>'
    "{body}"
    "</svg>"
).replace("{w1}", str(W - 1)).replace("{h1}", str(H - 1))


if __name__ == "__main__":
    out = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(out, encoding="utf-8")
    print(f"{OUT}  {len(out.encode('utf-8')) / 1024:.1f} KB")
    # A malformed SVG does not degrade, it fails to paint at all, and an <img>
    # gives no console error to notice it by. Parse it here or find out on the
    # org page.
    import xml.etree.ElementTree as ET

    ET.fromstring(out)

    low = out.lower()
    assert "<script" not in low and "javascript:" not in low
    assert "@import" not in low and "@font-face" not in low
    stray = [m for m in re.findall(r'https?://[^"\s]+', out)
             if not m.startswith("http://www.w3.org")]
    assert not stray, stray
    assert "<title" in low and "prefers-reduced-motion" in low
    print("checks: well-formed XML, no script, no font-face/import, "
          "no external URL, has title + reduced-motion")
