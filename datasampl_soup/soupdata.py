import json
import re

import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/india"


def is_valid_url(url):
    pattern = r'^https://timesofindia.indiatimes.com/india'
    return re.match(pattern, url) is not None


if not is_valid_url(url):
    print("invalid url")
else:
    def get_url(url):
        try:
            get_response = requests.get(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/89.0.4389.82 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",

            })
            print("fetched url")
            return get_response.text
        except requests.exceptions.ConnectionError as err:
            print(f"connection error{err}")
        except requests.exceptions.Timeout as tmouterr:
            print(f"timeout error{tmouterr}")


    html_content = get_url(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')


    def extracted_data(item):
        data = [items.text.strip() for items in item]
        return data


    def get_data(soup):
        img_tag = soup.find("img")
        print(img_tag)

        # Get the src or data-src attribute
        img_src = img_tag.get("src") or img_tag.get("data-src")
        print(img_src)
        # img_tags = soup.find_all("img")
        #
        # # Extract the 'src' or 'data-src' attribute for each img tag
        # img_links = [img.get("src") or img.get("data-src") for img in img_tags]
        #
        # # Print all the image links
        # for link in img_links:
        #     print(link)

        np_tag = soup.find("a", class_="rxTTw null undefined")
        cnp = None
        if np_tag:
            np = np_tag.get("href")
            cnp = "https://timesofindia.indiatimes.com/" + np if np else None
        data_info = {
            "title": extracted_data(soup.find_all("h1", class_="UvAgJ")),
            "data_info": extracted_data(soup.find_all("div", class_="WavNE")),
            "text": extracted_data(soup.select("h3 span")),
            "img_src":img_src,
            "cnp": cnp

        }
        return data_info


    data_info = get_data(soup)

    with open("newsdata.json", "w") as json_file:
        json.dump(data_info, json_file, indent=4)
        print("fetched data")









