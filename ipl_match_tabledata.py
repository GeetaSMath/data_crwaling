import requests
from bs4 import BeautifulSoup

url="https://www.iplt20.com/points-table/men"

r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
table=soup.find_all("th")
header=[]
for i in table:
    name=i.text
    header.append(name)
print(header)

























# def get_url(url):
#     try:
#         url_response=requests.get(url)
#         return url_response.text
#     except requests.exceptions.Timeout as timeout_err:
#         print(f"requests time out error: {timeout_err}")
#     except requests.exceptions.RequestException as err:
#         print(f"connection error: {err}")
#
# url_status=get_url(url)
# print(url_status)
#
# if url_status:
#     soup=BeautifulSoup(url_status,'html.parser')

