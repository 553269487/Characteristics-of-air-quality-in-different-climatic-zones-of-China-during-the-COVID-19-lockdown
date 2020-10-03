import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab

path = r'C:\Users\戴启航\Desktop\新冠\Climate zone'
folderlist= os.listdir(path)
path2 = r'C:\Users\戴启航\Desktop\新冠\0.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表

wzy=pd.DataFrame()
dqh=pd.DataFrame()
dl = pd.read_csv(path2, parse_dates=['date'])
dl = dl.drop(['Time', 'hour'], axis=1)
ma = dl.groupby('date').max()
mi = dl.groupby('date').min()
ra = ma - mi
for folder in folderlist:
    inner_path = os.path.join(path,folder)
    folds=os.listdir(inner_path)
    folder_name = os.path.basename(folder)
    i = 0
    for fold in folds:
        files = glob2.glob(os.path.join(inner_path,fold,"*.csv"))
        for f in files:
            file_name = os.path.basename(f)
            file_name = file_name.split('.')[0]
            df=pd.read_csv(f,parse_dates=['date'])
            df=df.drop(['Time','hour'],axis=1)
            df=df.set_index('date')
            df = df.truncate(after='20200124', before='20200101')
            #range
            # max=df.groupby('date').max()
            # min=df.groupby('date').min()
            # ran=max-min
            # range=ran.mean()
            # range['name']=file_name
            # range=range.to_frame().T
            # wzy=wzy.append(range)
            mean=df.mean()
            mean=mean.to_frame().T
            mean['name']=file_name
            wzy=wzy.append(mean)

            i = i + 1
    print(wzy)
wzy.to_csv('allmean.csv',index=False)
