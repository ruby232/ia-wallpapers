import os
import requests
import io
from PIL import Image
import random


def generate_image_online(prompt, image_name, api_key, folder):
    API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
    headers = {"Authorization": f"Bearer {api_key}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    image_bytes = query({
        "inputs": prompt,
    })
    image = Image.open(io.BytesIO(image_bytes))
    image_path = f"{folder}/{image_name}.png"
    image.save(image_path)
    return image_path


def get_prompt(api_key):
    API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-use-cache": "false"
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    themes = [
        "nature", "space", "abstract", "animals", "food", "art", "music", "sports", "cars", "anime",
        "movies", "games", "books", "comics", "cartoons", "fantasy", "history", "science", "education", "health",
        "fashion", "lifestyle", "culture", "travel", "architecture", "design", "photography", "gaming",
        "programming", "philosophy", "literature", "technology", "engineering", "mathematics", "physics",
        "chemistry", "biology", "geology", "astronomy", "meteorology", "environment", "ecology", "agriculture",
        "forestry", "fishing", "mining", "manufacturing", "construction", "transportation", "energy", "utilities",
        "telecommunications", "internet", "software", "hardware", "networking", "security", "databases", "web",
        "mobile", "ai", "robotics", "insurtech", "regtech", "legaltech", "edtech", "medtech", "biotech", "pharma",
        "healthtech", "agtech", "kayak", "foodtech", "cleantech", "greentech", "sustainability", "renewables",
        "recycling", "waste", "pollution", "savannas", "tundras", "climate", "biodiversity", "conservation",
        "ecosystems", "wildlife", "oceans", "forests", "deserts", "mountains", "rivers", "lakes", "islands",
        "parks", "gardens", "farms", "fields", "meadows", "jungles",
    ]

    # Random theme
    theme = random.choice(themes)

    prompt = query({
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": f"Create a simple prompt to generate a wallpaper on a random theme using IA, with max 100 characters and response only with the prompt. Whith the theme: {theme}"
            }
        ],
        "max_tokens": 500,
        "stream": False
    })
    return prompt


def change_wallpaper(image_path):
    if not os.path.exists(image_path):
        print(f"The image {image_path} does not exist.")
        return False
    os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}")
