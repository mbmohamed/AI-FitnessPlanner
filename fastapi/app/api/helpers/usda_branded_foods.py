import requests
import zipfile
import os
from pathlib import Path
import time
from tqdm import tqdm

def download_usda_branded_foods(save_directory="./fastapi/app/aapi/nutrition_data"):
    """download the latest dataset of branded foods"""

    #create the new directory for the dataset in case it doesnt exit
    save_path= Path(save_directory)
    save_path.mkdir(parents=True,exist_ok=True)

    #l'url for the dataset

    url="https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_branded_food_json_2025-04-24.zip"
    zip_file= save_path / "branded_foods.zip"

    print(f"Downloading USDA Branded Foods dataset...")
    print(f"URL: {url}")
    print(f"Saving to: {zip_file}")

    """""to be continued....."""