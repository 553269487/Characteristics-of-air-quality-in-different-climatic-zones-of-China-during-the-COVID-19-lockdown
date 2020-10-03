import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from matplotlib.ticker import MultipleLocator, FuncFormatter

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False
Path0=r'C:\Users\戴启航\Desktop\新冠\Climate zone'
Path1=r'C:\Users\戴启航\Desktop\新冠\Tier'
path2 = r'C:\Users\戴启航\Desktop\新冠\0.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表
prelock=['20200124','20200101']
level1=['20200226','20200124']
level2=['20200401','20200226']
level3=['20200501','20200401']
time=[level1,level2,level3]

def box(pollution):
    wzy = pd.DataFrame()
    for t in time:
        time1=t[0]
        time2=t[1]
        value=[]
        name=[]
        if time1=='20200124':
            period='Prelock'
        elif time1=='20200226':
            period='Level1'
        elif time1=='20200401':
            period='Level2'
        elif time2=='20200401':
            period='Level3'
        for fold in os.listdir(Path0):
            path = os.path.join(Path0, fold)
            folderlist= os.listdir(path)
            fold_name = os.path.basename(fold)
            for folder in folderlist:
                inner_path = os.path.join(path,folder)
                files = glob.glob(os.path.join(inner_path, "*.csv"))
                folder_name=os.path.basename(folder)
                for f in files:
                    df=pd.read_csv(f)
                    df.Time = pd.to_datetime(df['Time'])
                    df = df.set_index('Time')  # 将date设置为index
                    dp = df.truncate(after=time1, before=time2)
                    dp=dp.mean()
                    dl=df.truncate(after='20200124',before='20200101')
                    dl=dl.mean()
                    print(dl)
                    percent=((dp-dl)/dl)
                    # percent=percent.apply(lambda x: format(x, '.2%'))
                    value.append(percent[pollution])
                    name.append(fold_name)
                    # p.append(period)
            dqh=pd.DataFrame({'period':period,'area':name,'value':value})
            wzy=wzy.append(dqh)
    print(wzy)
    wzy.to_csv('percent.csv')
    plt.figure(figsize=(8,5))
    # sns.boxplot(x='name', y='value',data=dqh)
    sns.barplot(x="period", y="value", data=wzy,hue="area", palette="Paired")
    plt.title(pollution+' changed percentage '+period)

    def to_percent(temp, position):
        return '%1.0f' % (100 * temp) + '%'

    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    # plt.ylim(-1, 1)
    # plt.savefig(r'C:\Users\戴启航\Desktop\新冠\图\'' + ' citybox ' + pollution + period + '.png')
    plt.show()

pollutions=['O3','NO2','PM2.5','CO']
for p in pollutions:
        pollution=p
        box(p)

