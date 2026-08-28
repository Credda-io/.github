<!--
  THE CREDDA ORGANISATION PROFILE.

  GitHub renders this one file at the top of https://github.com/Credda-io. It is
  deliberately a single image and nothing else: every word a visitor reads is
  inside banner.svg.

  WHAT THIS REPLACED, AND WHY. This page was a long README describing a 0-100
  reliability score -- the retired product. Before that, the same banner under
  the CodeReef name was headed AUTONOMOUS BUG REPRODUCTION, and that is the more
  useful mistake to remember: nothing in it was false, and it still sold the
  wrong thing. Reproduction is the part of the job a customer never wanted done
  for them. They wanted the fix. The banner now says so.

  KEEP THE BANNER FREE OF ANYTHING THAT EXPIRES. The letterforms are outlined
  paths, so a sentence in there is only correct until someone remembers to
  regenerate it. No metric, no count, no benchmark score, no date. STATUS lives
  in the alt text below -- one line to edit, no regeneration -- which is why the
  banner can describe the product while the alt text carries where the build is.

  The two attributes below are the exception, and they are not decoration. The
  alt text is what a screen reader announces and what a search index sees, so it
  carries the same claim the picture makes rather than naming the file. Neither
  renders visibly, so the page still reads as one image.

  banner.svg is GENERATED. Do not hand-edit it -- the letterforms are outlined
  paths and there is no live text to find. Change the copy, the palette or the
  timing in ../tools/build_banner.py and run:

      python3 -m venv .venv && ./.venv/bin/pip install "fonttools[woff]" brotli
      ./.venv/bin/python tools/build_banner.py

  (A venv is needed on macOS: the system Python refuses `pip install` under
  PEP 668.)

  If GitHub ever fails to resolve the relative path on the org page, the same
  file is reachable absolutely:
  https://raw.githubusercontent.com/Credda-io/.github/main/profile/banner.svg
-->

<a href="https://credda.io">
  <img src="./banner.svg" width="880"
       alt="Credda. Anyone can tell you it is broken; Credda opens the pull request. Credda finds the security risks and the bugs in a company's production and QA environments and opens the pull request that fixes them: it runs in your own CI, reproduces the reported failure, finds what actually caused it, writes the patch, and proves it with a test that fails before and passes after. A person reviews the diff; Credda never merges. The reporting stages ship today and the fix stage lands with the model-backed release.">
</a>
