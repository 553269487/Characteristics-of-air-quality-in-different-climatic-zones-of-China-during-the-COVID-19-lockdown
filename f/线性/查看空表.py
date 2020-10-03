import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False

path = r'C:\Users\戴启航\Desktop\新冠\city'

path2 = r'C:\Users\戴启航\Desktop\新冠\0.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表

files = glob.glob(os.path.join(path, "*.csv"))
for f in files:
    file_name = os.path.basename(f)
    file_name = file_name.split('.')[0]
    df=pd.read_csv(f)
    missing=df.O3.isnull().sum()

    if missing/2616>0.1:
        print(file_name, missing)
    else:
        continue
