import json, requests, folium
from urllib.parse import quote
import matplotlib.pyplot as plt
import os
import pandas as pd


def hot_places(places, app):
    ## 도로명 주소 가져오기
    with open('../04.지도시각화/data/roadapikey.txt') as f:
        road_key = f.read()

    base_url = "https://www.juso.go.kr/addrlink/addrLinkApiJsonp.do"
    params1 = f'confmKey={road_key}&currentPage=1&countPerPage=10'

    address = []
    for place in places:
        params2 = f'keyword={quote(place)}&resultType=json'
        url = f'{base_url}?{params1}&{params2}'
        result = requests.get(url)

        if result.status_code == 200:
            address.append(json.loads(result.text[1:-1])['results']['juso'][0]['roadAddr'])
        else:
            print(result.status_code)
            return False

    ## 카카오에서 위도, 경도 가져오기
    with open('../04.지도시각화/data/kakaoapikey.txt') as f:
        kakao_key = f.read()

    kakao_url = 'https://dapi.kakao.com/v2/local/search/address.json'
    kakao_header = {'Authorization': f'KakaoAK {kakao_key}'}

    lat_list, lng_list = [], []
    for addr in address:
        url = f'{kakao_url}?query={quote(addr)}'
        result = requests.get(url, headers=kakao_header).json()

        lat_list.append(float(result['documents'][0]['y']))
        lng_list.append(float(result['documents'][0]['x']))     


    ## DataFrame 만들기
    df = pd.DataFrame({'장소':places, '주소':address, '위도': lat_list, '경도':lng_list})

    ## 지도 만들기
    g_map = folium.Map(location=[df.위도.mean(), df.경도.mean()], zoom_start=13)

    for i in df.index:
        folium.Marker(
            location=[df.위도[i], df.경도[i]], 
            popup=folium.Popup(df.주소[i], max_width=200),
            tooltip=df.장소[i],
        ).add_to(g_map)

    # title_html = '<h3 align="center" style="font-size:20px;">수원 명소</h3>'
    # g_map.get_root().html.add_child(folium.Element(title_html))

    filename = os.path.join(app.static_folder, 'img/hotpalces.html')
    g_map.save(filename)

    mtime = int(os.stat(filename).st_mtime)   # 마지막으로 변경된 시간

    return mtime
    # return True