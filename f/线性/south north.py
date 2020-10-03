import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt

myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
plt.figure(figsize=(10,5))
plt.style.use('fast')

path = r'C:\Users\戴启航\Desktop\新冠\一线\一线城市北部'
files = glob2.glob(os.path.join(path, "*.csv"))
print(files)
path2= r'C:\Users\戴启航\Desktop\新冠\北京悲剧.csv'  #因为我不会用字典，所以新建了一个所有值为0的列表
dl = pd.read_csv(path2,encoding = 'gbk')
i=0
for f in files:
    df=pd.read_csv(f)
    df['Time'] = df.date.map(str) + df.hour.map(str)
    df['Time'] = pd.to_datetime(df['Time'], format='%Y%m%d%H')
    dl['CO'] = dl['CO']+df['CO'] #每个列表时间是一样的，我尝试用循环把PM25的值加起来，求多个城市的平均，但是dl的长度为0所以不能相加？
    i=i+1
    # file_name = os.path.basename(f)
    # file_name = file_name.split('.')[0]
    # plt.plot(df['Time'],df['CO'],label= file_name)
dl['CO']= dl['CO']/i
dl['CO'] = dl['CO'].rolling(window=20).mean()
print(dl['CO'].head())
plt.plot(df['Time'],dl['CO'],label='北部')

path = r'C:\Users\戴启航\Desktop\新冠\一线\一线南部'
files = glob2.glob(os.path.join(path, "*.csv"))
print(files)
path2= r'C:\Users\戴启航\Desktop\新冠\北京悲剧.csv'  #因为我不会用字典，所以新建了一个所有值为0的列表
dl = pd.read_csv(path2,encoding = 'gbk')
i=0
for f in files:
    df=pd.read_csv(f)
    df['Time'] = df.date.map(str) + df.hour.map(str)
    df['Time'] = pd.to_datetime(df['Time'], format='%Y%m%d%H')
    dl['CO'] = dl['CO']+df['CO'] #每个列表时间是一样的，我尝试用循环把PM25的值加起来，求多个城市的平均，但是dl的长度为0所以不能相加？
    i=i+1
    # file_name = os.path.basename(f)
    # file_name = file_name.split('.')[0]
    # plt.plot(df['Time'],df['CO'],label= file_name)
dl['CO']= dl['CO']/i
dl['CO'] = dl['CO'].rolling(window=20).mean()
print(dl['CO'].head())
plt.plot(df['Time'],dl['CO'],label='南部')

plt.legend(prop = myfont)
plt.xlabel(u"时间", fontproperties = myfont)# plots an axis lable
plt.ylabel(u"ug/m3", fontproperties = myfont)
plt.title(u"一线城市CO平均浓度", fontproperties = myfont)
plt.savefig(r'C:\Users\戴启航\Desktop\新冠\一线\一线图\'CO南北.png')
# plt.show()


