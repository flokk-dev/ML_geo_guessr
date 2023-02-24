"""
Creator: HOCQUET Florian, TESSE Paul
Date: 24/01/2023
Version: 1.0

Purpose:
"""

# IMPORT: utils
import os

"""
ROOT
"""
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

"""
RESOURCES
"""
RESOURCES_PATH = os.path.join(ROOT_PATH, "resources")
DATA_PATH = os.path.join(RESOURCES_PATH, "data")

"""
MODELS
"""
MODEL_SAVE_PATH = os.path.join(RESOURCES_PATH, "models")
