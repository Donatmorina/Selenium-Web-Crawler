from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin, urlparse
import time

driver = webdriver.Chrome()

base_url = "https://sites.google.com/view/nikt2024?usp=sharing"
parsed_base = urlparse(base_url).netloc

visited_pages = set()

def crawl(url):
    """ Crawls a webpage, extracts internal links, and prints text content """
    
    if url in visited_pages:
        return 

    print(f"\nCrawling: {url}")
    visited_pages.add(url)  
    driver.get(url)
    time.sleep(2) 

    try:
        texts = driver.find_elements(By.XPATH, "//span[@class='C9DxTc ']")
        print("\n".join([text.text for text in texts if text.text.strip()]))
    except:
        print("No text found!")

    links = driver.find_elements(By.TAG_NAME, "a")
    all_links = [link.get_attribute("href") for link in links if link.get_attribute("href")]

    internal_links = set([link for link in all_links if link and urlparse(link).netloc == parsed_base])

    for link in internal_links:
        if link not in visited_pages:
            crawl(link)

crawl(base_url)

driver.quit()
