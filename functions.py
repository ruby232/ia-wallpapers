import os
import requests
import io
from PIL import Image


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

    prompt = query({
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": "Create a simple prompt to generate a wallpaper on a random theme using IA, with max 100 characters and response only with the prompt."
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
