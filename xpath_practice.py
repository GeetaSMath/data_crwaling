# import json
#
# from bs4 import BeautifulSoup
# import requests
# from lxml import etree
#
# # Fetch content (use your own URL here)
# url="https://www.hyrtutorials.com/p/add-padding-to-containers.html"
#
#
# response = requests.get(url)
# html_content = response.text
#
# # Parse HTML content with BeautifulSoup
# soup = BeautifulSoup(html_content, "html.parser")
#
# # Use XPath to get the desired text
# tree = etree.HTML(str(soup))  # Convert BeautifulSoup object to lxml object for XPath
#
# text = tree.xpath('//div[@class="container"]//h1/text()')
# text_box=tree.xpath('//div[@class="container"]/label//text()')
#
#
# # Print the extracted text
# if text_box:
#     print(text_box)  # Print the first matching result
# else:
#     print("No match found")
#
# with open("xpathdata.json", "w") as json_file:
#     json.dump(text_box, json_file, indent=4)

import json
import re
import requests
from bs4 import BeautifulSoup
from lxml import etree

url = ("https://www.hyrtutorials.com/p/add-padding-to-containers.html")


# Regex to validate the URL
def is_valid_url(url):
    pattern = r'^https://www.hyrtutorials.com/p/.?'
    return re.match(pattern, url) is not None


# Validate URL before proceeding
if not is_valid_url(url):
    print("Invalid URL format. Exiting...")
else:
    def get_url(url):
        try:
            url_response = requests.get(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/86.0.4240.198 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
            })
            print("Successfully fetched")
            return url_response.text
        except requests.exceptions.ConnectionError as err:
            print(f"Connection error: {err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Request timeout error: {timeout_err}")


    html_content = get_url(url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        tree = etree.HTML(str(soup))


    def extarcted_data(items):
        data = [item.strip() for item in items if isinstance(item, str)]
        return data


    def get_data(tree):
        product_data = {
            "text": extarcted_data(tree.xpath('//div[@class="container"]//h1/text()')),
            "box_text":extarcted_data(tree.xpath('//a[contains(text(),"Sign in into account")]/text()')),
        }
        return product_data


    # Get product data
    product_info = get_data(tree)

    # Write data to JSON file
    with open("xpathdata.json", "w") as json_file:
        json.dump(product_info, json_file, indent=4)

    print("Data has been written to 'amazoninfo.json'.")

