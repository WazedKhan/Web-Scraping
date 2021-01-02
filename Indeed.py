import requests
from bs4 import BeautifulSoup

print('Collecting Data.......')
page = requests.get('https://au.indeed.com/python-jobs').text
soup = BeautifulSoup(page,'lxml')

n = soup.find(id='p_623883fa31e1c627')
for i in n:
    name = i.find_all('h2',class_='title')
    print(name.text)