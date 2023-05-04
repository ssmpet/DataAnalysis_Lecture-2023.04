import requests
from bs4 import BeautifulSoup
from datetime import datetime
# import pandas as pd

def get_genie_chart():
    base_url = 'https://www.genie.co.kr/chart/top200?ditc=D'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

    now = datetime.now()
    ymd = now.strftime('%Y%m%d')
    hh = now.strftime('%H')

    lines = []

    for page in range(1, 5):
        url = f'{base_url}&ymd={ymd}&hh={hh}&rtm=Y&pg={page}'
        result = requests.get(url, headers=header)
        soup = BeautifulSoup(result.text, 'html.parser')

        trs = soup.select('tr.list')

        for tr in trs:
            rank = tr.select_one('.number').get_text().split('\n')[0].strip()
            img = 'http:' + tr.select_one('.cover > img')['src']
            title = tr.select_one('.title.ellipsis').get_text().split('\n')[-1].strip()
            artist = tr.select_one('.artist.ellipsis').string.strip()
            album = tr.select_one('.albumtitle.ellipsis').text.strip()
            lines.append({'rank':rank, 'title':title, 'artist':artist, 'album':album, 'img':img})

    return lines
#     df = pd.DataFrame(lines)            
#     print(df.head())



# get_genie_chart()