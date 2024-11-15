import json
import re

import requests
from bs4 import BeautifulSoup

url = "https://www.pfizer.com/news/articles/pharma_peers_unite_to_build_dna_encoded_libraries"


def is_valid_url(url):
    pattern = r'^https://www.pfizer.com/news.'
    return re.match(pattern, url) is not None


if not is_valid_url(url):
    print("invalid url")
else:
    def get_url(url):
        try:
            get_respone = requests.get(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/89.0.4389.82 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9", })
            print("fetched successfully")
            return get_respone.text
        except requests.exceptions.ConnectionError as err:
            print(f"connection err:{err}")
        except requests.exceptions.Timeout as errr:
            print(f"time out error occurred: {errr}")


    html_content = get_url(url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")


    def extareced_data(item):
        lst_data = [items.text.strip() for items in item]
        return lst_data


    def get_data(soup):
        data_info = {
            "name": extareced_data(soup.find_all("h1", class_="copy-clipboard h3-styling-article")),
            "text":extareced_data(soup.find_all("div",class_="article-body copy-clipboard")),
            "title":extareced_data(soup.find("a", {"href": "/newsroom"}))
        }

        return data_info


    product_data = get_data(soup)

    with open("fizerdata.json", "w") as json_file:
        json.dump(product_data, json_file,indent=4)
        print("json file created successfully")
