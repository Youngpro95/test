from bs4 import BeautifulSoup
import requests,datetime
import json

def news_search():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; ko-KR))',} #안티 크롤링
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+keyword
    req = requests.get(url.format(keyword))
    soup = BeautifulSoup(req.text, 'html.parser')

    news_dict = {}
    data = []

    table = soup.select('#main_pack > section > div > div.group_news > ul > li')
    for i in table:
        news_title = i.find(class_='news_tit').text
        news_href = i.find(class_='news_tit')['href']
        news_time = i.find("span", {"class": "info"}).text
        print(news_title + " " + news_time)
        print(news_href)
        news_dict = {'news_title': news_title, 'news_time': news_time, 'news_href': news_href}
        data.append(news_dict)
        news_dict = {keyword: data}
        with open('news_data.json', 'w', encoding="utf-8") as f:  # json 파일 저장 현재경로에
            json.dump(news_dict, f, ensure_ascii=False, indent="\t")
        with open('news_data.json', 'r', encoding='utf-8') as json_result:  # json 파일 load
            json_data = json.load(json_result)

with open('vi_data.json', 'r', encoding='utf-8') as json_result:  # json 파일 load
    json_data = json.load(json_result)
for i in json_data["listDate"]: #json 파일 decoding
    print(i["stk_nm"])
    keyword = i["stk_nm"] #종목명
    now = datetime.datetime.now()  # 시간
    time_ago = datetime.datetime.now() - datetime.timedelta(seconds = 60)
    time_ago_result = time_ago.strftime('%H:%M:%S')
    nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')
    nowtime = now.strftime('%H:%M:%S')
    test_time = '09:00:03'
    test_val = '%H:%M:%S'
    final_test = now.strptime(nowtime,test_val)- datetime.datetime.strptime(test_time, test_val)
    print(final_test)
    print(nowDate)

    news_search()

