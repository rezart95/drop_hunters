import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import hashlib

# The URL from which you want to scrape the data
category = 'basket-bags'
URL = f'https://chylak.com/pl/pl/products/{category}'

# Headers to simulate a request coming from a browser
headers = {"User-Agent": "Mozilla/5.0"}

# Send a GET request to the URL
response = requests.get(URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the relevant elements containing the data
    products_title = [title.text.strip()[:-11] for title in soup.find_all('div', class_='product-tile__info')]
    products_price = [price.text.strip() for price in soup.find_all('div', class_='product-tile__info__price')]
    product_images = []
    product_urls = []
    
    for picture in soup.find_all('picture'):
        source_tag = picture.find('source', media="(max-width: 600px)")
        if source_tag:
            product_images.append(source_tag['srcset'].split(', ')[0].split(' ')[0])
            # Find the parent <a> tag to get the product URL
            parent_a_tag = picture.find_parent('a', {'data-track': 'productTile'})
            if parent_a_tag:
                product_urls.append(f"https://chylak.com{parent_a_tag['href']}")
    product_stock = [stock.text.strip() for stock in soup.find_all('div', class_='product-tile__stock')]

    # Extract every second URL (starting from the second one)
    product_only_image_urls = product_images[::2]
    product_only_one_url = product_urls[::2]

    # Create a DataFrame from the data
    data = {
        'Product Title': products_title,
        'Product Price': products_price,
        'Product Image': product_only_image_urls,
        'Product URL': product_only_one_url,
        # 'Product Stock': product_stock
    }
    df = pd.DataFrame(data)

    # Print the DataFrame
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_columns', None)
    print(df)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")


# Folder where images will be saved
folder_name = 'downloaded_images'
os.makedirs(folder_name, exist_ok=True)

# Loop through the image URLs
for i, url in enumerate(product_only_image_urls):
    try:
        # Fetch the image
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Extract the name from the URL
        url_parts = url.split('/')
        image_name = url_parts[-1].split('?')[0]  # Get the last part of the URL and remove query parameters

        # Construct a file path where the image will be saved
        file_path = os.path.join(folder_name, image_name)

        # Write the image to a file
        with open(file_path, 'wb') as file:
            file.write(response.content)
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")