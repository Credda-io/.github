# Brand artwork for the org profile

Four files, every one of them COPIED byte for byte out of the Credda brand
folder. Nothing here is drawn, resized, recolored or composited in this
repository, and `profile/README.md` is the only thing that reads them.

| File | Source | Used by |
| --- | --- | --- |
| `creddaseallockuplighttransparent.png` | `brand-seal/`, generated | The header, light background |
| `creddaseallockupdarktransparent.png` | `brand-seal/`, generated | The header, dark background |
| `creddasealmarklighttransparent.png` | `brand-seal/`, generated | The footer mark, light background |
| `creddasealmarkdarktransparent.png` | `brand-seal/`, generated | The footer mark, dark background |

The light pair is brand orange `#C2410C` and the dark pair is brand blue
`#5B9BFF`. The accent is two colors by design, which is why there are two of
every file and why a blue mark is not a mistake.

## Rules

**Never hand-edit any of these.** All four are generated output. To change one,
change the brand folder and copy the result across again. `build-seal.mjs
--check` rebuilds every file in memory and reports drift without writing
anything, so a file that has been touched by hand is detectable.

**Copy the pixels, do not composite them.** Pasting an RGBA image using itself
as a mask blends every partially transparent pixel toward the empty canvas, so
each antialiased edge darkens. The artwork looks identical and is not. Verify a
copy by hashing the file, not by looking at it.

**Absolute `raw.githubusercontent.com` URLs, not relative paths.** An org
profile README is rendered on the organization page, which is not this
repository, so a relative path resolves against the wrong root and shows a
broken image.

**These four files are load bearing outside this repository.** The members-only
profile in `Credda-io/.github-private` hotlinks them from this repo on `main`,
because a private repo's raw URLs need a token and would render for nobody.
Renaming, moving or deleting one of these files breaks that page. Land a change
here first, then the private one.

## The mark

The lockup is `credda` set in Inter, then the seal: a thick ring with five short
notches cut into its outer edge, in a single run down the lower left, with the
rest of the rim left smooth.

That is the product in one shape. The record is append-only, every confirmed
outcome is a notch cut into the same seal, and the one clean gap is where the
next one goes.

The asymmetry is the whole idea and it is not a drafting slip. Space the notches
evenly and the ring reads as machinery. A run of tally marks down one side with
an unfinished rim reads as a record somebody has been keeping. Do not
redistribute the notches, do not close the run, and never describe the seal as a
cog or a gear.

There is one lockup, not a family. The wordmark comes first and the seal
follows, with no rule between them, because a rule was only ever there to
separate a mark from a logotype that opened with a competing round shape. The
wordmark now opens on a lowercase `c` in Inter and closes on `a`, so the seal
sits after the word as a terminal, and nothing needs separating.

Where a slot is square rather than wide, use the mark on its own. That is what
the two `creddasealmark*` files are for.

## What is NOT here

**The three-lobe mark and the long lockup.** They were the profile's artwork for
one day, 2026-08-10 to 2026-08-11, and the seal replaced both. Every file that
carried them was removed from this folder in the same commit that added these
four. Nothing in this repository should carry the wordmark with the large round
`C`.

**The retired standalone C.** Retired earlier, on 2026-08-10, and it should
appear on no Credda surface. This folder never carried it.

Filenames are not evidence here. Two of the files this folder just lost had `c`
in the name and contained the three-lobe mark rather than the letter, and a
`profile/logo-c.png` deleted in an earlier cleanup turned out to hold the
current mark of its day. If you are not sure what a file contains, open it.
