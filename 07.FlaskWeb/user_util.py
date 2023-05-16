import requests, json
import os, random
from urllib.parse import quote 
import numpy as np
import pandas as pd

from PIL import Image

def get_lat_lng(app, addr):

    road_keyfile = os.path.join(app.static_folder, 'key/roadapikey.txt')
    with open(road_keyfile) as f:
        road_key = f.read()

    base_url = "https://www.juso.go.kr/addrlink/addrLinkApiJsonp.do"
    params1 = f'confmKey={road_key}&currentPage=1&countPerPage=10'
    params2 = f'keyword={quote(addr)}&resultType=json'
    url = f'{base_url}?{params1}&{params2}'

    address = ''
    result = requests.get(url)
    if result.status_code == 200:
        res = json.loads(result.text[1:-1])
        address = res['results']['juso'][0]['roadAddr']
    else:
        print(f'result Code : {result.status_code}')    

    kakao_keyfile = os.path.join(app.static_folder, 'key/kakaoapikey.txt')
    with open(kakao_keyfile) as f:
        kakao_key = f.read()

    k_header = {'Authorization': f'KakaoAK {kakao_key}'}
    kakao_url = 'https://dapi.kakao.com/v2/local/search/address.json'
    k_url = f'{kakao_url}?query={quote(address)}'
    result = requests.get(k_url, headers=k_header).json()

    lat = float(result['documents'][0]['y'])
    lng = float(result['documents'][0]['x'])
    # print(lat, lng)

    return lat, lng


def get_weather(app, addr=None):

    if addr:
        lat, lng = get_lat_lng(app, addr)
    else:
        lat, lng = 37.295, 127.045  # 수원 중심부 좌표

    key_file = os.path.join(app.static_folder, 'key/openweather.txt')
    
    with open(key_file) as f:
        weather_key = f.read()

    base_url  = 'https://api.openweathermap.org/data/2.5/weather'
    icon_deps = 'https://api.openweathermap.org/img/w/'
    
    url = f'{base_url}?lat={lat}&lon={lng}&appid={weather_key}&units=metric&lang=kr'
    result = requests.get(url).json()

    desc = result['weather'][0]['description']

    icon_code = result['weather'][0]['icon']
    icon_url = f'{icon_deps}{icon_code}.png'

    temp_ = result['main']['temp']
    temp = round(float(temp_) + 0.01, 1)  # 올바르게 반올림 하기 위해서 0.01 해 준다.

    if addr:
        html = f'''<img src="{icon_url}" height="30">{desc}
            온도: {temp}&#8451'''
    else:
        html = f'''<img src="{icon_url}" height="32"><strong>{desc}</strong>
            온도: <strong>{temp}</strong>&#8451'''

    return html

def get_saying(app):
    filename = os.path.join(app.static_folder, 'data/famousSaying.txt')
    with open(filename, encoding='utf-8') as f:
        says = f.readlines()
 
    # print(random.sample(says, 1)[0])
    return says
    

# Pillow format의 img를 읽어서 중심부의 정사각형 이미지를 Pillow format으로 반환
def center_image(img):
    h, w, _  = np.array(img).shape
    diff = abs(h - w) // 2

    if w > h:   # landscap image 가로가 더 큰 경우
        final_img = np.array(img)[:, diff:diff+h, :]
    else:
        final_img = np.array(img)[diff:diff+w, :, :]

    return Image.fromarray(final_img)


def chg_profile(app, filename):
    img = Image.open(filename)
    new_fname = os.path.join(app.static_folder, 'data/profile.png')
    center_image(img).save(new_fname, format='png')
    return os.stat(new_fname).st_mtime  # 마지막으로 파일이 수정된 시각(int type)
