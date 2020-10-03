import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from matplotlib.ticker import MultipleLocator, FuncFormatter
import matplotlib.pylab as pylab
params={
    'axes.labelsize': '12',
    'xtick.labelsize':'12',
    'ytick.labelsize':'12',
    'lines.linewidth':0.7,
    'legend.fontsize': '10',
    'figure.figsize': '15, 20',
'savefig.dpi':600
}

pylab.rcParams.update(params)


mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False
Path0=r'C:\Users\戴启航\Desktop\新冠\Climate zone'
Path1=r'C:\Users\戴启航\Desktop\新冠\Tier'
path2 = r'C:\Users\戴启航\Desktop\新冠\0.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表
prelock=['20200124','20200101']
level1=['20200226','20200124']
level2=['20200401','20200226']
level3=['20200501','20200401']
time=[prelock,level1,level2,level3]

# def auto_text(rects):
#     for rect in rects:
#         ax.text(rect.get_x(), rect.get_height(), rect.get_height(), ha='left', va='bottom')
#
# def box():
#     wzy = pd.DataFrame()
#     for t in time:
#         time1=t[0]
#         time2=t[1]
#
#         if time1=='20200124':
#             period='(prelock)'
#         elif time1=='20200226':
#             period='(level1)'
#         elif time1=='20200401':
#             period='(level2)'
#         elif time2=='20200401':
#             period='(level3)'
#         for fold in os.listdir(Path0):
#             path = os.path.join(Path0,fold)
#             folderlist= os.listdir(path)
#             fold_name = os.path.basename(fold)
#             dl = pd.read_csv(path2, parse_dates=['date'])
#             dl = dl.drop(['Time'], axis=1)
#             dl = dl.set_index('date')
#             dl = dl.truncate(after=time1, before=time2)
#             i = 0
#             for folder in folderlist:
#                 inner_path = os.path.join(path,folder)
#                 files = glob.glob(os.path.join(inner_path, "*.csv"))
#                 folder_name=os.path.basename(folder)
#                 for f in files:
#                     df = pd.read_csv(f, parse_dates=['date'])
#                     df = df.drop(['Time'], axis=1)
#                     df = df.set_index('date')
#                     dp = df.truncate(after=time1, before=time2)
#                     dl= dl+dp
#                     i=i+1
#                     # percent=percent.apply(lambda x: format(x, '.2%'))
#                     # p.append(period）
#
#             dl=dl/i
#             dl['period']=period
#             dl['area'] = fold_name
#             wzy=wzy.append(dl)
#     return(wzy)
#     # sns.boxplot(x='name', y='value',data=dqh)
#
# wzy=box()
# wzy.to_csv('barplot8.csv')


#读表 绘图
path=r'C:\Users\戴启航\PycharmProjects\f\线性\barplot8.csv'
wzy=pd.read_csv(path,parse_dates=['date'])
wzy['period']=wzy['period'].str.replace('(','')
wzy['period']=wzy['period'].str.replace(')','')



colors = ["#F5F100","#fa9e00","#1d1942","#69d123","#00c0f5","#0056f5","#ff85ab","#f50000"]

customPalette = sns.set_palette(sns.color_palette(colors))


pollutions=['PM2.5','PM10','SO2','CO','NO2','O3']
i=1
plt.style.use('seaborn-ticks')
plt.figure()

for p in pollutions:
    pollution=p
    plt.subplot(3, 2, i)
    b1=sns.barplot(x="area", y=pollution, data=wzy, hue="period", palette="Paired",capsize=.1,ci='sd',errcolor='k',order=['NEC','NW','NCP','MG','TP','YR','CS','SC'])
    plt.xlabel('')
    lag=b1.legend(ncol=4,frameon=False, shadow=False)
    # lag.set_draggable(True)
    # b1.annotate('North', xy=(0.36, 0.92), xycoords='axes fraction', color='k',fontsize=12)
    # b1.annotate('South',fontsize=12,color='k', xy=(0.55, 0.92), xycoords='axes fraction')
    # b1.axvline(x=3.5,linestyle='--',color='red',lw=3)
    # plt.savefig(r'C:\Users\戴启航\Desktop\新冠\图\'' + ' citybox ' + pollution + period + '.png')
    i=i+1
    # if not p =='PM2.5': plt.legend().remove()
    if p=='PM2.5':   b1.set_ylabel('PM$\mathregular{_{2.5}}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'PM10':   b1.set_ylabel('PM$\mathregular{_{10}}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'SO2':   b1.set_ylabel('SO$\mathregular{_2}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'NO2':   b1.set_ylabel('NO$\mathregular{_2}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'O3':   b1.set_ylabel('O$\mathregular{_3}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'CO':   b1.set_ylabel('CO('+r'$\mathregular{m}$'+'$\mathregular{g/m^3}$)')

plt.tight_layout()
plt.show()

