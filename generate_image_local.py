# This did not work on my machine due to lack of resources.

import torch
from diffusers import FluxPipeline

def generate_image():
    #pipe = FluxPipeline.from_pretrained("models/black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16)
    #pipe.enable_model_cpu_offload() #save some VRAM by offloading the model to CPU. Remove this if you have enough GPU power

    pipe = FluxPipeline.from_pretrained("models/black-forest-labs/FLUX.1-schnell", torch_dtype=torch.float32)
    #pipe.to("cpu")

    prompt = "A cat"
    image = pipe(
        prompt,
        guidance_scale=0.0,
        num_inference_steps=4,
        max_sequence_length=256,
        generator=torch.Generator("cpu").manual_seed(0)
    ).images[0]
    image.save("flux-schnell.png")