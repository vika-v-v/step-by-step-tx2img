# Step by step image generation with FLUX.1-dev

This project aims to bring clarity into the way FLUX removes noise from the images during generation.

Example:
<img src="/example_people_coworking_animation.gif" alt="Demo login" style="max-width:80%;">

This project includes:
- the script to generate step-by-step images: [generate-tx2img-flux.py](generate-tx2img-flux.py)
- the example gif: [example_people_coworking_animation.gif](example_people_coworking_animation.gif)
- folders with example images: [example_people_at_the_office](example_people_at_the_office) and [example_people_coworking](example_people_coworking)

## Getting started
To run the script, do the following:
- Make sure you have python installed
- Clone this project and open it's root path
- Create and activate a virtual environment:
  <pre>
  python3 -m venv venv
  source venv/bin/activate
  </pre>
- Install the dependencies:
  <pre>
  pip install -r requirements.txt
  </pre>
- Get access to the FLUX.1-dev model:
  - Go to [https://huggingface.co/black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)
  - Request access
  - Create a token under: your profile top right → Access Tokens → Create new token → select some token name like "fux", scroll to the botoom to "Repositories permissions" and type in "black-forest-labs/FLUX.1-dev", click "create token" and copy it, it might take a few minutes before you can continue to the next step
- Add hugging face token:
  <pre>
  huggingface-cli login
  </pre>
  and paste the token you just copied
- Run the script with
  <pre>
  python3 generate-tx2img-flux.py
  </pre>
