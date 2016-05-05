from bs4 import BeautifulSoup
from datetime import date,datetime
import datetime
import requests
import pymysql
import time

#windows github test

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


data_info[1] = {
    '__EVENTTARGET':'PriceStaticControl1$nextpage',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'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',
    '__EVENTVALIDATION':'/wEdAAeH4O0YiniOrLNAybjwx4Or4kXHexmHTU3XFH1VXAJoLKE9sXUIGLUYn9CF6aOsrFQY207xRgN32GhpklrIeNb1k9q+Dvz5GhUZi/1U8wQNg6SRIWS4Ty/Jk88HkugWH7zcouhQiaDF9I9OFtqm0AqvNSkLf6vrHob4uAAQAO7+LyoWiwjh6WA1/jV7uGNhUm0=',
    'PriceStaticControl1':'pageno:'
}

data_info[2] = {
    '__EVENTTARGET':'PriceStaticControl1$nextpage',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'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',
    '__EVENTVALIDATION':'/wEdAAemaqfdr+KU14calGVwTVu44kXHexmHTU3XFH1VXAJoLKE9sXUIGLUYn9CF6aOsrFQY207xRgN32GhpklrIeNb1k9q+Dvz5GhUZi/1U8wQNg6SRIWS4Ty/Jk88HkugWH7zcouhQiaDF9I9OFtqm0Aqvr5bob7W4RmAxxvSquVkyphn8N2HQBMLtVhHbHJZadTM=',
    'PriceStaticControl1':'pageno:'
}

data_info[3] = {
    '__EVENTTARGET':'PriceStaticControl1$nextpage',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'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',
    '__EVENTVALIDATION':'/wEdAAcPQBnmDAi7vQNrg41UWmjJ4kXHexmHTU3XFH1VXAJoLKE9sXUIGLUYn9CF6aOsrFQY207xRgN32GhpklrIeNb1k9q+Dvz5GhUZi/1U8wQNg6SRIWS4Ty/Jk88HkugWH7zcouhQiaDF9I9OFtqm0AqvVrM4gMi1YDaH4GwhvB12D6JnM7cGSTdt2NMyzECsuz8=',
    'PriceStaticControl1':'pageno:'
}

data_info[4] = {
    '__EVENTTARGET':'PriceStaticControl1$nextpage',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'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',
    '__EVENTVALIDATION':'/wEdAAfsXk6VipUJXwDLiC+tMcRX4kXHexmHTU3XFH1VXAJoLKE9sXUIGLUYn9CF6aOsrFQY207xRgN32GhpklrIeNb1k9q+Dvz5GhUZi/1U8wQNg6SRIWS4Ty/Jk88HkugWH7zcouhQiaDF9I9OFtqm0Aqvj5Da0gYmG4tpHzZSuEN79FI/0m+7uPk3iZC6Lxg7I30=',
    'PriceStaticControl1':'pageno:'
}

data_info[5] = {
    '__EVENTTARGET':'PriceStaticControl1$nextpage',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'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',
    '__EVENTVALIDATION':'/wEdAAddWF+EII5sFgpyzkaKp73O4kXHexmHTU3XFH1VXAJoLKE9sXUIGLUYn9CF6aOsrFQY207xRgN32GhpklrIeNb1k9q+Dvz5GhUZi/1U8wQNg6SRIWS4Ty/Jk88HkugWH7zcouhQiaDF9I9OFtqm0AqvNjtJQ30Oht3AqLQ9t6EQ2Am31SzErKC6IROU8Q6Ubv0=',
    'PriceStaticControl1':'pageno:'
}

url = 'http://www.shian.gov.cn/web/jghq_static.aspx'
period = present_date.strftime("%Y-%m-%d")

def delete_today_data(config):
    connection = pymysql.connect(**config)
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = "DELETE FROM vegetable WHERE date = '%s'" %(present_date)
            cursor.execute(sql)
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close()
    print('-----------------------delete success!----------------','\n')

def get_page(url,data_num):
    web_data = requests.post(url, data=data_info[data_num])
    web_data.encoding = 'gb2312'
    soup = BeautifulSoup(web_data.text,'lxml')
    vegetable = soup.select('td.dotborder')
    return vegetable

def dump_data(config,vegetable):
    info = ['name',1,1,1]
    i=1
    for vegetables in vegetable:
        if i%4 == 1:
            info[0] = vegetables.get_text()
            i=i+1
        elif i%4 == 2:
            info[1] = vegetables.get_text()
            i=i+1
        elif i%4 == 3:
            info[2] = vegetables.get_text()
            i=i+1
        else:
            info[3] = vegetables.get_text()
            i=i+1
            connection = pymysql.connect(**config)
            try:
                with connection.cursor() as cursor:
                # 执行sql语句，插入记录
                    sql = 'INSERT INTO vegetable (date, vegetable, price_up, price_bottom, price_average, period) VALUES (%s, %s, %s, %s, %s, %s)'
                    cursor.execute(sql, (present_date, info[0], info[1], info[2], info[3], period))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close()

delete_today_data(mysql_config)
print('execute time:-------------------',present_date)

for one in range(1,6):
    vegetable_one = get_page(url,(one-1))
    dump_data(mysql_config,vegetable_one)
    time.sleep(2)
    print(vegetable_one,'\n')
