# Import
from bs4 import BeautifulSoup as soup
import requests
# URL from Rogue Canada
URL = 'https://www.roguecanada.ca/weightlifting-bars-plates/bumpers?is_salable[0]=1'
# Grabbing page and narrowing it down to container level
page = requests.get(URL)
page_html = soup(page.content, "html.parser")
containers = page_html.find_all("div", class_="product-details")
# Parsing containers with a loop to print out product name and price
for container in containers:
    name = container.h2.a["title"]
    price = container.span.span.text
    print('Name: ', name)
    print('Price: ', price)