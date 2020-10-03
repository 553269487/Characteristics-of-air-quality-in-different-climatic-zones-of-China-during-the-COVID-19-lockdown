import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator, FuncFormatter
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False

path = r'C:\Users\戴启航\Desktop\新冠\first'
plt.figure(figsize=(10, 5))
plt.style.use('fast')
folderlist= os.listdir(path)
path2 = r'C:\Users\戴启航\Desktop\新冠\0.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表

for folder in folderlist:

    inner_path = os.path.join(path,folder)
    files = glob.glob(os.path.join(inner_path, "*.csv"))

    dl = pd.read_csv(path2,encoding = 'gbk')
    dl = dl.groupby('hour', as_index=False)
    dl = dl.mean()
    i=0
    for f in files:
        df=pd.read_csv(f)
        df = df.groupby('hour', as_index=False)
        df = df.mean()
        dl.iloc[:,4:18] = dl.iloc[:,4:18]+df.iloc[:,4:18] #每个列表时间是一样的，我尝试用循环把PM25的值加起来，求多个城市的平均，但是dl的长度为0所以不能相加？
        i=i+1
        # file_name = os.path.basename(f)
        # file_name = file_name.split('.')[0]
        # plt.plot(df['Time'],df['CO'],label= file_name)
    folder_name = os.path.basename(folder)
    dl['O3']= dl['O3']/i
    dl['NO2']= dl['NO2']/i
    plt.scatter(dl['hour'], dl['O3'], c=dl['NO2'], cmap=plt.get_cmap("GnBu"))
    plt.plot(dl['hour'], dl['O3'], alpha=0.7,label=folder_name)

plt.legend()
plt.ylabel('O3ppm')
a = plt.colorbar()
a.set_label('NO2')
plt.xlabel('hour')
plt.gca().xaxis.set_major_locator(MultipleLocator(2))
plt.title(u"一线城市NO2四个月日平均")
    # plt.savefig(r'C:\Users\戴启航\Desktop\新冠\一线\一线图\'CO气候带.png')
plt.show()

#print(dl)