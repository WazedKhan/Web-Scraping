import requests
from bs4 import BeautifulSoup

print('Collecting Data.......')
page = requests.get('https://remote.co/remote-jobs/developer/').text
soup = BeautifulSoup(page,'lxml')
jobs_elems = soup.find_all('div',class_='card border-0 p-3 job-card bg-white')


for jobs in jobs_elems:
    Name = jobs.find('span',class_='font-weight-bold larger')
    time = jobs.find('span',class_='float-right d-none d-md-inline text-secondary')
    company =jobs.find('p',class_='m-0 text-secondary')
    #company_type = jobs.find('small',class_='badge badge-success')
    print(Name.text.strip())
    print(f'Posted: {time.text.strip()}')
    com = company.text.strip().split()
    print('Company Info: ', end='')
    [print(c,end=' ') for c in com]
    print()
    print('---------------------------------------------')