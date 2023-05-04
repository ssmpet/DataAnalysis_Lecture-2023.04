import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup

def get_siksin_util(place):
    base_url = "https://www.siksinhot.com/search" 
    url = f'{base_url}?keywords={quote(place)}'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')

    lines = []
    lis = soup.select_one('.localFood_list').find_all('li')

    for li in lis:
        title = li.select_one('.textBox > h2').get_text()
        score  = li.select_one('.textBox > .score').get_text()
        location  = li.select('.cate > a')[0].get_text()
        menu = li.select('.cate > a')[1].get_text()
        img = li.find('img')['src']
        lines.append({'title':title, 'score':score, 'location': location, 'menu': menu, 'img':img} )

    return lines