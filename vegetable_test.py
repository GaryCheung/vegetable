from bs4 import BeautifulSoup
from datetime import date,datetime
import datetime
import requests
import pymysql
import time

mysql_config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'19860112',
    'db':'vegetable',
    'charset':'gb2312'
}

present_date = datetime.date.today()
yesterday = present_date + datetime.timedelta(days=-1)

data_info=[1,1,1,1,1,1]

data_info[0] = {
   'goodsname':'',
   'goodstype':'00',
   'beginyear':yesterday.strftime("%Y"),
   'beginmonth':yesterday.strftime("%m"),
   'beginday':yesterday.strftime("%d"),
   'endyear':present_date.strftime("%Y"),
   'endmonth':present_date.strftime("%m"),
   'endday':present_date.strftime("%d")
}

period = present_date.strftime("%Y-%m-%d")
print(period)