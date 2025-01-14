from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def purchase_tshirt():
    driver.get("https://oragestudio.com/collections/nowosci")
    
    # Implement logic to add the t-shirt to the cart and proceed to checkout
    tshirt = driver.find_element(By.XPATH, "//a[contains(text(), 'Seashell T-shirt')]")
    tshirt.click()

    # Add to cart
    add_to_cart = driver.find_element(By.NAME, "add")
    add_to_cart.click()

    # Proceed to checkout (Modify according to the website's checkout process)
    checkout = driver.find_element(By.NAME, "checkout")
    checkout.click()

    # Fill in checkout details (Use a test account)
    # ...

# Call this function after the scraper detects the t-shirt
purchase_tshirt()