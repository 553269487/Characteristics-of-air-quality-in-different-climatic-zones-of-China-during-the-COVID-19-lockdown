import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt

myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')


path = r'C:\Users\戴启航\Desktop\新冠\city'
files = glob2.glob(os.path.join(path, "*.csv"))
list=[]


def getdata(pollution, time1, time2):
    path = r'C:\Users\戴启航\Desktop\新冠\city'
    files = glob2.glob(os.path.join(path, "*.csv"))
    lis = []
    name = []
    value = []
    for f in files:
        df = pd.read_csv(f)
        df.Time = pd.to_datetime(df['Time'])
        df = df.set_index('Time')  # 将date设置为index
        df = df.truncate(after=time1, before=time2)
        file_name = os.path.basename(f)
        file_name = file_name.split('.')[0]
        ave = [file_name, df[pollution].mean(0)]
        lis.append(ave)
        dl = pd.DataFrame(lis)
    return (dl)

prelock=['20200124','20200101']
level1=['20200226','20200124']
level2=['20200401','20200226']
level3=['20200501','20200401']
time=[prelock,level1,level2,level3]
pollutions=['O3','NO2','PM2.5','CO']

for p in pollutions:
    for t in time:
        time1=t[0]
        time2=t[1]
        pollution=p
        dl=getdata(pollution, time1, time2)
        print(t,p,'max:',dl.max(),'min:',dl.min())


# print(df['2020-01'])


# plt.xticks(rotation=10)
# plt.show()

# df['CM'] = df['PM2.5'].expanding(min_periods=4).mean() #cumulative average

# df['PM2.5'] = df['PM2.5'].rolling(window=86).mean()
# print(df.head())
# plt.scatter(df['Time'],df['PM2.5'],c='green',linewidth=1,alpha=0.2,edgecolors='white')
# plt.axvline(x=pd.to_datetime('2020/01/23'))
# plt.legend(prop = myfont)
# plt.xlabel(u"时间", fontproperties = myfont)# plots an axis lable
# plt.ylabel(u"ug/m3", fontproperties = myfont)
# plt.title(u"北京市PM2.5", fontproperties = myfont)
# plt.show()

# print(df[df.isnull().values==True])
