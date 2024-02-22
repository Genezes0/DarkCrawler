import requests
from bs4 import BeautifulSoup
import socks
import socket
import re
import os
from stem import Signal
from stem.control import Controller
import joblib
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Função para configurar o proxy Tor
def set_tor_proxy():
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket

# Função para obter um novo IP do Tor
def change_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

# Função para realizar a busca em uma página
def search_page(url, search_term):
    set_tor_proxy()
    try:
        options = Options()
        options.headless = True
        profile = webdriver.FirefoxProfile()

        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.socks", "127.0.0.1")
        profile.set_preference("network.proxy.socks_port", 9050)
        profile.set_preference("network.proxy.socks_version", 5)
        profile.set_preference("network.proxy.socks_remote_dns", True)

        options.profile = profile

        driver = webdriver.Firefox(options=options)
        driver.get(url)

        page_source = driver.page_source
        driver.quit()

        if search_term in page_source:
            return page_source
        return None
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return None

# Função para extrair links relevantes de uma página
def extract_links(page, search_term):
    soup = BeautifulSoup(page, 'html.parser')
    result_elements = soup.find_all(class_='result')
    relevant_links = []
    for result_element in result_elements:
        anchor_elements = result_element.find_all('a', href=re.compile("^http://"))
        for anchor in anchor_elements:
            href = anchor.get('href', '')
            if href not in relevant_links:
                relevant_links.append(href)
    return relevant_links

# Função para treinar o modelo de IA
def train_model(X, y):
    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(X)
    clf = SVC(kernel='linear')
    clf.fit(X_vectorized, y)
    joblib.dump(vectorizer, 'vectorizer.pkl')
    joblib.dump(clf, 'classifier.pkl')

# Função para prever relevância com base no modelo de IA
def predict_relevance(X):
    vectorizer = joblib.load('vectorizer.pkl')
    clf = joblib.load('classifier.pkl')
    X_vectorized = vectorizer.transform(X)
    predictions = clf.predict(X_vectorized)
    return predictions

if __name__ == "__main__":
    start_url = "http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion"
    search_term = input("Digite o termo de busca: ")
    max_depth = 5  # Profundidade máxima de rastreamento
    visited_urls = set()
    relevant_links = []

    def recursive_crawler(url, depth):
        if depth <= 0 or url in visited_urls:
            return

        visited_urls.add(url)
        page = search_page(url, search_term)
        if page:
            relevant_links.extend(extract_links(page, search_term))
            change_tor_ip()

        for link in relevant_links:
            recursive_crawler(link, depth - 1)

    recursive_crawler(start_url, max_depth)

    # Treinar o modelo de IA com os links relevantes encontrados
    X = relevant_links
    y = [1] * len(relevant_links)
    train_model(X, y)

    # Prever relevância de novos links
    new_links = ["http://example.onion", "http://another-example.onion", "http://example85jaylokws4rtcgfmf4ffh38kl90fvggghjntdhet547ghj58.onion", "http://example85jaylokws4rtcgfmf4ffh38kl90fvggghjntdhet547ghj58.onion", "http://62uir23lotvhl0u2ow38eqsqdgfoueu58di795u8oivdgh0bs5xbp9l3.onion", "http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/", "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=&DEFAULTOP=and&[=12"]
    predictions = predict_relevance(new_links)
    for link, prediction in zip(new_links, predictions):
        if prediction == 1:
            print(f"O link {link} é relevante.")
        else:
            print(f"O link {link} não é relevante.")
