import requests
from bs4 import BeautifulSoup
import pandas as pd

# The URL from which you want to scrape the data
URL = 'https://chylak.com/pl/pl/products/basket-bags'
# Headers to simulate a request coming from a browser
headers = {"User-Agent": "Mozilla/5.0"}

# Send a GET request to the URL
response = requests.get(URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the relevant elements containing the data
    products_title = [title.text.strip() for title in soup.find_all('div', class_='product-tile__info')]
    products_title = [title.text.strip()[:-11] for title in soup.find_all('div', class_='product-tile__info')]
    products_price = [price.text.strip() for price in soup.find_all('div', class_='product-tile__info__price')]
    product_images = []
    for picture in soup.find_all('picture'):
        source_tag = picture.find('source', media="(max-width: 600px)")
        if source_tag:
            product_images.append(source_tag['srcset'].split(', ')[0].split(' ')[0])
    product_stock = [stock.text.strip() for stock in soup.find_all('div', class_='product-tile__stock')]


    # Extract every second URL (starting from the second one)
    product_only_image_urls = product_images[::2]

    # Create a DataFrame from the data
    data = {
        'Product Title': products_title,
        'Product Price': products_price,
        'Product Image': product_only_image_urls,
        # 'Product Stock': product_stock
    }
    df = pd.DataFrame(data)

    # Print the DataFrame
    pd.set_option('display.max_colwidth', None)
    print(df)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")



# def download_image(image_url, filename):
#     response = requests.get(image_url)
#     if response.status_code == 200:
#         with open(filename, 'wb') as file:
#             file.write(response.content)
