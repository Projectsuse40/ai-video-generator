import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

def fetch_images(topic, count=10, retries=3, delay=2):
    headers = {
        "Authorization": os.getenv("PEXELS_API_KEY")
    }
    url = f"https://api.pexels.com/v1/search?query={topic}&per_page={count}"

    os.makedirs("assets/images", exist_ok=True)

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            image_paths = []

            for i, photo in enumerate(data.get("photos", [])):
                img_url = photo["src"]["medium"]
                img_data = requests.get(img_url, timeout=10).content

                path = f"assets/images/img_{i}.jpg"
                with open(path, "wb") as f:
                    f.write(img_data)

                image_paths.append(path)

            if not image_paths:
                raise ValueError("No images returned from Pexels")

            return image_paths

        except Exception as e:
            print(f"[WARN] Pexels fetch failed (attempt {attempt}/{retries}): {e}")
            time.sleep(delay)

    raise RuntimeError("Pexels API failed after multiple retries")
