# Brand artwork for the org profile

Four files, every one of them COPIED byte for byte out of the Credda brand
folder at `core/packages/design/brand/`. Nothing here is drawn, resized,
recolored or composited in this repository, and `profile/README.md` is the only
thing that reads them.

| File | Source | Used by |
| --- | --- | --- |
| `credda-lockup-black.png` | `core/packages/design/brand/` | The header, light background |
| `credda-lockup-white.png` | `core/packages/design/brand/` | The header, dark background |
| `credda-mark-black.png` | `core/packages/design/brand/` | The footer mark, light background |
| `credda-mark-white.png` | `core/packages/design/brand/` | The footer mark, dark background |

**The identity is achromatic.** Black artwork on light, white artwork on dark,
and nothing in between. There is no accent colour in the mark, which is why the
pairs differ only in ink and why a white lockup is not a mistake. The orange
`#C2410C` and blue `#5B9BFF` seal artwork that lived here until 2026-08-27
belonged to the retired trust product and was deleted in the same commit that
added these four. Neither colour should appear on any Credda surface.

## Rules

**Never hand-edit any of these.** All four are generated output. To change one,
change the brand folder in `core/packages/design/brand/` and copy the result
across again. Verify a copy by hashing both files with `shasum -a 256` and
comparing, not by looking at them.

**Copy the pixels, do not composite them.** Pasting an RGBA image using itself
as a mask blends every partially transparent pixel toward the empty canvas, so
each antialiased edge darkens. The artwork looks identical and is not.

**Absolute `raw.githubusercontent.com` URLs, not relative paths.** An org
profile README is rendered on the organization page, which is not this
repository, so a relative path resolves against the wrong root and shows a
broken image.

**These files are load bearing outside this repository.** The members-only
profile in `Credda-io/.github-private` hotlinks this folder on `main`, because a
private repo's raw URLs need a token and would render for nobody. The four
filenames changed on 2026-08-27, so **every hotlink in `.github-private` that
still points at a `creddaseal*` name is broken until it is updated.** Land the
change here first, then the private one.

## What is NOT here

**The seal lockup and seal mark.** `creddaseallockup{light,dark}transparent.png`
and `creddasealmark{light,dark}transparent.png` were the profile's artwork until
2026-08-27. They carried the notched ring that stood for an append-only record
of confirmed outcomes — the retired product — and they are gone. Nothing in this
repository should carry that seal.

**The three-lobe mark, the long lockup, and the standalone C.** Retired earlier,
in August 2026, and they should appear on no Credda surface.

Filenames are not evidence here. Files in this folder's history have carried
artwork their names did not describe. If you are not sure what a file contains,
open it.
