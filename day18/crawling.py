#crawling . == 웹 사이트에서 정보를 자동으로 가져오는 것
# html 알아야 한다. 웹 브라우저가 읽을 수 있는 파일
import pandas
import requests # 기본 라이브러리 (서버 요청)
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url)
html = response.text


soup = BeautifulSoup(html, 'html.parer')

popular_items = soup.find(id='popularItemList')
list_items = popular_items.find_all('li')
newList = []
for i in list_items:
    newList.append({'회사' : i.find('a').text, '가격': i.find('span').text})
print(newList)

company_list = []
stock_value = []
for i in newList:
    company_list.append(i['회사'])
    stock_value.append(i['가격'])
stockData = {
    '회사' : company_list,
    '가격' : stock_value
}
a = pandas.DataFrame(stockData)
a.to_csv('stock_info_naver.csv', index = False)


# up_tags = popular_items.find_all(class_ = 'up')
# dn_tags = popular_items.find_all(class_ = 'dn')
# name_tage = popular_items.find_all('a')  # a 태그 다 가져오기
#
# print(up_tags)
# print(dn_tags)
# print(name_tage)
