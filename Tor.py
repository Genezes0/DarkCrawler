"""
MIT License

Copyright (c) 2020 adnane tebbaa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import sys
import time
import requests
import asyncio
from proxybroker import Broker
from termcolor import colored, cprint
from bs4 import BeautifulSoup , SoupStrainer
from urllib.request import urlparse, urljoin
import re

T = """

  _____
 |_   _|__  _ __
   | |/ _ \| '__| Katana-ds V1.5.3
   | | (_) | |    Tor Mode
   |_|\___/|_|   
             
    """
print(T)
print(colored('[!] Tor proxy must be on port 9050 ', 'yellow' )) 
print(colored('[+] Checking TOR... ', 'green' )) 
#search launch**

session = requests.session()
session.proxies = {'http':  'socks5h://localhost:9050',
                   'https': 'socks5h://localhost:9050'}
print(session.get('http://httpbin.org/ip').text) 
print(colored('[+] Got session... ', 'green' ))
###################################################################################################### 
print ("") 
xquery = input ("Please set your query : ") 



#####
##### OnionLand
#####
print ("")
print(colored('[+] Searching in "FindTor" http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion  ', 'green' ))
session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=1")
page = session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=1")
soup = BeautifulSoup(page.text, 'html.parser')
main_tag = soup.find('main', class_='results')
if main_tag:
    link_elements = main_tag.find_all('a', href=True)
for link_element in link_elements:
    link = link_element['href']
    if link.startswith('http://'):
        print(link)
session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=2")
page = session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=2")
soup = BeautifulSoup(page.text, 'html.parser')
main_tag = soup.find('main', class_='results')
if main_tag:
    link_elements = main_tag.find_all('a', href=True)
for link_element in link_elements:
    link = link_element['href']
    if link.startswith('http://'):
        print(link)
session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=3")
page = session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=3")
soup = BeautifulSoup(page.text, 'html.parser')
main_tag = soup.find('main', class_='results')
if main_tag:
    link_elements = main_tag.find_all('a', href=True)
for link_element in link_elements:
    link = link_element['href']
    if link.startswith('http://'):
        print(link)
session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=4")
page = session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=4")
soup = BeautifulSoup(page.text, 'html.parser')
main_tag = soup.find('main', class_='results')
if main_tag:
    link_elements = main_tag.find_all('a', href=True)
for link_element in link_elements:
    link = link_element['href']
    if link.startswith('http://'):
        print(link)
session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=5")
page = session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=5")
soup = BeautifulSoup(page.text, 'html.parser')
main_tag = soup.find('main', class_='results')
if main_tag:
    link_elements = main_tag.find_all('a', href=True)
for link_element in link_elements:
    link = link_element['href']
    if link.startswith('http://'):
        print(link)
session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=6")
page = session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=6")
soup = BeautifulSoup(page.text, 'html.parser')
main_tag = soup.find('main', class_='results')
if main_tag:
    link_elements = main_tag.find_all('a', href=True)
for link_element in link_elements:
    link = link_element['href']
    if link.startswith('http://'):
        print(link)
session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=7")
page = session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=7")
soup = BeautifulSoup(page.text, 'html.parser')
main_tag = soup.find('main', class_='results')
if main_tag:
    link_elements = main_tag.find_all('a', href=True)
for link_element in link_elements:
    link = link_element['href']
    if link.startswith('http://'):
        print(link)
session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=8")
page = session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=8")
soup = BeautifulSoup(page.text, 'html.parser')
main_tag = soup.find('main', class_='results')
if main_tag:
    link_elements = main_tag.find_all('a', href=True)
for link_element in link_elements:
    link = link_element['href']
    if link.startswith('http://'):
        print(link)
session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=9")
page = session.get("http://findtorroveq5wdnipkaojfpqulxnkhblymc7aramjzajcvpptd4rjqd.onion/search?q=" + xquery + "&page=9")
soup = BeautifulSoup(page.text, 'html.parser')
main_tag = soup.find('main', class_='results')
if main_tag:
    link_elements = main_tag.find_all('a', href=True)
for link_element in link_elements:
    link = link_element['href']
    if link.startswith('http://'):
        print(link)
print(colored('[+] Done from FindTor', 'yellow' ))



print ("")  
#####
##### TOrdex
##### 
print(colored('[+] Searching in "Tordex" http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion  ', 'green' )) 
session.get("http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion/search?query=" + xquery)
page = session.get("http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion/search?query=" + xquery)
soup = BeautifulSoup(page.text, 'html.parser')
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
print(colored('[+] Done from Tordex', 'yellow'))
######
###### SenTor
######
url_base = "http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/?q=" + xquery + "&p={}"
print(colored('[+] Searching in "SenTor" ' + url_base.format(1), 'green'))
all_links = set()
for page_number in range(1, 21):
    url = url_base.format(page_number)
    response = session.get(url)
    if response.status_code != 200:
        print("Erro ao obter a página:", url)
        continue
    soup = BeautifulSoup(response.text, 'html.parser')
    result_elements = soup.find_all(class_='result')
    for result_element in result_elements:
        anchor_elements = result_element.find_all('a', href=re.compile("^http://"))
        for anchor in anchor_elements:
            href = anchor.get('href', '')
            all_links.add(href)
# Imprime os resultados únicos
for href in all_links:
    print(href)
print(colored('[+] Done from SenTor', 'yellow' ))
#####
##### AHMIA
#####
print(colored('[+] Searching in "AHMIA" http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/ ', 'green' )) 
session.get("http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q=" + xquery)
page = session.get("http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q=" + xquery)
soup = BeautifulSoup(page.text, 'html.parser')
cite_elements = soup.find_all('cite')
for cite in cite_elements:
    print(cite.get_text())
print(colored('[+] Done from Ahmia', 'yellow' ))
#####
##### Torch 
#####
print(colored('[+] Searching in "Torch" http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion ', 'green' )) 
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=1")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=1")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=2")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=2")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=3")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=3")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=4")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=4")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=5")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=5")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=6")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=6")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=7")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=7")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=8")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=8")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=9")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=9")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=10")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=10")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=11")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=11")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=12")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=12")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=13")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=13")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=14")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=14")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=15")
page = session.get("http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=" + xquery + "&DEFAULTOP=and&[=15")
soup = BeautifulSoup(page.text, 'html.parser')
a_elements = soup.find_all('a', href=lambda href: href and href.startswith('http://'))
unique_links = set()
for a_element in a_elements:
    href = a_element.get('href')
    if href:
      unique_links.add(href)
for link in unique_links:
  print(link)
print(colored('[+] Done from Torch', 'yellow' ))
#####
##### Haystak
#####
print(colored('[+] Searching in "Haystak" http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion ', 'green' )) 
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=1")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=1")
soup = BeautifulSoup(page.text, 'html.parser')
i_elements = soup.find_all('i')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=2")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=2")
soup = BeautifulSoup(page.text, 'html.parser')
i_elements = soup.find_all('i')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=3")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=3")
soup = BeautifulSoup(page.text, 'html.parser')
i_elements = soup.find_all('i')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=4")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=4")
soup = BeautifulSoup(page.text, 'html.parser')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=5")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=5")
soup = BeautifulSoup(page.text, 'html.parser')
i_elements = soup.find_all('i')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=test" + xquery + "&offset=6")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=test" + xquery + "&offset=6")
soup = BeautifulSoup(page.text, 'html.parser')
i_elements = soup.find_all('i')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=7")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=7")
soup = BeautifulSoup(page.text, 'html.parser')
i_elements = soup.find_all('i')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=8")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=8")
soup = BeautifulSoup(page.text, 'html.parser')
i_elements = soup.find_all('i')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=9")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=9")
soup = BeautifulSoup(page.text, 'html.parser')
i_elements = soup.find_all('i')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=10")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=10")
soup = BeautifulSoup(page.text, 'html.parser')
i_elements = soup.find_all('i')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=11")
page = session.get("http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=" + xquery + "&offset=11")
soup = BeautifulSoup(page.text, 'html.parser')
i_elements = soup.find_all('i')
unique_links = set()
for i_element in i_elements:
  if i_element.text.startswith('http://'):
    unique_links.add(i_element.text)
for link in unique_links:
  print(link)
print(colored('[+] Done from Haystak', 'yellow' ))
#####
##### Submarine
#####
print(colored('[+] Searching in "Submarine" http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion ', 'green' )) 
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=1")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=1")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=2")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=2")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=3")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=3")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=4")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=4")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=5")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=5")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=6")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=6")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=7")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=7")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=8")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=8")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=9")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=9")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=10")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=10")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=11")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=11")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=12")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=12")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=13")
page = session.get("http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=" + xquery + "&page=13")
soup = BeautifulSoup(page.text, 'html.parser')
list_elements = soup.find_all(class_='list')
href_values = set()  # Use a set to store unique href values
for list_element in list_elements:
    href = list_element.text.strip()
    if href.startswith('http://'):
        href_values.add(href)
for href in href_values:
    print(href)
print(colored('[+] Done from Submarine', 'yellow' ))

