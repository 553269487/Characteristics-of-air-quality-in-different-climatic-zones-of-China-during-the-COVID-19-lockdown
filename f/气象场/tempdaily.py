import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab
params={
    'axes.labelsize': '12',
    'xtick.labelsize':'12',
    'ytick.labelsize':'12',
    'lines.linewidth':1.5,
    'legend.fontsize': '12',
    'figure.figsize' : '10, 20'
}
pylab.rcParams.update(params)


path2 = r'C:\Users\戴启航\PycharmProjects\f\线性\0air.csv'
path = r'C:\Users\戴启航\Desktop\新冠\station.csv'
PATH2= r'C:\Users\戴启航\Desktop\新冠\air\PR'
move= r'C:\Users\戴启航\Desktop\新冠\station\0'
files=glob.glob(os.path.join(PATH2,'*.csv'))
dl=pd.read_csv(path2,parse_dates=['Time'])
dl['Time'] = pd.to_datetime(dl[['year', 'month', 'day', 'hour']])
dl.drop(['year', 'month', 'day','cloud','rain0'], axis=1, inplace=True)
dl = dl.set_index('Time')
dl = dl.truncate(after='20200418', before='20200101')
dl=dl.resample('6h').apply(np.nanmean)
# rainl=dl['rain6'].sum()
# dl=dl.apply(np.nanmean)


i=1
for f in files:
    try:
        df=pd.read_csv(f)
        df.replace(-9999, None,inplace=True)
        df.rename(columns={'0': 'year', '1': 'month', '2': 'day', '3': 'hour', '4': 'Temp', '5': 'Dew', '6': 'SeaP',
                           '7': 'WD', '8': 'WS', '9': 'cloud', '10': 'rain0', '11': 'rain6'}, inplace=True)
        df['Time'] = pd.to_datetime(df[['year', 'month', 'day','hour']])
        df.drop(['year', 'month','day','cloud','rain0'], axis=1,inplace=True)
        df['Temp'] = df['Temp'] / 10
        df['Dew'] = df['Dew'] / 10
        df['SeaP'] = df['SeaP'] / 10
        df['WS'] = df['WS'] / 10
        df.replace(-9999,np.nan,inplace=True)
        df = df.set_index('Time')
        df = df.truncate(after='20200418', before='20200101')
        df = df.resample('6h').apply(np.nanmean)
        dl = df+dl
        # rainf = df['rain6']/10
        # rainf = rainf.sum()
        # df=df.apply(np.nanmean)
        # dl=dl+df
        # rainl=rainl+rainf
        i=i+1

    except:
        file_name = os.path.basename(f)
        file_name = file_name.split('.')[0]
        print(file_name)

dl=dl/i
print(dl)
# dl.hour=dl['Time'].dt.hour
# print(dl.iloc[5]['hour'])
# print(dl)
# ax = sns.lineplot(x='hour',y='Temp',data=dl,markers='.')
#
# plt.show()
