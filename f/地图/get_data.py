import pandas as pd
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt

import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False

myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')



class tool:
    def __init__(self,name,time1,time2):
        self.name=str(name)
        self.time1=time1
        self.time2=time2
    def getdata(pollution,time1,time2):
        path = r'C:\Users\戴启航\Desktop\新冠\city'
        files = glob2.glob(os.path.join(path, "*.csv"))
        lis = []
        name = []
        value = []
        for f in files:
            df= pd.read_csv(f)
            df.Time = pd.to_datetime(df['Time'])
            df = df.set_index('Time')  # 将date设置为index
            df = df.truncate(after=time1, before=time2)
            file_name = os.path.basename(f)
            file_name = file_name.split('.')[0]
            ave = [file_name,df[pollution].mean(0)]
            lis.append(ave)
            name.append(file_name)
            value.append(df[pollution].mean(0))
        return(lis)
pollution='O3'
time1='20200401'
time2='20200101'
print(tool.getdata(pollution,time1,time2))
# time1='20200123'
# time2='20200101'
# pollution='O3'

# df=Datafram(tool.getdata(pollution,time1,time2))
# print('hello world')
# print(name)
# print(value)
# plt.bar(name[1:10],value[1:10])
# plt.show()

