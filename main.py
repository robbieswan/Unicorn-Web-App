import unicorn1
import unicorn2
import streamlit as st

PAGES = {
    "Per Country": unicorn1,
    "Per City": unicorn2
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()