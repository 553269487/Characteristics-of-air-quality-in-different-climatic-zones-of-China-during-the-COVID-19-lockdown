import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt

myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
plt.figure(figsize=(10,5))
plt.style.use('fast')

path = r'C:\Users\戴启航\Desktop\新冠\city'
files = glob2.glob(os.path.join(path, "*.csv"))
print(files)
path2= r'C:\Users\戴启航\Desktop\新冠\北京悲剧.csv'  #因为我不会用字典，所以新建了一个所有值为0的列表
dl = pd.read_csv(path2,encoding = 'gbk')
i=0
for f in files:
    file_name = os.path.basename(f)
    file_name = file_name.split('.')[0]
    df = pd.read_csv(f)