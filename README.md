# arbutus.audio

The public site for Arbutus-1, a portable synthesizer, sampler and 4-track recorder.
Static HTML, CSS and vanilla JavaScript, served by GitHub Pages from `main` at https://arbutus.audio.

## Structure

- `index.html`: the whole site. Hero, one-minute mission, contact and signup, then the development log newest first.
- `assets/css/styles.css`: three colour tokens at the top (`:root`): beige, brown, green, from the look-alike model. Everything else is a shade of those.
- `assets/js/carousel.js`: carousels, lightbox and the signup form handler.
- `assets/images/logo.svg`: the branch logo, converted from `logo.dxf`. Ring and branch in brown, leaves in green.
- `assets/images/log/`: photos for the log, resized to 1600 px on the long edge. `r<N>.jpg` files came from the co-op bi-monthly report workbook, numbered by their order in it.

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
