# app.py
import todolist
import videotutorial
import docstutorial

import streamlit as st

PAGES = {
    "ToDo List": todolist,
    "Video Tutorial": videotutorial,
    "Docs Tutorial": docstutorial
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Select", list(PAGES.keys()))
page = PAGES[selection]
page.app()
