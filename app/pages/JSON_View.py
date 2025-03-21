"""
File: JSON_View.py
Author: Samuel Van Winkle
"""

import streamlit as st
from data import get_data, last_updated, DATA_FILE

events = get_data()

st.title("Yu-Gi-Oh Cards")
#st.subheader(f"Updated: {last_updated(events)}")
st.json(events)
with open(DATA_FILE, encoding="utf-8") as f:
    st.sidebar.download_button(
        "Download JSON", f, file_name="az_events.json", mime="application/json", type="primary")