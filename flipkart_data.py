import requests
from bs4 import BeautifulSoup

for i in range(2, 10):
    url = ("https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART"
           "&as-show=on&as=off&page=1") + str(i)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.82 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://www.flipkart.com/",
        "Origin": "https://www.flipkart.com"
    }

    # Use a session to handle cookies
    session = requests.Session()
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

    np = soup.find("a", class_="_9QVEpD").get("href")
    cnp = "https://www.flipkart.com" + np
    print(cnp)

# url = "https://www.flipkart.com/" headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36", "Accept-Language": "en-US,en;q=0.9",
# "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive", }
#
# response = requests.get(url, headers=headers)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     print(soup.prettify())
# else:
#     print(f"Failed to retrieve content: {response.status_code}")
