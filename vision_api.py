# Use Open AI vision api to look at the downloade photos and chek if they are the same as the one we want
from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

load_dotenv() 

OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')
client = OpenAI(api_key=OPEN_AI_KEY)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "chylak-shell-bag-black-11.jpeg"

# Getting the base64 string
base64_image = encode_image(image_path)
local_image_url = f"data:image/jpeg;base64,{base64_image}"

list_of_urls = ['https://chylak.imgix.net/2022/06/chylak-backpack-glossy-black-crocodile-3.jpg?auto=format,compress&w=720&h=1080&fit=crop',
"https://chylak.imgix.net/2023/09/chylak-shell-bag-brown-ostrich-6.jpg?auto=format,compress&w=720&h=1080&fit=crop",
"https://chylak.imgix.net/2021/06/chylak-big-basket-bag-glossy-black-crocodile-1.jpg?auto=format,compress&w=1200&h=1500&fit=crop",
# below in is same
"https://chylak.imgix.net/2022/10/chylak-shell-bag-black-4.jpg?auto=format,compress&w=1200&h=1500&fit=crop"
]
for other_url in list_of_urls:

  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": f"""You're shop assistant. Your task is to compare if products are identicall on both photos.
            Answer 0 if products are different and answer 1 if on both pictures there is the same product."""
          },
          {
            "type": "image_url",
            "image_url": {
              "url": local_image_url
              # "https://chylak.imgix.net/2023/11/chylak-small-shell-bag-black-6.jpg?auto=format,compress&w=720&h=1080&fit=crop",
            },
          },
          {
            "type": "image_url",
            "image_url": {
              "url": other_url,
            },
          },
        ],
      }
    ],
    max_tokens=10,
  )
  print(response.choices[0].message.content)