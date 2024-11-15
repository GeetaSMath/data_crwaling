import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

def get_url(url):
    try:
        response_url = requests.get(url)
        response_url.raise_for_status()  # Check for successful status
        return response_url.text  # Return HTML content
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None

html_content = get_url(url)
if html_content:
    soup = BeautifulSoup(html_content, "html.parser")
    for item in soup.find_all("a", class_="title"):
        print(item.text.strip())
