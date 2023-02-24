"""
Creator: HOCQUET Florian, TESSE Paul
Date: 24/01/2023
Version: 1.0

Purpose:
"""

# IMPORT: utils
import os
import datetime

# IMPORT: data processing
import torch

# IMPORT: data visualization
import matplotlib.pyplot as plt


def get_datetime():
    """
    Returns the current date.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


def plot_country(path):
    images_paths = [os.path.join(path, file_path) for file_path in sorted(os.listdir(path))]
    images_ids = {0: "North", 1: "East", 2: "South", 3: "West", 4: "Sky", 5: "Car"}

    plt.figure()
    for idx, image_path in enumerate(images_paths):
        plt.subplot(1, len(images_paths), idx+1)
        plt.title(f"{images_ids[idx]}")
        plt.imshow(torch.load(image_path)[0])

    plt.tight_layout(w_pad=0, h_pad=0)
    plt.show()
