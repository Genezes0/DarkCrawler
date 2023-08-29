import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def extract_links_from_code_2(driver):
    onion_links = []

    time.sleep(20)
    html_text = driver.page_source
    soup = BeautifulSoup(html_text, "html.parser")
    code_2_elements = soup.find_all("div", class_="result")
    for code_2_element in code_2_elements:
        a_element = code_2_element.find("a")
        if a_element:
            link = a_element["href"]
            onion_links.append(link)
    return onion_links

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
    onion_links = extract_links_from_code_2(driver)

    for link in onion_links:
        print(link)

    driver.quit()
