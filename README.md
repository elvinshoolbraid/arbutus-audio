# arbutus.audio

The public site for Arbutus-1, a portable synthesizer, sampler and eight-track recorder.
Static HTML, CSS and vanilla JavaScript, served by GitHub Pages from `main` at https://arbutus.audio.

## Structure

- `index.html`: the whole site. Hero, one-minute mission, contact and signup, then the development log newest first.
- `assets/css/styles.css`: three colour tokens at the top (`:root`): beige, brown, green, from the look-alike model. Everything else is a shade of those.
- `assets/js/carousel.js`: carousels, lightbox and the signup form handler.
- `assets/images/logo.svg`: the branch logo, converted from `logo.dxf`. Ring and branch in brown, leaves in green.
- `assets/images/icon.svg`: the logo on a filled beige disc, for browser tabs, the address bar and search results. `favicon.ico` (16, 32, 48 px), `assets/images/icon-192.png` and `apple-touch-icon.png` (180 px, on a beige square) are rendered from it.
- `assets/images/log/`: photos for the log, resized to 1600 px on the long edge. `r<N>.jpg` files came from the co-op bi-monthly report workbook, numbered by their order in it.

## The cost stack

The `#pricing` section of `index.html` (between the `cost-stack:begin` and `cost-stack:end` markers) is generated; do not edit it by hand. In the Arbutus-1 repo, `python3 docs/strategy/finance/calc.py --public` writes `docs/strategy/finance/cost-stack-public.md`; then, here:

```bash
python3 tools/cost-stack.py ../Arbutus-1/docs/strategy/finance/cost-stack-public.md
```

It rewrites only that section, from the file's tables and its "Prices as of" date, as one bar at a batch of 25 and a stacked chart across every batch size in the file. Every row of the tables must belong to a layer in `LAYERS` at the top of the script; a new row stops it with a message rather than vanishing from the bar. Check the price line in *Honestly priced* (the batch-of-25 figure) still matches.

## Adding a log post

Copy any `<article class="post">` block in `index.html`, change the date pill, title, slides and text, and place it at the top of the `#log` section. A carousel with one slide needs no prev/next buttons. Captions live in the `.caption` element under each image and are reused by the lightbox.

## Signup form

The form posts to Formspree. Replace `YOUR_FORM_ID` in the form's `action` with the ID from formspree.io. Until then the form shows a note asking people to email instead.

## Local preview

```bash
open index.html
```

## Contact

Elvin Shoolbraid, elvin@arbutus.audio
