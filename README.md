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
- Create and activate a virtual environment:
  <code>
    python3 -m venv venv
    source venv/bin/activate
  </code>
- Install the dependencies:
- Get access to the FLUX.1-dev model:
  - Go to [https://huggingface.co/black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)
  - Request access
  - Create a token under your profile top right -> Access Tokens -> Create new token -> select some token name like "fux", scroll to the botoom to "Repositories permissions" and type in "black-forest-labs/FLUX.1-dev", click "create token" and copy it
- Add hugging face token:
  <code>
    huggingface-cli login
  </code>
  and paste the token you just copied
- Run the script with
  <code>
    python3 generate-tx2img-flux.py
  </code>
