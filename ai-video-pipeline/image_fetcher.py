import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_images(topic, count=10):
    headers = {
        "Authorization": os.getenv("PEXELS_API_KEY")
    }
    url = f"https://api.pexels.com/v1/search?query={topic}&per_page={count}"

    response = requests.get(url, headers=headers).json()
    image_paths = []

    for i, photo in enumerate(response["photos"]):
        img_url = photo["src"]["medium"]
        img_data = requests.get(img_url).content
        path = f"assets/images/img_{i}.jpg"
        with open(path, "wb") as f:
            f.write(img_data)
        image_paths.append(path)

    return image_paths