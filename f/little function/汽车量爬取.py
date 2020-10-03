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
df=pd.DataFrame()
onepage=[]
for t2 in t1:
    t3 = t2.get('href')
    name=t2.get_text()
    #search from second page
    t3=t3[:-5]
    link=url+t3+'_2.html'
    #search from first page
    # link=url+t3
    # print(t3,name,link)
    page=getHTMLText(link)
    text=getRealText(page)
    # print(text)
    car=re.findall(r"私人汽车[\u4e00-\u9fa5]*(\d+(?:\.\d+)?)万辆.*", text)

    if car:
        print(name,car,'一次就行')
    else:
        while not car:
            try:
                before=link
                ll= urlopen(link)
                pp = BeautifulSoup(ll, 'html.parser')
                l = pp.find_all('a', href=True, text='下一页')

                for a in l:
                    link = url + a['href']
                if before == link:break
                page = getHTMLText(link)
                text = getRealText(page)
                # car = re.findall(r"民用[\u4e00-\u9fa5]+(-?\d+\.?\d*e?-?\d*?)万辆", text)
                car = re.findall(r"私人汽车[\u4e00-\u9fa5]+(\d+(?:\.\d+)?)万辆", text)
                if len(car)==0:
                    car = re.findall(r"个人[\u4e00-\u9fa5]*(\d+(?:\.\d+)?)万辆", text)
                if len(car)==0:
                    car = re.findall(r".+私家[\u4e00-\u9fa5]*(\d+(?:\.\d+)?)万辆", text)
                if not len(car)==0:
                    print(name,car,'翻页匹配')
                print(link)
            except:
                onepage.append(name)
                break

    if car:
        df=df.append(pd.DataFrame({'name':[name],'car':[car[0]]}),ignore_index=True)
    else:
        print(name,'unfind')
    if df.shape[0] % 20 == 0:
        print(df)

onepage=pd.DataFrame(onepage)
df.to_csv('car.csv')
onepage.to_excel('只有一页的.xlsx')