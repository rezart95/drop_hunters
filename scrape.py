import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    """
    Launch a Chrome browser and scrape the HTML content of a given website.
    
    Args:
        website (str): The URL of the website to scrape.
        
    Returns:
        str: The HTML source code of the webpage.
        
    Note:
        Requires ChromeDriver to be installed at the specified path.
    """
    print("Launching Chrome browser...")

    chrome_driver_path="C:/Users/User/github_projects/drop_hunters/chromedriver.exe"
    options=webdriver.ChromeOptions()
    driver=webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded successfully")
        html=driver.page_source
        # time.sleep(10)
        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    """
    Extract the body content from HTML using BeautifulSoup.
    
    Args:
        html_content (str): Raw HTML content to parse.
        
    Returns:
        str: The extracted body content as a string, or empty string if no body found.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    """
    Clean HTML body content by removing scripts, styles, and excess whitespace.
    
    Args:
        body_content (str): HTML body content to clean.
        
    Returns:
        str: Cleaned text content with preserved line breaks.
    """
    soup = BeautifulSoup(body_content, "html.parser")
    
    # Remove all script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text content and clean up whitespace
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content, max_length=8000):
    """
    Split DOM content into chunks of specified maximum length.
    
    Args:
        dom_content (str): The content to split.
        max_length (int, optional): Maximum length of each chunk. Defaults to 8000.
        
    Returns:
        list: List of content chunks, each no longer than max_length.
    """
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
    ]