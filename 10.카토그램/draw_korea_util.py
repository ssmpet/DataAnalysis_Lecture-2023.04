import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False 

# import folium
# import json
import warnings
warnings.filterwarnings('ignore')

BORDER_LINES = [
    [(5, 1), (5, 2), (6, 2), (6, 3), (11, 3), (11, 0)],        # 인천
    [(4, 4), (4, 5), (2, 5), (2, 7), (4, 7), (4, 9), (7, 9),
     (7, 8), (8, 8), (8, 6), (9, 6), (9, 4), (4, 4)], # 서울
    [(1, 7), (1, 8), (3, 8), (3, 10), (10, 10), (10, 7), 
     (12, 7), (12, 6), (11, 6), (11, 5), (12, 5), (12, 4), 
     (11, 4), (11, 3)], # 경기도
    [(8, 10), (8, 11), (6, 11), (6, 12)], # 강원도
    [(12, 5), (13, 5), (13, 4), (14, 4), (14, 5), (15, 5),
     (15, 4), (16, 4), (16, 2)], # 충청북도
    [(16, 4), (17, 4), (17, 5), (16, 5), (16, 6), (19, 6), 
     (19, 5), (20, 5), (20, 4), (21, 4), (21, 3), (19, 3), (19, 1)], # 전라북도
    [(13, 5), (13, 6), (16, 6)], # 대전시
    [(13, 5), (14, 5)], # 세종시
    [(21, 2), (21, 3), (22, 3), (22, 4), (24, 4), (24, 2), (21, 2)], # 광주
    [(20, 5), (21, 5), (21, 6), (23, 6)],   # 전라남도
    [(10, 8), (12, 8), (12, 9), (14, 9), (14, 8), (16, 8), (16, 6)], # 충청북도
    [(14, 9), (14, 11), (14, 12), (13, 12), (13, 13)], # 경상북도
    [(15, 8), (17, 8), (17, 10), (16, 10), (16, 11), (14, 11)], # 대구
    [(17, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10), (21, 10)], # 부산
    [(16, 11), (16, 13)], # 울산
    [(27, 5), (27, 6), (25, 6)]
]

GU_DICT = {
    '수원' : ['장안구', '권선구', '팔달구', '영통구'],
    '성남' : ['수정구', '중원구', '분당구'], 
    '안양' : ['만안구', '동안구'],
    '안산' : ['상록구', '단원구'],
    '고양' : ['덕양구', '일산동구', '일산서구'],
    '용인' : ['처인구', '기흥구', '수지구'], 
    '청주' : ['상당구', '서원구', '흥덕구', '청원구'],
    '천안' : ['동남구', '서북구'],
    '전주' : ['완산구', '덕진구'],
    '포항' : ['남구', '북구'],
    '창원' : ['의창구', '성산구', '진해구', '마산합포구', '마산회원구']
    }


def get_guname(g_name, s_name):

    
    
    si_name = [None] * len(g_name)
    for n in range(len(g_name)):
        if g_name[n][-3:] not in ['광역시', '특별시', '자치시']:
            if s_name[n][:-1] == '고성' and g_name[n] == '강원도':
                si_name[n] = '고성(강원)'
            elif s_name[n][:-1] == '고성' and g_name[n] == '경상남도':
                si_name[n] = '고성(경남)'
            else:
                si_name[n] = s_name[n][:-1]
            
            for key, values in GU_DICT.items():
                if s_name[n] in values:
                    if len(s_name[n]) == 2:
                        si_name[n] = key + ' ' + s_name[n]
                    elif s_name[n] in ['마산합포구', '마산회원구']:
                        si_name[n] = key + ' ' + s_name[n][2:-1]
                    else:
                        si_name[n] = key + ' ' + s_name[n][:-1]

        elif g_name[n] == '세종특별자치시':
            si_name[n] = '세종'

        else:
            if len(s_name[n]) == 2:
                si_name[n] = g_name[n][:2] + ' ' + s_name[n]
            else:
                si_name[n] = g_name[n][:2] + ' ' + s_name[n][:-1]

    return si_name



def draw_korea_map(target_data, blocked_map, cmapname):
    gamma = 0.75

    whitelabelmin = (max(blocked_map[target_data]) -
                     min(blocked_map[target_data])) * 0.25 + \
                     min(blocked_map[target_data])
    datalabel = target_data
    vmin = min(blocked_map[target_data])
    vmax = max(blocked_map[target_data])

    mapdata= blocked_map.pivot_table(index='y', columns='x', values=target_data)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

    plt.figure(figsize=(9, 11))
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname,
               edgecolor='#aaaaaa', linewidth=0.5)
    
    # 지역 이름 표시
    for idx, row in blocked_map.iterrows():
        if len(row['ID'].split()) == 2:
            dispname = f"{row['ID'].split()[0]}\n{row['ID'].split()[1]}"
        elif row['ID'][:2] == '고성':
            dispname = '고성'
        else:
            dispname = row['ID']

        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 10.0, 1.1
        else:
            fontsize, linespacing = 11, 1.

        annocolor = 'white' if row[target_data] > whitelabelmin else 'black'
        plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=2)
    
    plt.gca().invert_yaxis()

    plt.axis('off')
    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)

    plt.tight_layout()
    plt.show()


get_guname([], [])