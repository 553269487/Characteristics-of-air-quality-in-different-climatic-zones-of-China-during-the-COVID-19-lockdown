import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import shutil
path0= r'C:\Users\戴启航\Desktop\新冠\air\NCP'
path = r'C:\Users\戴启航\Desktop\新冠\NOAA气象数据\noaa测站.csv'
os.chdir(path0)
noaa=pd.read_csv(path)
CH=noaa[noaa['CTRY']=='CH']
files = os.listdir(path0)
NW=[]
NEC=[]
CS=[]
YR=[]
SC=[]
TP=[]
NCP=[]
MG=[]
for i in range(len(CH)):
    if CH.iloc[i]['LON']<108.5:
        name=CH.iloc[i]['USAF']
        MG.append(name)
    elif CH.iloc[i]['LON']<112.7 and CH.iloc[i]['LON']>38.45:
        name=CH.iloc[i]['USAF']
        MG.append(name)
    else: continue

for f in files:
    for name in MG:
        if name in f :
            print("MG" + f)
            if not os.path.exists('MG'):
                os.makedirs('MG')
                shutil.move(f, 'MG')
            else:
                shutil.move(f, 'MG')





# geo_cities_coords = {df.iloc[i]['name']: [df.iloc[i]['lon'], df.iloc[i]['lat']] for i in range(len(df))}