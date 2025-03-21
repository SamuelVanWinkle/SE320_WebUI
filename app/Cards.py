"""
File: Cards.py
Author: Samuel Van Winkle
Some help from Sedona Weather example and ChatGPT
"""

import pandas as pd
import streamlit as st
import altair as alt
from data import reload_data, get_data, last_updated


st.set_page_config(
    page_title="Yu-Gi-Oh Card Database"
)

st.markdown(
    """
    <style>
        header {visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True
)

cards = get_data()

st.title("Yu-Gi-Oh Cards")
st.header("Card List")

cards_per_page = 100
total_cards = len(cards["data"])
total_pages = (total_cards + cards_per_page - 1) // cards_per_page

# Page Selector
page_number = st.number_input("Select Page", min_value=1, max_value=total_pages, value=1, step=1)
st.write(f"Page ({page_number} - {total_pages})")

# Calculates the range of cards to display
start_index = (page_number - 1) * cards_per_page
end_index = start_index + cards_per_page
paginated_cards = cards["data"][start_index:end_index]

with st.container(border=True):
    for card in paginated_cards:
        col1, col2, col3 = st.columns(3, gap="medium")

        with col1:
            st.markdown(f"<p style='font-size:24px;'><strong>Name:</strong> {card['name']}</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p style='font-size:24px;'><strong>Type:</strong> {card['type']}</p>", unsafe_allow_html=True)
        with col3:
            st.image(card["card_images"][0]["image_url"], use_container_width=True)

updat_btn = st.sidebar.button("Update", type="primary", on_click=reload_data)
columns = ["ID", "Description", "Severity", "EventType", "StartDate"]
chart_data = pd.DataFrame(cards, columns=columns)
