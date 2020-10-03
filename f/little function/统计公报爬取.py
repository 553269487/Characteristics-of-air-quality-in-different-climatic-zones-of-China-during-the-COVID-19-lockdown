from urllib.request import urlopen#用于获取网页
from bs4 import BeautifulSoup#用于解析网页
import requests
import re
import random
import numpy as np
import pandas as pd


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)

        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR!"


'''通过去除标签获取HTML源代码中的正文信息'''


def getRealText(html):
    dre = re.compile(r'<[^>]+>', re.S)
    real_Text = dre.sub('', html)
    '''print(real_Text)'''
    return real_Text

html = urlopen('http://www.tjcn.org/tjgbsy/nd/36163.html')
url='http://www.tjcn.org'
bsObj = BeautifulSoup(html, 'html.parser')
t1 = bsObj.find_all(href=re.compile("/tjgb/+\w"))
i=0
df=pd.DataFrame(columns=('name','GDP'))
for t2 in t1:
    # print(t2)
    t3 = t2.get('href')
    name=t2.get_text()
    link=url+t3
    # print(t3,name,link)
    page=getHTMLText(link)
    text=getRealText(page)
    # GDP=re.findall(r"生产总值(.*?)亿元|生产总值（GDP）(.*?)亿元|生产总值\(GDP\)(.*?)亿元|实现生产总值(.*)亿元|生产总值实现(.*)亿元",text)
    GDP=re.findall(r"生产总值.+(\d+(?:\.\d+)?)亿元",text)
    if GDP:
        print(GDP)
        df=df.append(pd.DataFrame({'name':[name],'GDP':[GDP[0]]}),ignore_index=True)
    else:
        continue

    if df.shape[0] % 20 == 0:
        print(df)
    # if not GDP:
    #     GDP=re.findall(r".*生产总值（GDP）(.*?)亿元，",text)
    # if not GDP:
    #     GDP = re.findall(r".*生产总值\(GDP\)(.*?)亿元，", text)
df.to_csv('GDP.csv')