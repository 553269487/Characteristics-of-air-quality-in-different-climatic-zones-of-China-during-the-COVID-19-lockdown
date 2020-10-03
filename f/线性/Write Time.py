import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt


path = r'C:\Users\戴启航\Desktop\新冠\first'
folderlists = os.listdir(path)

for folder in folderlists:
    path2= os.path.join(path,folder)
    files = glob2.glob(os.path.join(path2, "*.csv"))
    os.chdir(path2)
    for f in files:
        df=pd.read_csv(f)
        # put the Time column into the first columbn( though may be not useful)  https://www.cnblogs.com/wodexk/p/10316793.html
        col_name = df.columns.tolist()  # 将数据框的列名全部提取出来存放在列表里
        col_name.insert(0, 'Time')  # 在列索引为2的位置插入一列,列名为:city，刚插入时不会有值，整列都是NaN
        df = df.reindex(columns=col_name)
        df['Time'] = df.date.map(str) + df.hour.map(str)
        df['Time'] = pd.to_datetime(df['Time'], format='%Y%m%d%H')
        file_name = os.path.basename(f)
        df.to_csv(file_name,index=False)