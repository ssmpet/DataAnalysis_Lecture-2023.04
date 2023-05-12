import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd


def melon_util():
    url = 'https://www.melon.com/chart/index.htm'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

    result = requests.get(url, headers=header)

    if result.status_code != 200:
        return []

    soup = BeautifulSoup(result.text, 'html.parser')
    trs = soup.select(' tbody > tr')

    lines = []
    for tr in trs:
        rank = tr.select_one('.rank').get_text().strip()
        img = tr.select_one('img')['src']
        title = tr.select_one('.rank01 > span > a').get_text()
        artist = tr.select_one('.rank02 > a').get_text()
        album = tr.select_one('.rank03 > a').get_text()
        lines.append({'순위': rank, '곡명': title, '아티스트': artist, '앨범': album, '이미지': img})

    return lines