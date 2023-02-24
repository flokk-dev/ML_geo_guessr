"""
Creator: HOCQUET Florian
Date: 13/02/2023
Version: 1.0

Purpose:
"""

# IMPORT: utils
import time

# IMPORT: mouth management
import pyautogui


class GeoGuessrButtons:
    def __init__(self):
        self._delay = 0.5

        # Start button
        self._buttons = {
            "start": (120, 1335),
            "map": (2969, 1074),
            "guess_country": (2812, 917),
            "guess": (2885, 1400)
        }

        # Directions
        self._directions = {
            "N": (54, 1112),
            "E": (80, 1138),
            "S": (54, 1164),
            "W": (28, 1138)
        }

    def start(self):
        pyautogui.click(self._buttons["start"])
        time.sleep(self._delay)

    def map(self):
        pyautogui.click(self._buttons["map"])
        time.sleep(self._delay)

    def guess_country(self):
        pyautogui.click(self._buttons["guess_country"])
        time.sleep(self._delay)

    def guess(self):
        pyautogui.click(self._buttons["guess"])
        time.sleep(self._delay)

    def directions(self, direction):
        pyautogui.click(self._directions[direction])
        time.sleep(self._delay)
