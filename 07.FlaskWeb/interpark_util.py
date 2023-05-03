
import requests
from bs4 import BeautifulSoup

def interpark_util():
    base_url = 'https://book.interpark.com'
    url = "http://book.interpark.com/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, 'html.parser')

    lis = soup.select('.rankBestContentList > ol > li')

    lines = []
    for li in lis:

        rank_data = li.select('.rankBtn_ctrl')

        if len(rank_data) == 1:
            rank = int(rank_data[0]['class'][-1][-1])
        else:
            rank = int(rank_data[0]['class'][-1][-1] + rank_data[-1]['class'][-1][-1])

        title_info = base_url + li.select_one('.coverImage > label > a')['href']
        img = li.select_one('.coverImage > label > a > img')['src']
        title = li.select_one('.itemName').get_text().strip()
        author = li.select_one('.author').get_text().strip()
        company = li.select_one('.company').get_text().strip()
        price = li.select_one('.price > em').get_text().strip()
        lines.append({'순위': rank,  '이미지':img, '제목':title, '저자': author, '출판사': company, '판매가': price, '세부정보': title_info})

    return lines


# book_rank = interpark_util()

# for book in book_rank:
#     print(book['순위'])