from datetime import datetime, timedelta
import pandas as pd
import requests, json
from pandas import json_normalize
import calendar


def get_calendar():
    today = datetime.now()

    tyear = today.year
    tmon = today.month
    tday = today.day

    # 0이면 월요일, 6이면 일요일이 시작일이다.
    start_day_week, end_day = calendar.monthrange(tyear, tmon)

    # 해당 달의 첫날의 datetime형식으로 변환한다.
    start_date = datetime.strptime(f'{tyear:02d}-{tmon:02d}-01', '%Y-%m-%d')
    end_date = datetime.strptime(f'{tyear:02d}-{tmon:02d}-{end_day:02d}', '%Y-%m-%d')

    lines = []

    #지난 달 
    before_month_day = 0
    if start_day_week < 6:
        before_month_day = (start_date - timedelta(start_day_week+1))

        lines.extend(pd.date_range(before_month_day.strftime('%Y-%m-%d'), periods=start_day_week+1))

    # 현재 달
    lines.extend(pd.date_range(start_date.strftime('%Y-%m-%d'), periods=end_day))

    # 다음 달
    nday = calendar.weekday(tyear, tmon, end_day)
    next_cnt = 0
    if nday == 6: next_cnt = 6
    elif nday < 5: next_cnt = 5 - nday

    # 마지막 날짜 구하기
    lines.extend(pd.date_range((end_date+timedelta(1)).strftime('%Y-%m-%d'), periods=next_cnt))

    l_dt = pd.DataFrame(lines, columns=['locdate'])
    l_dt['day'] = l_dt.locdate.apply(lambda x: int(x.strftime('%d')))
    # l_dt.head()

    # 공휴일, 24절기, 잡절
    with open('static/key/holidays.txt') as f:
        apikey = f.read()

    f_list = ['getRestDeInfo', 'getAnniversaryInfo', 'get24DivisionsInfo', 'getSundryDayInfo']
    base_url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/' #getSundryDayInfo?_type=json&numOfRows=50&solYear='
    param1 = '?_type=json&numOfRows=80&solYear='
    holidays = None
    for name in f_list:
        url = base_url + name + param1 + str(tyear) + '&ServiceKey=' + apikey
        res = ''

        try:
            result = requests.get(url) 
            if result.status_code == 200:
                print('200')
                res = result.text
        except:
            pass

        if res: 
            res = json.loads(res)
            holidays = pd.concat([holidays, json_normalize(res['response']['body']['items']['item'])[['dateKind', 'dateName', 'isHoliday', 'locdate']] ])


    holidays['locdate'] = holidays['locdate'].astype(str)
    holidays['locdate'] = pd.to_datetime(holidays['locdate'], format='%Y%m%d')

    try:
        nindex = holidays.index[holidays.dateName=='기독탄신일'][0]
        holidays.iloc[nindex, 1] = '크리스마스'
    except:
        pass

    result_dt = pd.merge(l_dt, holidays, how='left', on='locdate')
    result_dt.dateKind.fillna('05', inplace=True)
    result_dt.dateName.fillna('', inplace=True)
    result_dt.isHoliday.fillna('N', inplace=True)

    res_list = result_dt.to_dict('records')

    return res_list