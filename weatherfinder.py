# Weather Finder

import requests, re
from bs4 import BeautifulSoup

def weatherfind():
    url = "http://www.weather.com/weather/today/l/94513"
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    
    print (temps)
(weatherfind())
