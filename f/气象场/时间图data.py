import pandas as pd

import pandas as pd

import numpy as np
import glob,os
import shutil

path2 = r'C:\Users\戴启航\PycharmProjects\f\线性\0air.csv'

PATH2= r'C:\Users\戴启航\Desktop\新冠\air\YR'
dir=r'C:\Users\戴启航\Desktop\新冠\air'
move= r'C:\Users\戴启航\Desktop\新冠\station\0'



wzy=pd.DataFrame()


folds=os.listdir(dir)
for folder in folds:
    i = 0
    dl = pd.read_csv(path2, parse_dates=['Time'])
    dl.drop(['year', 'month', 'day', 'hour', 'cloud'], axis=1, inplace=True)
    dl = dl.set_index('Time')
    dl = dl.truncate(after='20200418', before='20200101')
    dl = dl.resample('D').mean()
    folder_name=os.path.basename(folder)
    files = glob.glob(os.path.join(dir,folder, '*.csv'))
    for f in files:
        try:
            df=pd.read_csv(f)
            df.replace(-9999, np.nan,inplace=True)
            try:
                df['rain6','rain0'].replace(-1, np.nan,inplace=True)
            except : pass
            df.rename(columns={'0': 'year', '1': 'month', '2': 'day', '3': 'hour', '4': 'Temp', '5': 'Dew', '6': 'SeaP',
                               '7': 'WD', '8': 'WS', '9': 'cloud', '10': 'rain0', '11': 'rain6'}, inplace=True)
            df['Time'] = pd.to_datetime(df[['year', 'month', 'day']])
            df.drop(['year', 'month','day','hour','cloud'], axis=1,inplace=True)
            df['Temp'] = df['Temp'] / 10
            df['Dew'] = df['Dew'] / 10
            df['SeaP'] = df['SeaP'] / 10
            df['WS'] = df['WS'] / 10
            df['rain6'] = df['rain6'] / 10
            df = df.set_index('Time')
            df = df.truncate(after='20200418', before='20200101')
            df = df.resample('D').mean()
            df['rain0']=df['rain0'].resample('D').sum()
            df['rain6']=df['rain6'].resample('D').sum()
            dl=dl+df
            i=i+1

        except:
            file_name = os.path.basename(f)
            file_name = file_name.split('.')[0]
            print(file_name)

    dl=dl/i
    dl['area']=folder_name
    wzy=wzy.append(dl)

print(wzy)
wzy.to_csv('rain6.csv')

