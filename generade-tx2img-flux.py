import os
os.environ["CUDA_VISIBLE_DEVICES"] = "10" 

import torch
from diffusers import DiffusionPipeline
import numpy as np
from PIL import Image

# Set up device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Create a folder for step images
steps_folder = "generation_steps_2"
os.makedirs(steps_folder, exist_ok=True)
print(f"Created folder: {steps_folder}")

# Load the FLUX.1-dev model directly from Hugging Face
print("Loading FLUX.1-dev model...")
pipeline = DiffusionPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-dev",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    use_safetensors=True
)
pipeline = pipeline.to(device)

# Define the image generation prompt
prompt = """A modern, sleek coworking space interior with wooden floors and black acoustic ceiling panels. The space features stylish black pendant lights hanging over a minimalist bar counter with high stools along one side. In the foreground, two professionals are having a meeting at a small round table with vibrant orange chairs. The space is accented with indoor plants, a statement green abstract wall mural, and contemporary furniture. The lighting is bright and natural, creating an inviting atmosphere with a blend of professional and creative elements. Wide angle, architectural photography style, highly detailed."""
negative_prompt = "low quality, blurry, distorted, unrealistic, poor lighting, bad anatomy"

# Total number of inference steps
total_steps = 100

# Set fixed seed for reproducibility
seed = 50

# Generate pure noise image for step 0
print("Generating pure noise image (step 0)...")
height, width = 512, 1024

# Create a random noise image without using the VAE
np.random.seed(seed)  # Set numpy random seed for consistency
noise = np.random.rand(height, width, 3) * 255  # Random RGB values
noise_img = Image.fromarray(noise.astype(np.uint8))
noise_filename = os.path.join(steps_folder, "step_0.png")
noise_img.save(noise_filename)
print(f"Saved random noise image to {noise_filename}")

# Now generate every intermediate step
for step in range(1, total_steps + 1):
    print(f"Generating image for step {step}/{total_steps}...")
    
    # Reset the generator for consistency
    generator = torch.Generator(device=device).manual_seed(seed)
    
    # Generate image with specified number of steps
    image = pipeline(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=step,  # Run only up to this step
        guidance_scale=7.5,
        width=width,
        height=height,
        generator=generator,
    ).images[0]
    
    # Save the intermediate image
    step_filename = os.path.join(steps_folder, f"step_{step}.png")
    image.save(step_filename)
    print(f"Saved step {step} to {step_filename}")

print("All steps have been generated and saved.")