from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

import warnings
warnings.filterwarnings('ignore')

import re, os
import matplotlib.pyplot as plt
import seaborn as sns



def convert_num(s):
    return int(re.sub('[,억개 ]', '', s).replace('만', '0000'))


def youtube_rank_util(app):

    options = webdriver.ChromeOptions() # 화면없이
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")

    base_url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page='
    driver = webdriver.Chrome('C:/Users/YONSAI/Downloads/chromedriver_win32/chromedriver.exe', options=options)

    lines = []
    for i in range(1, 11):
        driver.get(base_url + str(i))
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        trs = soup.select('.aos-init')

        for tr in trs:
            rank = int(tr.select_one('.rank').get_text().strip())
            category = tr.select_one('.category').get_text().strip()[1:-1]
            channel = tr.select_one('h1 > a').get_text().strip()

            subscriber = convert_num(tr.select_one('.subscriber_cnt').get_text())
            view = convert_num(tr.select_one('.view_cnt').get_text())
            video = convert_num(tr.select_one('.video_cnt').get_text())

            lines.append({'순위':rank, '카테고리':category, '채널': channel, '구독자수': subscriber, '조회수': view, '비디오': video})

    driver.close()

    df = pd.DataFrame(lines)

    filename = os.path.join(app.static_folder, 'data/youtubeRank.csv')
    df.to_csv(filename, index=False)

    return lines

    
def rank_top20(app):
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    filename = os.path.join(app.static_folder, 'data/youtubeRank.csv')

    df = pd.read_csv(filename)
    df_top20 = df.head(20)

    # top20
    filename = os.path.join(app.static_folder, 'data/youtubeRanktop20.png')
    plt.figure(figsize=(10, 8))
    sns.set_palette("muted")
    splot = sns.barplot(x='구독자수', y='채널', data=df_top20)
    plt.title('구독자수 Top20 채널')
    splot.get_figure().savefig(filename, bbox_inches='tight', pad_inches=0.3)

    mtime = int(os.stat(filename).st_mtime)   

    return mtime

# top10
def rank_top10(app):
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    filename = os.path.join(app.static_folder, 'data/youtubeRank.csv')

    df = pd.read_csv(filename)

    df_top10 = df.pivot_table('채널', '카테고리', aggfunc='count').sort_values('채널', ascending=False).head(10)   
    
    filename = os.path.join(app.static_folder, 'data/youtubeRanktop10.png')
    plt.figure(figsize=(10, 6))
    sns.set_palette("colorblind")
    splot = sns.barplot(x='채널', y=df_top10.index, data=df_top10)
    plt.title('카테로리별 채널 top10')
    splot.get_figure().savefig(filename, bbox_inches='tight', pad_inches=0.3)

    mtime = int(os.stat(filename).st_mtime)

    return mtime



