"""
File: test_app.py
Author: Samuel Van Winkle
"""
from unittest import TestCase
from streamlit.testing.v1 import AppTest


class Test(TestCase):
    def test_ui_title_and_header(self) -> None:    
        """
            Tests if the title and header load properly
        """
        at = AppTest.from_file("./app/Cards.py")
        at.run()

        assert at.title[0].value.startswith("Yu-Gi-Oh Cards")
        assert at.header[0].value.startswith("Card List")
        assert not at.exception


