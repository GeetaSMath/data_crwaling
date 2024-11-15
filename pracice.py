import json
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones"


def get_url(url):
    try:
        url_response = requests.get(url)
        print("request was successful")
        return url_response.text
    except requests.exceptions.ConnectionError as err:
        print(f"connection error: {err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"time out error: {timeout_err}")


html_content = get_url(url)
if html_content:
    soup = BeautifulSoup(html_content, "html.parser")


def extract_data(items):
    extracted_data = []
    for item in items:
        extracted_data.append(item.text.strip())  # Extract and strip extra spaces
    return extracted_data


def get_data(soup):
    product_data = {
        "names": extract_data(soup.find_all("a", class_="title")),
        "rate": extract_data(soup.find_all("h4", class_="price float-end card-title pull-right"))

    }
    return product_data


# Get product data
product_info = get_data(soup)

# Write data to JSON file
with open("product_data1.json", "w") as json_file:
    json.dump(product_info, json_file, indent=4)
print("Data has been written to 'product_data1.json'.")
