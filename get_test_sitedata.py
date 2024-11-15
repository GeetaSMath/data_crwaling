import requests
from bs4 import BeautifulSoup
import json

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"


# Function to fetch HTML content from the URL
def get_url(url):
    try:
        response_url = requests.get(url)
        print("Request was successful.")
        return response_url.text  # Return HTML content
    except requests.exceptions.ConnectionError as conn:
        print(f"Connection error occurred: {conn}")
    except requests.exceptions.Timeout as timeout:
        print(f"Connection timeout error: {timeout}")
    except requests.exceptions.RequestException as err:
        print(f"Any error occurred: {err}")


html_content = get_url(url)
if html_content:
    soup = BeautifulSoup(html_content, "html.parser")


def extract_data(items):
    extracted_data = []
    for item in items:
        extracted_data.append(item.text.strip())  # Extract and strip extra spaces
    return extracted_data


# Function to get all required data
def get_data(soup):
    product_data = {
        "names": extract_data(soup.find_all("a", class_="title")),
        "prices": extract_data(soup.find_all("h4", class_="price float-end card-title pull-right")),
        "review_counts": extract_data(soup.find_all("p", class_="review-count float-end")),
        "descriptions": extract_data(soup.find_all("p", class_="description card-text"))
    }
    return product_data


# Get product data
product_info = get_data(soup)

# Write data to JSON file
with open("product_data.json", "w") as json_file:
    json.dump(product_info, json_file, indent=4)

print("Data has been written to 'product_data.json'.")
