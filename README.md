# lariscus.de

Source of the Lariscus website (Drey and dricket), served by GitHub Pages at <https://lariscus.de>.

Plain static files, no framework, no tracking. The pages are generated from one script:

```bash
python3 scripts/build.py   # rewrites index.html, drey/, dricket/, 404.html, sitemap.xml, robots.txt
python3 -m http.server 8000
```

Images live in `assets/` (WebP in 1000 and 1800 px widths, Open Graph cards, favicons). Screenshots come from the Drey manual.
