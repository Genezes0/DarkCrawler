import time
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

    driver.implicitly_wait(30)
    time.sleep(20)

    onion_links = []

    html_text = driver.page_source

    soup = BeautifulSoup(html_text, "html.parser")
    title_element = soup.find("h5", id="title")
    a_element = title_element.find("a")
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
    onion_links = search_with_selenium(driver, search_query)
    time.sleep(20)

    for link in onion_links:
        print(link)

#    driver.quit()
