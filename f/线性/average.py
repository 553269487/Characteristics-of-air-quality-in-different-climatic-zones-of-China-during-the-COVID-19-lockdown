import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

path = r'C:\Users\戴启航\Desktop\新冠\first'
plt.figure(figsize=(10, 5))
plt.style.use('fast')
folderlist= os.listdir(path)
for folder in folderlist:

    inner_path = os.path.join(path,folder)
    files = glob2.glob(os.path.join(inner_path, "*.csv"))
    print(files)
    di = []
    dl = []
    for f in files:
            df = pd.read_csv(f, engine="python")
            df['Time'] = df.date.map(str) + df.hour.map(str)
            df['Time'] = pd.to_datetime(df['Time'], format='%Y%m%d%H')
            rows = df.shape[0]  # 得到数据行数
            if len(dl) == 0:  # 初始化dl和di,di存放每个时间PM2.5不为0的情况数
                    dl = df['CO']
                    di = [0 for p in range(rows)]
            else:
                    dl = [dl[p] + df['CO'][p] for p in range(rows)]
                    # 累加求和
            di = [di[p] if df['CO'][p] == 0 else di[p] + 1 for p in range(rows)]
            # file_name = os.path.basename(f)

            # file_name = file_name.split('.')[0]
            # plt.plot(df['Time'],df['PM2.5'],label= file_name)
    # dl['PM2.5']= dl['PM2.5']/i
    folder_name = os.path.basename(folder)
    dl = [dl[p] / di[p] for p in range(rows)]
    dl=pd.DataFrame(dl)
    dl= dl.rolling(window=20).mean() #移动平均平滑数据
    # print(dl['PM2.5'].head())
    print(sum([0 if i == 4 else 1 for i in di]))
    plt.plot(df['Time'], dl,label=folder_name)
plt.legend(prop=myfont)
plt.xlabel(u"时间", fontproperties=myfont)  # plots an axis lable
plt.ylabel(u"ug/m3", fontproperties=myfont)
plt.title(u"一线城市CO平均浓度", fontproperties=myfont)
    # plt.savefig(r'C:\Users\戴启航\Desktop\新冠\一线\一线图\'CO气候带.png')
plt.show()

#print(dl)