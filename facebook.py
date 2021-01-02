import requests
from bs4 import BeautifulSoup
from pprint import pprint


page = requests.get('https://www.facebook.com/m.wazedkhan11.01/friends')
soup = BeautifulSoup(page,'lxml')

print(page)