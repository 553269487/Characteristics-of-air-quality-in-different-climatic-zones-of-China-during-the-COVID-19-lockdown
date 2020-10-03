import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator, FuncFormatter
import seaborn as sns
import matplotlib.pylab as pylab
params={
    'axes.labelsize': '12',
    'xtick.labelsize':'12',
    'ytick.labelsize':'12',
    'lines.linewidth':0.8,
    'legend.fontsize': '12',
    'figure.figsize'   : '10, 20'
}
pylab.rcParams.update(params)

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False
Path0=r'C:\Users\戴启航\Desktop\新冠\Climate zone'
Path1=r'C:\Users\戴启航\Desktop\新冠\Tier'
path2 = r'C:\Users\戴启航\Desktop\新冠\0.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表

def daily(pollution,period):
    wzy = pd.DataFrame()
    for fold in os.listdir(Path0):
        path = os.path.join(Path0, fold)
        folderlist= os.listdir(path)
        fold_name = os.path.basename(fold)
        i=0
        # dl = pd.read_csv(path2, encoding='gbk')
        # dl = dl.groupby('hour', as_index=False)
        # dl = dl.mean()
        dl=[]
        di=[]

        for folder in folderlist:
            inner_path = os.path.join(path,folder)
            files = glob.glob(os.path.join(inner_path, "*.csv"))
            for f in files:
                df = pd.read_csv(f, parse_dates=['Time'])
                df = df.set_index('Time')
                if period=='pre':
                    df = df.truncate(after='20200124', before='20200101')
                elif period =='l1':
                    df = df.truncate(after='20200226', before='20200124')
                elif period =='l2':
                    df = df.truncate(after='20200401', before='20200226')
                elif period =='l3':
                    df = df.truncate(after='20200418', before='20200401')

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
            dqh = pd.DataFrame({'Time': df.hour, pollution: dl, 'area': fold_name})
            wzy = wzy.append(dqh)
            # else:
            #     path = os.path.join(Path0, fold)
            #     folderlist = os.listdir(path)
            #     fold_name = os.path.basename(fold)
            #     i = 0
            #     # dl = pd.read_csv(path2, encoding='gbk')
            #     # dl = dl.groupby('hour', as_index=False)
            #     # dl = dl.mean()
            #     dl = []
            #     di = []
            #
            #     for folder in folderlist:
            #         inner_path = os.path.join(path, folder)
            #         files = glob.glob(os.path.join(inner_path, "*.csv"))
            #         for f in files:
            #             df = pd.read_csv(f, parse_dates=['date'])
            #             # df = df.set_index('Time').resample('D')
            #             rows = df.shape[0]  # 得到数据行数
            #             if len(dl) == 0:  # 初始化dl和di,di存放每个时间PM2.5不为0的情况数
            #                 dl = df[pollution]
            #                 di = [0 for p in range(rows)]
            #             else:
            #                 dl = [dl[p] + df[pollution][p] for p in range(rows)]
            #                 # 累加求和
            #             di = [di[p] if df[pollution][p] == 0 else di[p] + 1 for p in range(rows)]
            #             # file_name = os.path.basename(f)
            #             # file_name = file_name.split('.')[0]
            #             # plt.plot(df['Time'],df['CO'],label= file_name)
            #         folder_name = os.path.basename(folder)
            #         dl = [dl[p] / di[p] for p in range(rows)]
            #         dqh1 = pd.DataFrame({'Time': df.hour, 'value': dl, 'area': fold_name})
            #         wzy1 = wzy1.append(dqh)
    return(wzy)


# plt.subplot(121)
# sns.barplot(x='Time', y='value', data=wzy, hue='area', ci='sd', capsize=.2,palette="Blues_d",errcolor="c")
# plt.legend(loc=(0.0, 1.0),ncol=3)
# plt.ylabel(pollution)
# # a = plt.colorbar()
# # a.set_label('NO2')
# plt.xlabel('hour')
# plt.gca().xaxis.set_major_locator(MultipleLocator(2))
# plt.show()
    # plt.savefig(r'C:\Users\戴启航\Desktop\新冠\图\zoneav\''+pollution+'daily'+'.png')


    # for fold in os.listdir(Path1):
    #     path = os.path.join(Path1, fold)
    #     plt.figure(figsize=(10, 5))
    #     plt.style.use('fast')
    #     folderlist= os.listdir(path)
    #     fold_name = os.path.basename(fold)
    #     for folder in folderlist:
    #
    #         inner_path = os.path.join(path,folder)
    #         files = glob.glob(os.path.join(inner_path, "*.csv"))
    #
    #         dl = pd.read_csv(path2,encoding = 'gbk')
    #         dl = dl.groupby('hour', as_index=False)
    #         dl = dl.mean()
    #         i=0
    #         for f in files:
    #             df=pd.read_csv(f)
    #             df = df.groupby('hour', as_index=False)
    #             df = df.mean()
    #             dl.iloc[:,2:18] = dl.iloc[:,2:18]+df.iloc[:,2:18] # 每个列表时间是一样的，我尝试用循环把PM25的值加起来，求多个城市的平均，但是dl的长度为0所以不能相加？
    #             i=i+1
    #             # file_name = os.path.basename(f)
    #             # file_name = file_name.split('.')[0]
    #             # plt.plot(df['Time'],df['CO'],label= file_name)
    #         folder_name = os.path.basename(folder)
    #         dl[pollution] = dl[pollution] / i
    #         # dl['NO2']= dl['NO2']/i
    #         # plt.scatter(dl['hour'], dl['O3'], c=dl['NO2'], cmap=plt.get_cmap("GnBu"))
    #         plt.scatter(dl['hour'], dl[pollution], cmap=plt.get_cmap("GnBu"))
    #         plt.plot(dl['hour'], dl[pollution], alpha=0.7,label=folder_name)
    #
    #     plt.legend()
    #     plt.ylabel(pollution)
    #     # a = plt.colorbar()
    #     # a.set_label('NO2')
    #     plt.xlabel('hour')
    #     plt.gca().xaxis.set_major_locator(MultipleLocator(2))
    #     plt.title(fold_name+' '+pollution+' '+'daily')
    #     plt.savefig(r'C:\Users\戴启航\Desktop\新冠\图\Tierav\''+fold_name+' '+pollution+' '+'daily'+'.png')
    #     # plt.show()

pollutions=['PM2.5','PM10','O3','NO2','SO2','CO']
period=['pre','l1','l2','l3']

# sns.palplot(sns.hls_palette(8, l=.7, s=.9))
# plt.style.use('ggplot')
# for p in pollutions:
#     wzy=daily(p)
#     plt.subplot(3,2,i)
#     i=i+1
#     sns.pointplot(x='Time', y='value', data=wzy, hue='area', ci='sd', capsize=.2,
#                   errcolor="c",errwidth=.9,dodge=True,markers=True
#                     )
#     plt.legend(loc=(0.0, 1.0), ncol=7,frameon=False,shadow=False)
#     plt.ylabel(p)
#     # a = plt.colorbar()
#     # a.set_label('NO2')
#     plt.xlabel('hour')
#     if not p =='PM2.5': plt.legend().remove()
#     # plt.gca().xaxis.set_major_locator(MultipleLocator(2))
#
# plt.show()

i=0
for p in pollutions:
    data = pd.DataFrame()
    for time in period:
        wzy=daily(p,time)
        wzy['period']=time
        data=data.append(wzy)
    data.to_csv(p+'.csv')
    if i==0: new=data
    else:
        result=new.merge(data)
        print(result)

print(data)
result.to_csv('pollution range.csv')