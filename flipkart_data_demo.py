import requests
from bs4 import BeautifulSoup

# Define the base URL without the page number
base_url = ("https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace"
            "=FLIPKART&as-show=on&as=off&page=")

# Headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.flipkart.com/",
    "Origin": "https://www.flipkart.com"
}

# Loop over page numbers
for i in range(2, 10):  # Starting from page 2 to page 9
    # Correctly format the URL with the page number
    url = base_url + str(i)

    # Use a session to handle cookies
    session = requests.Session()
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Attempt to find the link and check if it's present
        np_tag = soup.find("a", class_="_9QVEpD")
        if np_tag:
            np = np_tag.get("href")
            cnp = "https://www.flipkart.com" + np
            print(f"Page {i} link:", cnp)
        else:
            print(f"Element with class '_9QVEpD' not found on page {i}.")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
