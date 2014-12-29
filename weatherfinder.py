# Weather Finder

import requests, re
from bs4 import BeautifulSoup

def weatherfind():
    #url = "http://www.weather.com/weather/today/l/94513"
    #r = requests.get(url)
    #soup = BeautifulSoup(r.content)
    req = requests.get('http://dsx.weather.com/wxd/v2/MORecord/en_US/(USCA0478:1:US)?api=7bb1c920-7027-4289-9c96-ae5e263980bc')
    data = req.json()
    print(data[0]['doc']['MOData']['tmpF'])
    
(weatherfind())
