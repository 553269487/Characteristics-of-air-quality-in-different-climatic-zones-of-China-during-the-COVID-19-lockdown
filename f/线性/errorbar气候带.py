import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False

def double_std(array):
 return np.std(array) * 2




path = r'C:\Users\戴启航\Desktop\新冠\Climate zone'
plt.figure(figsize=(10, 5))
plt.style.use('ggplot')
folderlist= os.listdir(path)
path2 = r'C:\Users\戴启航\Desktop\新冠\0.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表

def errobar(pollution):
    wzy = pd.DataFrame()
    for folder in folderlist:
        if folder in ['PR','YR','SC']:
            continue
        inner_path = os.path.join(path,folder)
        folds=os.listdir(inner_path)
        dl=[]
        di=[]
        i = 0
        for fold in folds:
            files = glob2.glob(os.path.join(inner_path,fold,"*.csv"))
            for f in files:
                df=pd.read_csv(f,parse_dates=['date'])
                # df = df.set_index('Time').resample('D')
                rows = df.shape[0]  # 得到数据行数
                if len(dl) == 0:  # 初始化dl和di,di存放每个时间PM2.5不为0的情况数
                        dl = df[pollution]
                        di = [0 for p in range(rows)]
                else:
                        dl = [dl[p] + df[pollution][p] for p in range(rows)]
                        # 累加求和
                di = [di[p] if df[pollution][p] == 0 else di[p] + 1 for p in range(rows)]
                # file_name = os.path.basename(f)
                # file_name = file_name.split('.')[0]
                # plt.plot(df['Time'],df['CO'],label= file_name)
        folder_name = os.path.basename(folder)
        dl = [dl[p] / di[p] for p in range(rows)]
        dqh = pd.DataFrame({'Time': df.date,'value': dl,'area':folder_name})
        wzy=wzy.append(dqh)
    return(wzy)
        # dqh=dqh.set_index('Time')
        # mean = dqh.resample('D').mean().reset_index()
        # std= dqh.resample('D').std()
P=errobar('PM2.5')
sns.lineplot(x='Time',y='value',data=P,hue='area',palette="Set2",err_style='band',ci='sd')
    # plt.errorbar(x='Time',y='value',yerr=std.value,data=mean,fmt='.k',label=None)
# pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
# g = sns.FacetGrid(df, row="g", hue="g", aspect=15, height=.5, palette=pal)
# sns.kdeplot(x='value',hue='area',data=wzy,clip_on=False, shade=True, alpha=1, lw=1.5, bw=.2)
# plt.legend()
plt.text(pd.to_datetime('2020/01/07'),2,'prelock',fontsize=18,color='red',alpha=0.5)
plt.text(pd.to_datetime('2020/02/07'),2,'level1',fontsize=18,color='blue',alpha=0.5)
plt.text(pd.to_datetime('2020/03/10'),2,'level2',fontsize=18,color='red',alpha=0.5)
# plt.text(pd.to_datetime('2020/03/28'),1.8,'level3',fontsize=18,color='blue',alpha=0.5)
plt.axvspan(pd.to_datetime('2020/01/23'), pd.to_datetime('2020/02/25'), facecolor='red', alpha=0.3)
plt.axvspan(pd.to_datetime('2020/02/25'), pd.to_datetime('2020/03/31'), facecolor='c', alpha=0.2)
# plt.axvline(x=pd.to_datetime('2020/01/23'))
# plt.axvline(x=pd.to_datetime('2020/02/25'))
# plt.axvline(x=pd.to_datetime('2020/03/31'))
plt.xlabel(u"Time")  # plots an axis lable
plt.ylabel(u"ug/m3")
    # plt.savefig(r'C:\Users\戴启航\Desktop\新冠\一线\一线图\'CO气候带.png')
plt.show()

