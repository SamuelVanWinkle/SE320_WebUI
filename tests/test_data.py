"""
File: test_data.py
Author: Samuel Van Winkle
"""

from unittest import TestCase
from data import get_data
from os.path import exists, join
from os import remove
import os

class Test(TestCase):
    def test_data_acquisition(self):
        """
            Test fetching data
        """
        app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
        path_to_data_file = os.path.join(app_dir, "data", "cards.json")
        print(f"File path = {path_to_data_file}")
        if exists(path_to_data_file):
            remove(path_to_data_file)
        assert not exists(path_to_data_file)
        cards = get_data()
        name = cards["data"][0]["name"]
        assert len(name) > 0
        assert cards["data"][0]["id"]
        