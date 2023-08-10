from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def search_with_selenium(driver, query):
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()  
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    driver.implicitly_wait(10)

links = []
link_elements = driver.find_elements(By.TAG_NAME, "a")
    for link_element in link_elements:
        link_href = link_element.get_attribute("href")
        if link_href and link_href.startswith("http://"):
            links.append(link_href)
    
return links

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

    driver.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion")

    search_query = input("Insira a palavra-chave:" ) 
    onion_links = search_with_selenium(driver, search_query)

for link in onion_links:
    print(link)

driver.quit()
