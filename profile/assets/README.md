# Brand artwork for the org profile

Six files, every one of them COPIED byte for byte out of the Credda brand
folder. Nothing here is drawn, resized, recolored or composited in this
repository, and `profile/README.md` is the only thing that reads them.

| File | Source | Used by |
| --- | --- | --- |
| `creddalockuplonglighttransparent.png` | `collateral/`, generated | The header, light background |
| `creddalockuplongdarktransparent.png` | `collateral/`, generated | The header, dark background |
| `creddalightctransparent.png` | a master | The footer rule, light background |
| `creddadarkctransparent.png` | a master | The footer rule, dark background |
| `creddalockuplighttransparent.png` | `collateral/`, generated | Nothing yet. See below. |
| `creddalockupdarktransparent.png` | `collateral/`, generated | Nothing yet. See below. |

## Rules

**Never hand-edit any of these.** Four are generated output and two are masters.
To change one, change the brand folder and copy the result across again.
`build-collateral.mjs --check` fails if a generated file has drifted from what
the generator produces.

**Copy the pixels, do not composite them.** Pasting an RGBA image using itself
as a mask blends every partially transparent pixel toward the empty canvas, so
each antialiased edge darkens. The artwork looks identical and is not. Verify a
copy by hashing the file, not by looking at it.

**Absolute `raw.githubusercontent.com` URLs, not relative paths.** An org
profile README is rendered on the organization page, which is not this
repository, so a relative path resolves against the wrong root and shows a
broken image.

## Which lockup goes where

The header carries the LONG lockup: the wordmark first, then the three-lobe mark
after it, no rule between them. That is the form for a wide horizontal slot,
which a profile header is, and it is what the app, the boot splash and all eight
generated banners already carry.

The two `creddalockup*` files without `long` in the name are the STANDARD
lockup, which puts the mark first and separates it from the wordmark with a
hairline rule. They are deliberately kept and deliberately unused: the standard
lockup was not retired, and it stays the right choice for a square-ish slot the
long form cannot fill. If a future edit needs one, it is here rather than
reachable only by another trip to the brand folder. Do not substitute it for the
long lockup in the header.

## What is NOT here

The retired standalone C. It was replaced by the three-lobe mark on 2026-08-10
and it should appear on no Credda surface. This folder never carried it; the
`profile/logo-c.png` that did was deleted along with `profile/logofull.png` and
the pre-crop-pipeline `profile/logo-wordmark.png`, all three of which were
leftovers from before the brand folder had a build script.
