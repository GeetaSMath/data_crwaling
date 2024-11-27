import re
import json

import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/india"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


def is_valid(url):
    pattern = r'^https://timesofindia.indiatimes.com/india'
    return re.match(pattern, url) is not None

if not is_valid(url):
    print("invalid url")
else:
    def get_url(url):
        try:
            get_response = requests.get(url, headers=headers)
            return get_response.text
            print("url response")
        except requests.exceptions.ConnectionError as err:
            print(f"connection error{err}")
        except requests.exceptions.Timeout as timeout:
            print(f'timeout error{timeout}')


    html_content = get_url(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')


    def get_extract(item):
        items = [items.text.strip() for items in item]
        return items


    def get_data(soup):
        a_tag = soup.find_all("a")
        links = [a['href'] for a in a_tag if 'href' in a.attrs]
        print(len(links))
        for link in links:
            print(link)
        info_data = {
            "title": get_extract(soup.find_all("h1", class_="UvAgJ")),
            "text": get_extract(soup.find_all("div", class_="WavNE")),
            "text_tag": get_extract(soup.find_all('a', class_='keyword')),
            "info_data": get_extract(soup.find_all("div", class_="WavNE undefined")),
            "link": link,

        }
        return info_data


    data_info = get_data(soup)

    with open("newsdata.json", "w") as json_file:
        json.dump(data_info, json_file, indent=4)
        print("fetched data")




