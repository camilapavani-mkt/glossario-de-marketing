# Marketing Glossary · Glossário de Marketing

**CAC, MVP, LTV, stakeholder, branding. Does marketing still sound like alphabet soup?**

The Marketing Glossary explains marketing terms and acronyms in plain language. Every term has three parts: the concept, a real-life example and a step-by-step "how to apply".

**Live site:** https://glossariomarketing-camilapavani.netlify.app
*(Content in Portuguese.)*

## The story

The glossary is a weekly series I, Camila Pavani, publish on LinkedIn. Each term becomes a post with an animated card, and a new entry on this site.

It was the first website I ever built. I made it from scratch by working with AI (Claude), using my own brand design system, and published it on Netlify. This repository holds the site and the source of every term: each update pushed here goes live automatically in about a minute.

## Published terms

| # | Term | Meaning |
|---|---|---|
| 01 | MVP | Minimum Viable Product |
| 02 | ICP | Ideal Customer Profile |
| 03 | JTBD | Jobs To Be Done |

## How it's organized

- `site/index.html`: the published site (a single file, with the animations embedded)
- `fonte/`: the site template (`site.src.html`), the terms (`termos.js`), the animated cards (`videos/`), the motion templates and the brand fonts
- `fonte/build.py`: puts everything together and generates `site/index.html`

## How it's built

HTML, CSS and JavaScript · animated cards rendered with Playwright and FFmpeg · versioned on GitHub · continuous deployment on Netlify.

---

Camila Pavani · Marketing strategist
[LinkedIn](https://www.linkedin.com/in/camilapavanii) · [Instagram](https://www.instagram.com/camila_pavani)
