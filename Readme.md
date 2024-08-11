# IA Wallpapers
Generating and setting wallpapers in GNOME with AI [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell), 
[Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) and the API [Hugging Face](https://huggingface.co/). 

`Testing in en Pop!_OS 22.04`

## Installation
```bash
# Create and active a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt 
```

## Configuration
Create a config.py file and set the value of the variables, use config.example.py as reference.

Variables to be configured:
HUGGINGFACE_API_KEY: Hugging Face API key, it can be obtained from the Hugging Face website https://huggingface.co/settings/tokens
IMAGE_FOLDER: Absolute path to the folder where the images will be saved

## Usage
Run it using Python from a terminal
```bash
# Activate the virtual environment and run the script
python main.py
```

If you want to run from an external location such as the crontab, call the script `run.sh`.
```bash
/path/to/run.sh
```