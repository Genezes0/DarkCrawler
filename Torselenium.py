from selenium import webdriver
from selenium.webdriver.common.by import By

def search_with_findtor(driver, query):
    driver.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion")
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(query)
    search_box.submit()

    return extract_links_findtor(driver)

def search_with_tordex(driver, query):
    driver.get("http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion/")
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(query)
    search_box.submit()

    return extract_links_tordex(driver)

def extract_links_findtor(driver):
    links = []
    link_elements = driver.find_elements(By.TAG_NAME, "a")
    for link_element in link_elements:
        link_href = link_element.get_attribute("href")
        if link_href and link_href.startswith("http://"):
            links.append(link_href)
    return links

def extract_links_tordex(driver):
    links = []
    result_elements = driver.find_elements(By.CLASS_NAME, "result")
    for result_element in result_elements:
        link_elements = result_element.find_elements(By.TAG_NAME, "a")
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

    search_query = input("Insira a palavra-chave: ")

    choice = input("Escolha o mecanismo de busca (FindTor/TorDex): ").lower()

    if choice == "findtor":
        onion_links = search_with_findtor(driver, search_query)
    elif choice == "tordex":
        onion_links = search_with_tordex(driver, search_query)
    else:
        print("Escolha de mecanismo de busca inválida!")

    for link in onion_links:
        print(link)

    driver.quit()
