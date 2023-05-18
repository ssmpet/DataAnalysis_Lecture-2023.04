from datetime import datetime, timedelta
import pandas as pd
import requests, json, os
from pandas import json_normalize
import calendar

# 같은 날은 데이터 추가만
def is_info_day(in_list, s_date, s_datename):

    for i in range(len(in_list)):

        if in_list[i]['locdate'] == s_date:
            in_list[i]['dateName'] = in_list[i]['dateName'] + ' ' + s_datename
            return True
    return False

### 휴일, 기념일 파일로 불러오기
def get_holiday_file(app, tyear):
    
    filename = os.path.join(app.static_folder, f'data/holidays_{tyear}.csv')
    
    try:
        df = pd.read_csv(filename)
        df.locdate = df.locdate.astype(str)
    except:
        return []

    return df

### 휴일, 기념일 공공데이터 api로 불러오기
def call_holidays(app, tyear):
    # 공휴일, 24절기, 잡절
    filename = os.path.join(app.static_folder, 'key/holidays.txt')
    
    with open(filename) as f:
        apikey = f.read()

    f_list = ['getRestDeInfo', 'getAnniversaryInfo', 'get24DivisionsInfo', 'getSundryDayInfo']
    base_url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/'
    param1 = '?_type=json&numOfRows=80&solYear='

    holidays = None
    in_list = []
    for name in f_list:
        url = base_url + name + param1 + str(tyear) + '&ServiceKey=' + apikey
        ress = ''

        try:
            result = requests.get(url) 
            if result.status_code == 200:
                ress = result.text
        except:
            pass

        if ress: 
            ress = json.loads(ress)['response']['body']['items']['item']
        for i in range(len(ress)):
            if is_info_day(in_list, ress[i]['locdate'], ress[i]['dateName']) :
                pass
            else:
                in_list.append(ress[i])

    holidays = pd.DataFrame(in_list)

    holidays.locdate = holidays.locdate.astype(str)
    holidays = holidays[['locdate', 'dateName', 'isHoliday']]

    try:
        nindex = holidays.index[holidays.dateName=='1월1일'][0]
        holidays.iloc[nindex, 1] = '신정'
        nindex = holidays.index[holidays.dateName=='기독탄신일'][0]
        holidays.iloc[nindex, 1] = '크리스마스'
    except:
        pass

    filename = os.path.join(app.static_folder, f'data/holidays_{tyear}.csv')
    holidays.to_csv(filename, index=False)

    return holidays

### 해당 월 정보
def get_calendar(app, cday):
    
    if cday:
        tyear = int(cday.split('.')[0])
        tmon = int(cday.split('.')[1])
    else:
        today = datetime.now()
        tyear = today.year
        tmon = today.month
        # tday = today.day

    holidays = get_holiday_file(app, tyear)
    if len(holidays) == 0:
        holidays = call_holidays(app, tyear)


    # 0이면 월요일, 6이면 일요일이 시작일이다.
    start_day_week, end_day = calendar.monthrange(tyear, tmon)

    # 해당 달의 첫날의 datetime형식으로 변환한다.
    start_date = datetime.strptime(f'{tyear:02d}-{tmon:02d}-01', '%Y-%m-%d')
    end_date = datetime.strptime(f'{tyear:02d}-{tmon:02d}-{end_day:02d}', '%Y-%m-%d')

    lines, opacitys = [], []

    # 지난 달 
    before_month_day = 0
    if start_day_week < 6:
        before_month_day = (start_date - timedelta(start_day_week+1))

        lines.extend([nd.strftime('%Y%m%d') for nd in pd.date_range(before_month_day.strftime('%Y-%m-%d'), periods=start_day_week+1)])
        opacitys = ['0.5' for i in range(start_day_week+1)]

    # 현재 달
    lines.extend([nd.strftime('%Y%m%d') for nd in pd.date_range(start_date.strftime('%Y-%m-%d'), periods=end_day)])
    opacitys.extend(['' for i in range(end_day)])

    # 다음 달
    nday = calendar.weekday(tyear, tmon, end_day)
    next_cnt = 0
    if nday == 6: next_cnt = 6
    elif nday < 5: next_cnt = 5 - nday
    lines.extend([nd.strftime('%Y%m%d') for nd in pd.date_range((end_date+timedelta(1)).strftime('%Y-%m-%d'), periods=next_cnt)])
    opacitys.extend(['0.5' for i in range(next_cnt)])

    ## 
    l_dt = pd.DataFrame({'locdate': lines, 'opacity': opacitys})

    records = pd.merge(l_dt, holidays, how='left', on='locdate')
    records.dateName.fillna('', inplace=True)
    records.isHoliday.fillna('N', inplace=True)

    return records.to_dict('records')
   


