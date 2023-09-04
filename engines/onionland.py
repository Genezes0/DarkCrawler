import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def extract_links_from_page(driver):
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    result_elements = soup.find_all(class_='result')
    all_links = []

    for result_element in result_elements:
        link_div = result_element.find('div', class_='link')
        if link_div:
            content = link_div.get_text()
            # Encontre todas as URLs que começam com "http://"
            urls = re.findall(r'http://\S+', content)
            all_links.extend(urls)

    return all_links

def navigate_to_next_page(driver):
    # Encontre os números de página clicáveis
    page_numbers = driver.find_elements(By.CSS_SELECTOR, 'a[data-category="pagination"] span.page')

    for page_number in page_numbers:
        page_number.click()
        time.sleep(5)  # Adicione um pequeno atraso para carregar a próxima página

def search_with_selenium(driver, query):
    try:
        search_box = driver.find_element(By.NAME, "query")
    except:
        search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)  # Reduza o tempo de espera para 10 segundos
    driver.implicitly_wait(10)  # Reduza o tempo de espera implícito para 10 segundos

    while True:
        all_links_on_page = extract_links_from_page(driver)
        for link in all_links_on_page:
            print(link)

        # Navegue para a próxima página
        navigate_to_next_page(driver)

        # Verifique se há mais páginas para clicar
        # Se não houver mais números de página clicáveis, saia do loop
        if not page_numbers:
            break

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
    search_with_selenium(driver, search_query)
    time.sleep(10)  # Reduza o tempo de espera para 10 segundos

    driver.quit()
