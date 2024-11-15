import json
import re
import requests
from bs4 import BeautifulSoup

url = ("https://www.amazon.in/s?bbn=1375424031&rh=n%3A1375424031%2Cp_n_feature_four_browse-bin%3A7005006031&ref"
       "=mega_elec_s23_2_1_1_3")


# Regex to validate the URL
def is_valid_url(url):
    pattern = r'^https://www\.amazon\.in/s\?'
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


    def extarcted_data(item):
        data = [dec.text.strip() for dec in item]
        return data


    def get_data(soup):
        product_data = {
            "names": extarcted_data(soup.find_all("span", class_="a-size-base-plus a-color-base a-text-normal")),
            "price": extarcted_data(soup.find_all("span", class_="a-price-whole"))
        }
        return product_data


    # Get product data
    product_info = get_data(soup)

    # Write data to JSON file
    with open("amazoninfo.json", "w") as json_file:
        json.dump(product_info, json_file, indent=4)

    print("Data has been written to 'amazoninfo.json'.")
