import json
from bs4 import BeautifulSoup
import requests
from lxml import etree

# Corrected URL (remove the trailing comma)
url = "https://www.flipkart.com/samsung-galaxy-s23-5g-cream-256-gb/p/itm745d4b532623e?pid=MOBGMFFXURCVYANE&lid=LSTMOBGMFFXURCVYANE4SRNTK&marketplace=FLIPKART&q=mobile+under+50000&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&iid=908752ee-6da9-45eb-9665-36a716e49cc9.MOBGMFFXURCVYANE.SEARCH&ssid=i53ur3omsw0000001732182054877&qH=b8a25b5423fb6bc5"

# Set up headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.flipkart.com/",
    "Origin": "https://www.flipkart.com"
}

response = requests.get(url, headers=headers)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

tree = etree.HTML(str(soup))

text_data = tree.xpath("//span[@class='VU-ZEz']/text()")
print(text_data)
with open("flipkartinfo.json", "w") as json_file:
    json.dump(text_data, json_file)
    print("Data saved to flipkartinfo.json.")
