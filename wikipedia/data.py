from bs4 import BeautifulSoup
import requests
from lxml import etree

# Fetch content (use your own URL here)
url = "https://www.pfizer.com/news/articles/pharma_peers_unite_to_build_dna_encoded_libraries"
response = requests.get(url)
html_content = response.text


# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Use XPath to get the desired text
# Convert BeautifulSoup object to lxml object for XPath
tree = etree.HTML(str(soup))
text = tree.xpath()

# Print the extracted text
if text:
    print(text[0])  # Print the first matching result
else:
    print("No match found")
