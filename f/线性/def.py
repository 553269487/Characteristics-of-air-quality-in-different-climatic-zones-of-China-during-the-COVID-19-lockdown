import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')


path = r'C:\Users\戴启航\Desktop\新冠\一线'

folderlist= os.listdir(path)
for folder in folderlist:
    plt.figure(figsize=(50, 30))
    plt.style.use('fast')
    inner_path = os.path.join(path,folder)
    files = glob2.glob(os.path.join(inner_path, "*.csv"))
    path2= r'C:\Users\戴启航\Desktop\新冠\北京悲剧.csv'  #因为我不会用字典，所以新建了一个所有值为0的列表
    dl = pd.read_csv(path2,encoding = 'gbk')
    i=0
    for f in files:
        df=pd.read_csv(f)
        file_name = os.path.basename(f)
        file_name = file_name.split('.')[0]
        df.Time = pd.to_datetime(df['Time'])
        df['O3'] = df['O3'].rolling(window=20).mean()
        plt.plot(df['Time'],df['O3'],label= file_name)

    plt.axvline(x=pd.to_datetime('2020/01/23'))
    plt.legend(prop=myfont, ncol=4)
    folder_name = os.path.basename(folder)
    plt.xlabel(u"时间", fontproperties = myfont)# plots an axis lable
    plt.ylabel(u"ug/m3", fontproperties = myfont)
    plt.title(folder_name+'O3平均浓度', fontproperties = myfont)
    # plt.savefig(r'C:\Users\戴启航\Desktop\新冠\0\'O3北部城市.png')
    plt.show()