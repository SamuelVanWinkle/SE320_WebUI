"""
File: data.py
Author: Samuel Van Winkle
Help from the Sedona Weather sample and ChatGPT
"""

from json import dump, load
import os
from os.path import abspath, join
from datetime import datetime
from dateutil import tz
from requests import get
import streamlit as st

DATA_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "cards.json")


@st.cache_data(show_spinner="Fetching data from APU...", ttl=60*10)
def get_data(data_url: str = DATA_URL, data_file: str = DATA_FILE) -> dict:
    """ Fetches data from the api or file upon failure """
    try:
        data_directory = os.path.dirname(DATA_FILE)
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)
            print(f"Created directory: {data_directory}")

        response = get(url=data_url, timeout=10)
        print(response.status_code)
        cards = response.json()
        if isinstance(cards, dict) and "data" in cards:
            with open(data_file, "w", encoding="utf-8") as file:
                dump(cards, file)
            return cards
        with open(data_file, "r", encoding="utf-8") as file:
            cards = load(file)
        st.warning("Using cached event data", icon="⚠️")
        return cards
    except OSError as err: 
        st.error(str(err), icon="💣")
    except TypeError as err: 
        st.error(str(err), icon="💣")
    return {}

def reload_data() -> None:
    """ Clears the event data cache and makes the next get_data call request json from web service """
    get_data.clear()

def last_updated(cards: dict) -> str:
    """ returns a display string of the last update timestamp """
    dtime = datetime.fromisoformat(cards['LastUpdated'])
    readable_time = datetime.fromtimestamp(dtime).strftime('%Y-%m-%d %H:%M:%S UTC')
    print(readable_time)
