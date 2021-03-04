from bs4 import BeautifulSoup
import requests
import json

def news_search():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; ko-KR))',} #안티 크롤링
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+keyword
    req = requests.get(url.format(keyword))
    soup = BeautifulSoup(req.text, 'html.parser')

    news_dict = {}
    idx = 0
    cur_page = 1

    table = soup.select('#main_pack > section > div > div.group_news > ul > li')
    for i in table:
        news_title = i.find(class_='news_tit').text
        news_href = i.find(class_='news_tit')['href']
        print(news_title)
        print(news_href)

with open('vi_data.json', 'r', encoding='utf-8') as json_result:  # json 파일 load
    json_data = json.load(json_result)
for i in json_data["listDate"]: #json 파일 decoding
    print(i["stk_nm"])
    keyword = i["stk_nm"] #종목명
    news_search()

