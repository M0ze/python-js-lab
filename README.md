# notes — Flask CRUD + vanilla JS frontend (Python/JS P1)

A tiny note-taking app with a vanilla JS UI. Teaches: routing, templates,
fetch, DOM, JSON.

## How to run

    cd notes
    python3 -m venv .venv
    source .venv/bin/activate
    pip install flask
    flask --app app run --debug

Open http://127.0.0.1:5000. Add a note, then it appears without a page
reload — that is the fetch + DOM part.

## Files

    app.py          Flask app (routes + in-memory store)
    static/app.js   vanilla JS: fetch, render, delete
    templates/index.html  single page + note list

## Roadmap

| # | Project | Stack | Core concept |
|---|---------|-------|--------------|
| 1 | notes | Flask + vanilla JS | routes, templates, fetch, JSON |
| 2 | api | Express + SQLite | REST, middleware, promises |
| 3 | dashboard | Next.js | React, SSR, data fetching |

## Toolchain (this machine)

    python 3.14.9   node v26.13.1
    npm 11.20.0
