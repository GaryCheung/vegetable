from bs4 import BeautifulSoup
import requests

url = 'http://www.xinnong.net/hangqing/province/shanghai/20410/'
web_data = requests.get(url)
web_data.encoding = 'gb2312'
soup = BeautifulSoup(web_data.text,'lxml')

vegetable = soup.select('body > div.page_main > div.main > div.left > div.plist > table > tr > td > a')



print(vegetable)


