import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def search_with_selenium(driver, query):
    try:
        search_box = driver.find_element(By.NAME, "query")
    except:
        search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)  # Reduce sleep time to 10 seconds
    driver.implicitly_wait(10)  # Reduce implicit wait time to 10 seconds

    page = driver.page_source  # Get the page source after the search

    soup = BeautifulSoup(page, 'html.parser')
    result_elements = soup.find_all(class_='result')
    all_links = []
    for result_element in result_elements:
        anchor_elements = result_element.find_all('a', href=re.compile("^http://"))
        for anchor in anchor_elements:
            href = anchor.get('href', '')
            if href not in all_links:
                all_links.append(href)

    for href in all_links:
        print(href)

    return all_links  # Change to return all_links

if __name__ == "__main__":
    options = webdriver.FirefoxOptions()
    options.headless = True
    profile = webdriver.FirefoxProfile()

    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "127.0.0.1")
    profile.set_preference("network.proxy.socks_port", 9050)
    profile.set_preference("network.proxy.socks_version", 5)
    profile.set_preference("network.proxy.socks_remote_dns", True)

    options.profile = profile

    driver = webdriver.Firefox(options=options)

    driver.get("http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion")

    search_query = input("Insira a palavra-chave: ")
    onion_links = search_with_selenium(driver, search_query)  # Call the function with the correct name
    time.sleep(10)  # Reduce sleep time to 10 seconds

    for link in onion_links:
        print(link)

    driver.quit()
