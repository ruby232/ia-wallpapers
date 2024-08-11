# IA Wallpapers
Generar y establecer fondos de pantalla en Gnome con [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell), 
[Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) y la api de [Hugging Face](https://huggingface.co/). 

`Probado en Pop!_OS 22.04`

## Instalación
```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate


pip install -r requirements.txt 
```

## Configuración
Crear un fichero config.py y establecer el valor de las variables, usar como referencia config.example.py.

### Variables a configurar:
HUGGINGFACE_API_KEY: La clave API de Hugging Face puede obtenerse en el sitio web de Hugging Face https://huggingface.co/settings/tokens
IMAGE_FOLDER: Ruta absoluta a la carpeta donde se guardarán las imágenes.

## Uso
Ejecutarlo usando Python desde un terminal
```bash
# Activate the virtual environment and run the script
python main.py
```

Sí, se quiere ejecutar desde un lugar externo como el crontab, llamar al script `run.sh`.
```bash
/path/to/run.sh
```