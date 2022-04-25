import requests
import pandas as pd
from bs4 import BeautifulSoup


products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
print('Requestig .....')
source = requests.get('https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi5')
soup = BeautifulSoup(source.content,'html.parser')
print('Looking For info ... .')
info = soup.find_all("div", class_="_2pi5LC col-12-12")
for i in info:
    title = i.find('div', attrs={'class':'_4rR01T'})
    rateing = i.find('div', class_ = '_3LWZlK')
    price = i.find('div', class_= '_30jeq3 _1_WHN1')
    if None in (title, rateing, price):
        continue
    products.append(title.text)
    prices.append(price.text)
    ratings.append(rateing.text)
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
print()
print(df.head)