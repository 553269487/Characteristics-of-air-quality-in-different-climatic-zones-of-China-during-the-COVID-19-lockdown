import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator, FuncFormatter

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False
Path0=r'C:\Users\戴启航\Desktop\新冠\Climate zone'
path2 = r'C:\Users\戴启航\Desktop\新冠\0.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表
Path1=r'C:\Users\戴启航\Desktop\新冠\Tier'

def trendzone(pollution):

    for fold in os.listdir(Path0):
        path = os.path.join(Path0, fold)
        folderlist= os.listdir(path)
        fold_name = os.path.basename(fold)
        for folder in folderlist:
            inner_path = os.path.join(path, folder)
            files = glob.glob(os.path.join(inner_path, "*.csv"))
            dl = pd.read_csv(path2, encoding='gbk')
            dl['Time'] = pd.to_datetime(dl['Time'])
            dl = dl.set_index('Time').resample('D').mean()
            i=1
            for f in files:
                df = pd.read_csv(f)
                df['Time'] = pd.to_datetime(df['Time'])
                df = df.set_index('Time').resample('D').mean()
                dl.iloc[:,2:18] = dl.iloc[:,2:18]+df.iloc[:,2:18]# 每个列表时间是一样的，我尝试用循环把PM25的值加起来，求多个城市的平均，但是dl的长度为0所以不能相加？
                i = i + 1
            folder_name = os.path.basename(folder)
            dl[pollution] = dl[pollution] / i
            # dl['CO'] = dl['CO'].rolling(window=20).mean()#rolling average
            plt.plot(df.index, dl[pollution], label=folder_name)
        plt.legend()
        plt.axvline(x=pd.to_datetime('2020/01/23'))
        plt.axvline(x=pd.to_datetime('2020/02/25'))
        plt.axvline(x=pd.to_datetime('2020/03/31'))

        plt.xlabel(u"时间")  # plots an axis lable
        plt.ylabel(u"ug/m3")
        plt.title(fold_name+' '+pollution+' '+'timetrend')
        # plt.savefig(r'C:\Users\戴启航\Desktop\新冠\图\zone\''+ fold_name+' '+pollution+' '+'timetrend'+'.png')
        plt.show()

def trendtier(pollution):
    for fold in os.listdir(Path1):
        path = os.path.join(Path1, fold)
        plt.figure(figsize=(10, 5))
        plt.style.use('fast')
        folderlist= os.listdir(path)
        fold_name = os.path.basename(fold)
        for folder in folderlist:

            inner_path = os.path.join(path, folder)
            files = glob.glob(os.path.join(inner_path, "*.csv"))
            dl = pd.read_csv(path2, encoding='gbk')
            dl['Time'] = pd.to_datetime(dl['Time'])
            dl = dl.set_index('Time').resample('D').mean()
            i = 0
            for f in files:
                df = pd.read_csv(f)
                df['Time'] = pd.to_datetime(df['Time'])
                df = df.set_index('Time').resample('D').mean()
                dl.iloc[:,2:18] = dl.iloc[:,2:18]+df.iloc[:,2:18] # 每个列表时间是一样的，我尝试用循环把PM25的值加起来，求多个城市的平均，但是dl的长度为0所以不能相加？
                i = i + 1
                # file_name = os.path.basename(f)
                # file_name = file_name.split('.')[0]
                # plt.plot(df['Time'],df['CO'],label= file_name)
            folder_name = os.path.basename(folder)
            dl[pollution] = dl[pollution] / i
            # dl['CO'] = dl['CO'].rolling(window=20).mean()#rolling average
            plt.plot(df.index, dl[pollution], label=folder_name)
        plt.legend()
        plt.axvline(x=pd.to_datetime('2020/01/23'))
        plt.axvline(x=pd.to_datetime('2020/02/25'))
        plt.axvline(x=pd.to_datetime('2020/03/31'))

        plt.xlabel(u"时间")  # plots an axis lable
        plt.ylabel(u"ug/m3")
        plt.title(fold_name+' '+pollution+' '+'timetrend')
        # plt.savefig(r'C:\Users\戴启航\Desktop\新冠\图\Tier\''+fold_name+' '+pollution+' '+'timetrend'+'.png')
        plt.show()

pollutions=['SO2','PM10','O3','NO2','PM2.5','CO']
for p in pollutions:
    trendzone(p)
    trendtier(p)
