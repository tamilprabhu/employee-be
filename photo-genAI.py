from diffusers import StableDiffusionPipeline
import torch

model_id = "sd-legacy/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32, safety_checker = None)
# pipe = pipe.to("cuda")

prompt = "a photo of full earth taken from moon long shot"
image = pipe(prompt).images[0]  
    
image.save("astronaut_rides_horse.png")
