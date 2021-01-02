import requests
from bs4 import BeautifulSoup

page = requests.get('http://pythonjobs.github.io/').text
soup = BeautifulSoup(page,'lxml')

jobs_info = soup.find_all('div',class_='job')

for jobs in jobs_info:
    title = jobs.find('h1')
    info = jobs.find('span',class_='info')
    date_posted = jobs.find('span',class_='info').findNext('span',class_='info').contents[1]
    if None == (title,info.date_posted):
        print('No text found!')
        continue
    print()
    print(f'Title: {title.text.strip()}')
    print(f'Place: {info.text.strip()}')
    print(f'Date of Post: {date_posted.strip()}')
