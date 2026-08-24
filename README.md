# scrapbooking

A "Happy 1st Anniversary" interactive scrapbook: a photo book with a page-flip
book intro, plus a jar of 365 keepsake messages.

- `scrapbook.html` — the self-contained scrapbook (HTML/CSS/JS, no build step).
- `streamlit_app.py` — a thin Streamlit wrapper that embeds `scrapbook.html`
  so the whole thing can be deployed on Streamlit Community Cloud.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
