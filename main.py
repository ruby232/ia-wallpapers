import os
import importlib.util
from datetime import datetime
import json

from functions import get_prompt, generate_image_online, change_wallpaper

config_file_path = 'config.py'

if os.path.exists(config_file_path):
    spec = importlib.util.spec_from_file_location("config", config_file_path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
else:
    print(f"El fichero {config_file_path} no existe.")
    exit()

api_key = config.HUGGINGFACE_API_KEY
result_prompt_str = get_prompt(api_key)
result_prompt_json = json.loads(result_prompt_str)
prompt = result_prompt_json["choices"][0]["message"]["content"]

# nombre de la con la fecha y hora actual
image_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
image_path=generate_image_online(prompt, image_name, api_key, config.IMAGE_FOLDER)
change_wallpaper(image_path)
