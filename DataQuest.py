import requests
import pandas as pd
from bs4 import BeautifulSoup

print('Requestig. . . . ')
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
#forecast_items = seven_day.find_all(class_="tombstone-container")


period_tag = seven_day.select('.tombstone-container .period-name')
short_dec_tag = seven_day.select('.tombstone-container img')
tem_tag = seven_day.select('.tombstone-container .temp')
period = [pt.get_text() for pt in period_tag]
short_desc = [sd['title'] for sd in short_dec_tag]
tem = [t.get_text() for t in tem_tag]

weather = pd.DataFrame({
    "Period": period,
    "Dhort_Desc": short_desc,
    "Temp": tem
})

print(weather)