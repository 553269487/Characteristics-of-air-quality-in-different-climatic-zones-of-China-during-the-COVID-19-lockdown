import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab

path2 = r'C:\Users\戴启航\PycharmProjects\f\线性\0air.csv'
path=r'C:\Users\戴启航\Desktop\新冠\air'
folderlist= os.listdir(path)

dqh=pd.DataFrame()

prelock=['20200124','20200101']
level1=['20200226','20200124']
level2=['20200401','20200226']
level3=['20200418','20200401']

def dayave(time1,time2,period):
    wzy = pd.DataFrame()
    for folder in folderlist:
        inner_path = os.path.join(path,folder)
        dl = pd.read_csv(path2, parse_dates=['Time'])
        dl['Time'] = pd.to_datetime(dl[['year', 'month', 'day', 'hour']], unit='s', utc=True)
        dl.drop(['year', 'month', 'day', 'cloud', 'rain0'], axis=1, inplace=True)
        dl = dl.set_index('Time')
        dl = dl.truncate(after=time1, before=time2)
        dl = dl.resample('3h').apply(np.nanmean)
        i = 0
        files = glob.glob(os.path.join(inner_path, "*.csv"))
        for f in files:
            try:
                df = pd.read_csv(f)
                df.replace(-9999, np.nan, inplace=True)
                df.rename(
                    columns={'0': 'year', '1': 'month', '2': 'day', '3': 'hour', '4': 'Temp', '5': 'Dew', '6': 'SeaP',
                             '7': 'WD', '8': 'WS', '9': 'cloud', '10': 'rain0', '11': 'rain6'}, inplace=True)
                df['Time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']], unit='s', utc=True)
                df.drop(['year', 'month', 'day', 'cloud', 'rain0','hour'], axis=1, inplace=True)
                df['Temp'] = df['Temp'] / 10
                df['Dew'] = df['Dew'] / 10
                df['SeaP'] = df['SeaP'] / 10
                df['WS'] = df['WS'] / 10
                df['rain6'] = df['rain6'] / 10
                # print(df)
                try:
                    df.fillna(method='ffill', inplace=True)
                except:
                    df.fillna(method='bfill', inplace=True)
                # print(df)
                df = df.set_index('Time')
                df = df.truncate(after=time1, before=time2)
                df = df.resample('3h').apply(np.nanmean)

                dl = df + dl
                # rainf = df['rain6']/10
                # rainf = rainf.sum()
                # df=df.apply(np.nanmean)
                # dl=dl+df
                # rainl=rainl+rainf
                i = i + 1

            except:
                print('哈哈，我是傻逼')
        folder_name = os.path.basename(folder)
        dl=dl/i
        dl['area']=folder_name
        wzy=wzy.append(dl)
    wzy.index = wzy.index.tz_convert('Asia/Shanghai')
    wzy=wzy.reset_index()
    wzy.hour=wzy.Time.dt.hour
    print(period)
    wzy.to_csv(period+'.csv',index=False)

time=[prelock,level1,level2,level3]
i=0
for t in time:
    time1 = t[0]
    time2 = t[1]
    if i==0:period='pre'
    if i==1:period='level1'
    if i==2:period='level2'
    if i==3:period='level3'
    dayave(time1,time2,period)
    i=i+1
