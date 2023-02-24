"""
Creator: HOCQUET Florian
Date: 30/01/2023
Version: 1.0

Purpose:
"""

# IMPORT: utils
import argparse

# IMPORT: deep learning
import torch

# IMPORT: project
from src import Trainer2D

# WARNINGS SHUT DOWN
import warnings
warnings.filterwarnings("ignore")


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Get model training parameters.")

    parser.add_argument("-m", "--model", type=str, nargs="?", default=None,
                        help="the model's path.")

    parser.add_argument("-p", "--pipe", type=str, nargs="?",
                        choices=["training", "inference"], default="training",
                        help="the type of pipeline to use")

    parser.add_argument("-ll", "--lazy_loading", type=str, nargs="?", default=False,
                        help="the loading method.")

    return parser


if __name__ == "__main__":
    # Free the memory
    torch.cuda.empty_cache()

    # Parameters
    parser = get_parser()
    args = parser.parse_args()

    params = {
        "batch_size": 16, "epochs": 20, "valid_coeff": 0.2,
        "lr": 1e-2, "lr_multiplier": 0.9,
        "lazy_loading": args.lazy_loading, "workers": 1,
    }

    print()
    for key, value in params.items():
        print(f"{key}: {value}")

    tasks = {"training": Trainer2D, "inference": None}
    task = tasks[args.pipe](params=params, model_path=args.model)
    task.launch()
