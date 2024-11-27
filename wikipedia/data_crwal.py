
import requests
from bs4 import BeautifulSoup

base_site="https://en.wikipedia.org/wiki/Music"
url_response=requests.get(base_site)
soup=BeautifulSoup(url_response.text,"html.parser")
param_tag=soup.find_all('p')[1]
print(param_tag.parent.text.strip())
# print(param_tag.text)
# param=[i.text.strip() for i in param_tag]
# print(param)






















