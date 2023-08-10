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
    result_elements = driver.find_elements(By.CLASS_NAME, "result")
    for result_element in result_elements:
        link = result_element.find_element(By.TAG_NAME, "a")
        links.append(link.get_attribute("href"))
    
    return links

if __name__ == "__main__":
    options = webdriver.FirefoxOptions()
    profile = webdriver.FirefoxProfile()

    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "127.0.0.1")
    profile.set_preference("network.proxy.socks_port", 9050)
    profile.set_preference("network.proxy.socks_version", 5)
    profile.set_preference("network.proxy.socks_remote_dns", True)

    options.profile = profile
    driver = webdriver.Firefox(options=options)

    driver.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion")

    search_query = input("Enter your search query: ")
    onion_links = search_with_selenium(driver, search_query)

    for link in onion_links:
        print(link)

    # Mantenha o navegador aberto para inspecionar manualmente
    input("Press Enter to close the browser...")

    driver.quit()
