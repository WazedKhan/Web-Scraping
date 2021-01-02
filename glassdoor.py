import requests
import urllib
from urllib.request import urlopen
import bs4

url = 'https://www.glassdoor.com/Job/boston-full-stack-engineer-jobs-SRCH_IL.0,6_IC1154532_KO7,26.htm?jl=3188635682&guid=0000016a8432102e99e9b5232325d3d5&pos=102&src=GD_JOB_AD&srs=MY_JOBS&s=58&ao=599212'
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
soup = bs4.BeautifulSoup(urlopen(req),"html.parser")
divliul=soup.body.findAll(['div','li','ul'])
for i in divliul:
    if i.string is not None:
        print(i.string)

