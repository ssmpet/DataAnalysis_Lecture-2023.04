import requests
from bs4 import BeautifulSoup
from datetime import datetime
import numpy as np
import pandas as pd
from selenium import webdriver
import time

import warnings
warnings.filterwarnings('ignore')

import re
def convert_num(s):
    return int(re.sub('[,억개 ]', '', s).replace('만', '0000'))


def youtube_rank_util():

    base_url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page='
    driver = webdriver.Chrome('C:/Users/YONSAI/Downloads/chromedriver_win32/chromedriver.exe')

    lines = []
    for i in range(1, 2):
        driver.get(base_url + str(i))
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        trs = soup.select('.aos-init')

        for tr in trs[:5]:
            rank = int(tr.select_one('.rank').get_text().strip())
            category = tr.select_one('.category').get_text().strip()[1:-1]
            channel = tr.select_one('h1 > a').get_text().strip()

            subscriber = convert_num(tr.select_one('.subscriber_cnt').get_text())
            view = convert_num(tr.select_one('.view_cnt').get_text())
            video = convert_num(tr.select_one('.video_cnt').get_text())

            lines.append({'순위':rank, '카테고리':category, '채널': channel, '구독자수': subscriber, '조회수': view, '비디오': video})

    driver.close()

    return lines

