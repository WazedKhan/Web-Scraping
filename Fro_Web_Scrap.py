import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://www.hubertiming.com/results/2017GPTR10K')
soup = BeautifulSoup(page.content,'lxml')
data_row = []

rows = soup.find_all('tr')
    
for row in rows:
    row_td = row.find_all('td')
    for data in row_td:
        if data == None:
            continue
        print(data.text)
    print('End of td')