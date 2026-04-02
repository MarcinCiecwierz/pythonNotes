import os
from dotenv import load_dotenv
import streamlit as st
import requests

load_dotenv()

API_URL = os.getenv('API_URL')

st.set_page_config(page_title="Notes Base", layout="wide")
st.title("Notes Base")

with st.expander("Add new note"):
    title = st.text_input("Title")
    content = st.text_area("Content")
    tags = st.text_input("Tags (comma separation)")

    if st.button("Save"):
        if title and content:
            res = requests.post(API_URL + "/add", json={
                "title": title,
                "content": content,
                "tags": tags
            })
            if res.status_code == 200:
                st.success("Note added.")
                st.rerun()
            else:
                st.error("Something went wrong.")
        else:
            st.warning("Title and content is required.")


res = requests.get(API_URL, "/")
notes = res.json() if res.status_code == 200 else []

if not notes:
    st.info("Cannot find notes. Add first!")
else:
    cols = st.columns(3)
    for i, note in enumerate(notes):
        with st.container(border=True):
            st.subheader(note["title"])
            st.caption(f"{note['tags']}" if note["tags"] else "")
            st.write(note["content"])
            if st.button("Delete", key=f"delete_{note['id']}"):
                requests.delete(f"{API_URL}/{note['id']}")
                st.rerun()

