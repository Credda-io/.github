# Vendored fonts

`banner.svg` contains no font files and no `@font-face`. Its letterforms are
outlined paths, cut from these two faces at build time by
`tools/build_banner.py`. They are here so the build is reproducible.

Both are licensed under the SIL Open Font License 1.1, which permits
redistribution. The licence requires this notice to travel with them.

  plexsans.woff2   IBM Plex Sans
                   Copyright (c) 2017 IBM Corp.
                   https://github.com/IBM/plex
                   SIL OFL 1.1

  jbmono.woff2     JetBrains Mono
                   Copyright (c) 2020 The JetBrains Mono Project Authors
                   https://github.com/JetBrains/JetBrainsMono
                   SIL OFL 1.1

Full licence text: https://openfontlicense.org

These are the same faces the website loads, which is why the profile and
codereef.app are recognisably set in the same type. The repository's own
LICENSE (Apache-2.0) covers the code here, not these files.
