"""
Creator: HOCQUET Florian
Date: 13/02/2023
Version: 1.0

Purpose:
"""

# IMPORT: utils
import os
import time

import pytesseract

# IMPORT: data processing
import torch
import numpy as np

# IMPORT: data visualization
import matplotlib.pyplot as plt

# IMPORT: mouth management
import pyautogui

# IMPORT: project
import paths
from utils import GeoGuessrButtons


class DataExtractor:
    def __init__(self):
        # Screen size
        screen_resolution = pyautogui.size()
        self._width, self._height = screen_resolution.width, screen_resolution.height

        # Image order
        self._order = {"N": 0, "E": 1, "S": 2, "W": 3}

        # Geoguessr buttons
        self._geo_buttons = GeoGuessrButtons()

    def _launch(self, nb_country):
        nb_data = len(os.listdir(paths.DATA_PATH))
        for i in range(nb_country):
            self._extract_country(country_id=i+nb_data)
            self._check_result()

    def _extract_country(self, country_id):
        if not os.path.exists(os.path.join(paths.DATA_PATH, str(country_id))):
            os.makedirs(os.path.join(paths.DATA_PATH, str(country_id)))

        # Extract directions
        self._geo_buttons.start()
        for direction in ["N", "E", "S", "W"]:
            self._geo_buttons.directions(direction)
            self._screenshot(
                path=os.path.join(paths.DATA_PATH, str(country_id), f"{self._order[direction]}.pt")
            )

        # Extract sky
        time.sleep(0.5)
        self._geo_buttons.start()
        self._drag(direction="top")

        self._screenshot(
            path=os.path.join(paths.DATA_PATH, str(country_id), f"4.pt")
        )

        # Extract car
        time.sleep(0.5)
        self._geo_buttons.start()
        self._drag(direction="bottom")
        time.sleep(0.5)

        self._screenshot(
            path=os.path.join(paths.DATA_PATH, str(country_id), f"5.pt")
        )

    def _screenshot(self, path):
        self._move((10, 10))

        image = np.array(pyautogui.screenshot())
        image = image[:, int(self._width*0.1):int(self._width*0.85)]

        tensor = torch.permute(torch.from_numpy(image), dims=(2, 0, 1)).unsqueeze(dim=0)
        tensor = torch.permute(torch.nn.functional.interpolate(tensor, (512, 512), mode="nearest-exact"), dims=(0, 2, 3, 1))

        torch.save(tensor.type(torch.uint8), path)
        return tensor

    def _drag(self, direction):
        height = self._height-25 if direction == "bottom" else 25
        distance = -1500 if direction == "bottom" else 1500
        duration = 2

        self._move((self._width//2, height))
        pyautogui.drag(0, distance, duration, button="left")

        self._move((self._width // 2, height))
        pyautogui.drag(0, distance//5, duration//5, button="left")

        time.sleep(0.5)

    def _check_result(self):
        # Validate guess
        self._geo_buttons.map()
        self._geo_buttons.guess_country()
        self._geo_buttons.guess()

        # Extract answer
        pass

    @staticmethod
    def _move(position):
        pyautogui.moveTo(position)

    @staticmethod
    def _get_position():
        return pyautogui.position()

    @staticmethod
    def _click(position):
        pyautogui.click(position)

    @staticmethod
    def _plot(image):
        plt.imshow(image)
        plt.show()

    def __call__(self, nb_country):
        self._launch(nb_country)
        while True:
            print(self._get_position())
            time.sleep(5)


data_extractor = DataExtractor()
data_extractor(nb_country=1)
