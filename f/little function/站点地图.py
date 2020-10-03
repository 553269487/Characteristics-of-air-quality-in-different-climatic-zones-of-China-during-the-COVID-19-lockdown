import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import shutil
path0= r'C:\Users\戴启航\Desktop\新冠\NOAA气象数据\2020china_csv'
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
    if CH.iloc[i]['LAT']>38.5 and CH.iloc[i]['LON']<105:
        name=CH.iloc[i]['USAF']
        NW.append(name)
    elif CH.iloc[i]['LAT']>43 and CH.iloc[i]['LON']>120:
        name=CH.iloc[i]['USAF']
        NEC.append(name)
    elif CH.iloc[i]['LAT']>38 and CH.iloc[i]['LON']>106 and CH.iloc[i]['LAT']<43 and CH.iloc[i]['LON']<117:
        name=CH.iloc[i]['USAF']
        NCP.append(name)
    elif CH.iloc[i]['LAT']>30 and CH.iloc[i]['LON']>104 and CH.iloc[i]['LAT']<34.75 and CH.iloc[i]['LON']<121:
        name=CH.iloc[i]['USAF']
        YR.append(name)
    elif CH.iloc[i]['LAT']>25 and CH.iloc[i]['LON']>100 and CH.iloc[i]['LAT']<30 and CH.iloc[i]['LON']<120:
        name=CH.iloc[i]['USAF']
        CS.append(name)
    elif CH.iloc[i]['LAT']<25:
        name=CH.iloc[i]['USAF']
        SC.append(name)
    elif CH.iloc[i]['LAT'] > 28.5 and CH.iloc[i]['LON'] > 75.38 and CH.iloc[i]['LAT'] < 37.68 and CH.iloc[i]['LON'] < 100:
        name = CH.iloc[i]['USAF']
        TP.append(name)
    else: continue

for f in files:
    for name in NW:
        if name in f :
            print("NW " + f)
            if not os.path.exists('NW'):
                os.makedirs('NW')
                shutil.copy(f, 'NW')
            else:
                shutil.copy(f, 'NW')
    for name in CS:
        if name in f :
            print("CS " + f)
            if not os.path.exists('CS'):
                os.makedirs('CS')
                shutil.copy(f, 'CS')
            else:
                shutil.copy(f, 'CS')
    for name in SC:
        if name in f :
            print("SC" + f)
            if not os.path.exists('SC'):
                os.makedirs('SC')
                shutil.copy(f, 'SC')
            else:
                shutil.copy(f, 'SC')
    for name in YR:
        if name in f :
            print("YR " + f)
            if not os.path.exists('YR'):
                os.makedirs('YR')
                shutil.copy(f, 'YR')
            else:
                shutil.copy(f, 'YR')

    for name in TP:
        if name in f :
            print("TP" + f)
            if not os.path.exists('TP'):
                os.makedirs('TP')
                shutil.copy(f, 'TP')
            else:
                shutil.copy(f, 'TP')

    for name in NCP:
        if name in f :
            print("NCP" + f)
            if not os.path.exists('NCP'):
                os.makedirs('NCP')
                shutil.copy(f, 'NCP')
            else:
                shutil.copy(f, 'NCP')

    for name in NEC:
        if name in f :
            print("NEC" + f)
            if not os.path.exists('NEC'):
                os.makedirs('NEC')
                shutil.copy(f, 'NEC')
            else:
                shutil.copy(f, 'NEC')




# geo_cities_coords = {df.iloc[i]['name']: [df.iloc[i]['lon'], df.iloc[i]['lat']] for i in range(len(df))}