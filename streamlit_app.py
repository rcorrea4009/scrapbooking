import pathlib

import streamlit as st

st.set_page_config(page_title="Happy 1st Anniversary", page_icon="💌", layout="wide")

st.markdown(
    """
    <style>
    .block-container {padding: 0 !important; max-width: 100% !important;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = pathlib.Path(__file__).parent / "scrapbook.html"
html_content = html_path.read_text(encoding="utf-8")

st.components.v1.html(html_content, height=900, scrolling=False)
