import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.monster.com/jobs/search/?q=python&intcid=skr_navigation_nhpso_searchMain&stpage=1&page=1').text

soup = BeautifulSoup(page,'lxml')

job = soup.find_all('h2', string = lambda text: 'python' in text.lower())
for p_job in job:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")