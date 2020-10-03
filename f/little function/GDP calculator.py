import re
import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

df=pd.read_csv('GDP.csv')
car=pd.read_csv('car.csv')

eco=df.merge(car,how='outer',on='name')

a=r'\[.*\]'
eco['B']=eco['GDP'].str.replace(a,'')
eco['G'] = eco['B'].str.extract(r'(\d+(?:\.\d+)?)',expand=True)
eco['name']= eco['name'].str.replace('市','')
eco['Z']= eco['name'].str.extract(r'([\u4e00-\u9fa5]{2,12})州',expand=True)
eco['D']=eco['name'].str.extract(r'([\u4e00-\u9fa5]+)地区',expand=True)
#%%
eco=eco[~eco['name'].str.endswith('国')]
eco=eco[~eco['name'].str.endswith('省')]
eco=eco[~eco['name'].str.endswith('自治区')]
print(eco)
# eco['C']=eco['car'].str.extract(r'(\d+(?:\.\d+)?)',expand=True)


eco.loc[eco.Z.notnull(),'name']=eco.loc[eco.Z.notnull(),'Z']
eco.loc[eco.D.notnull(),'name']=eco.loc[eco.D.notnull(),'D']


Zone={}
price={}
wzy=pd.DataFrame()
path = r'C:\Users\戴启航\Desktop\新冠\Climate zone'
folderlist= os.listdir(path)
for folder in folderlist:
    inner_path = os.path.join(path, folder)
    folds = os.listdir(inner_path)
    folder_name = os.path.basename(folder)
    list = []
    for root, dirs, files in os.walk(inner_path):
        list.extend(files)
    dqh=pd.DataFrame(list,columns=['name'])
    dqh['area']=folder_name
    Zone[folder]=list
    wzy=wzy.append(dqh)
    wzy.name=wzy.name.str.replace('.csv','')


new=wzy.merge(eco,how='outer',on='name')

new.to_csv('cor.csv')

