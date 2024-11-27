# import json
#
# import requests
# from bs4 import BeautifulSoup
# url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
# r=requests.get(url)
# from bs4 import BeautifulSoup
#
# # Example HTML content
#
#
#
# soup=BeautifulSoup(r.text, "html.parser")
# # Find all <a> tags
# links = soup.find_all('a')
#
# # Extract href attributes
# hrefs = [link['href'] for link in links if link.has_attr('href')]
# print(hrefs.get)
# # boxes=soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
# # # print(boxes)
# # print(len(boxes))
# # names=soup.find_all("a",class_="title")
# # for i in names:
# #     print(i.text)
# #
# # price=soup.find_all("h4",class_="price float-end card-title pull-right")
# # print(len(price))
# # for j in price:
# #     print(j.text)
# #
# # review_count=soup.find_all("p",class_="review-count float-end")
# # for k in review_count:
# #     print(k.text)
#
# # description_item=soup.find_all("p",class_="description card-text")
# # data=[data.text.strip()for data in description_item]
# #
# # with open("product.json", "w") as json_file:
# #     json.dump(data, json_file, indent=4)
# #
# # print("Data has been written to 'product_data.json'.")
#
# # import requests
# # from bs4 import BeautifulSoup
# # import json
# #
# # # URL to scrape
# # url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
# #
# # # Function to fetch HTML content
# # r = requests.get(url)
# # print(r)
# #
# # # Parse HTML with BeautifulSoup
# # soup = BeautifulSoup(r.text, "html.parser")
# #
# # # Extract product names
# # names = soup.find_all("a", class_="title")
# # product_names = [name.text.strip() for name in names]
# #
# # # Extract product prices
# # prices = soup.find_all("h4", class_="price float-end card-title pull-right")
# # product_prices = [price.text.strip() for price in prices]
# #
# # # Extract review counts
# # review_count = soup.find_all("p", class_="review-count float-end")
# # review_counts = [review.text.strip() for review in review_count]
# #
# # # Extract product descriptions
# # description_item = soup.find_all("p", class_="description card-text")
# # product_descriptions = [desc.text.strip() for desc in description_item]
# #
# # # Prepare data for saving
# # product_data = {
# #     "product_names": product_names,
# #     "product_prices": product_prices,
# #     "review_counts": review_counts,
# #     "product_descriptions": product_descriptions
# # }
# #
# # # Write the data to a JSON file
# # with open("product_data.json", "w") as json_file:
# #     json.dump(product_data, json_file, indent=4)
# #
# # print("Data has been written to 'product_data.json'.")
#
#
