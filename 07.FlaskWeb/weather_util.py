import requests
import os

def get_weather(app):
    key_file = os.path.join(app.static_folder, 'key/openweather.txt')
    with open(key_file) as f:
        weather_key = f.read()

    base_url  = 'https://api.openweathermap.org/data/2.5/weather'
    icon_deps = 'https://api.openweathermap.org/img/w/'
    lat, lon = 37.295, 127.045  # 수원 중심부 좌표
    url = f'{base_url}?lat={lat}&lon={lon}&appid={weather_key}&units=metric&lang=kr'
    result = requests.get(url).json()

    desc = result['weather'][0]['description']

    icon_code = result['weather'][0]['icon']
    icon_url = f'{icon_deps}{icon_code}.png'

    temp_ = result['main']['temp']
    temp = round(float(temp_) + 0.01, 1)  # 올바르게 반올림 하기 위해서 0.01 해 준다.

    html = f'''<img src="{icon_url}" height="32"><strong>{desc}</strong>
            온도: <strong>{temp}</strong>&#8451'''

    return html