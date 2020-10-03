import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab
import matplotlib.dates as mdates

def plotform():

    plt.axvspan(pd.to_datetime('2020/01/23'), pd.to_datetime('2020/02/25'), facecolor='red', alpha=0.1)
    plt.axvspan(pd.to_datetime('2020/02/25'), pd.to_datetime('2020/03/31'), facecolor='c', alpha=0.1)
    ax.set_xlabel('')
    # ax.set_facecolor('#EAECEE')
    # ax.tick_params(direction='out')
    # plt.tick_params(top='off', right='off', which='both')
    # # ax.tick_params(labeltop='off', labelright='off')
    # ax.spines['top'].set_visible(None)  # 去掉上边框
    # ax.spines['right'].set_color(None)
    # ax.xaxis.set_tick_params(rotation=12)
    ax.annotate('Prelock', xy=(0.09, 0.92), xycoords='axes fraction', color='k',fontsize=12)
    ax.annotate('Level 1',fontsize=12,color='k', xy=(0.33, 0.92), xycoords='axes fraction')
    ax.annotate('Level 2',fontsize=12,color='k', xy=(0.61, 0.92), xycoords='axes fraction')
    ax.annotate('Level 3', fontsize=12, color='k', xy=(0.87, 0.92), xycoords='axes fraction')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
    h, l = ax.get_legend_handles_labels()
    lag=ax.legend(h[1:], l[1:], loc=(0,1),ncol=9,
                 fancybox=True,frameon=False)
    lag.set_draggable(True)

    # plt.legend(loc=(0.05, 1), ncol=8, frameon=False, shadow=False)


# dark = ["#dd433fff", "#63cbff", "#ffa501", "#4d4d4d", "#34495e", "#2ecc71"]
#
# sns.set_palette(sns.color_palette(dark))
# palette="dark"

# path = r'C:\Users\戴启航\Desktop\新冠\Climate zone'
#
#
# folderlist= os.listdir(path)
# path2 = r'C:\Users\戴启航\Desktop\新冠\0.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表
# wzy=pd.DataFrame()
# dqh=pd.DataFrame()
# for folder in folderlist:
#     inner_path = os.path.join(path,folder)
#     folds=os.listdir(inner_path)
#     dl=pd.read_csv(path2,parse_dates=['date'])
#     dl = dl.drop(['Time'], axis=1)
#     dl=dl.set_index('date')
#     i = 0
#     for fold in folds:
#         files = glob2.glob(os.path.join(inner_path,fold,"*.csv"))
#         for f in files:
#             df=pd.read_csv(f,parse_dates=['date'])
#             df=df.drop(['Time'],axis=1)
#             df=df.set_index('date')
#             dl=dl+df# 每个列表时间是一样的，我尝试用循环把PM25的值加起来，求多个城市的平均，但是dl的长度为0所以不能相加？
#             i = i + 1
#     folder_name = os.path.basename(folder)
#     dl=dl/i
#     dl['area']=folder_name
#     wzy=wzy.append(dl)
#
# wzy=wzy.reset_index()
# wzy.to_csv('lineplot8.csv')
#读表
path=r'C:\Users\戴启航\PycharmProjects\f\线性\lineplot8.csv'
wzy=pd.read_csv(path,parse_dates=['date'])




#绘图


i=1
plt.style.use('seaborn-ticks')
fig, ax = plt.subplots(3, 2)

# sns.palplot(sns.hls_palette(8, l=.7, s=.9))
# sns.set_style("whitegrid")
pollutions=['PM2.5','PM10','SO2','CO','NO2','O3']
params = {
    'axes.labelsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'lines.linewidth': 1.8,
    'legend.fontsize': 11,
    'figure.figsize': '15, 20',
    'lines.markersize':4,
'savefig.dpi':600

}

pylab.rcParams.update(params)

colors = ["#F5F100","#fa9e00","#1d1942","#69d123","#00c0f5","#0056f5","#ff85ab","#f50000"]
# Set your custom color palette
customPalette = sns.set_palette(sns.color_palette(colors))

for p in pollutions:

    plt.subplot(3, 2, i)
    i = i + 1
    ax=sns.lineplot(x='date', y=p, data=wzy, hue='area',err_style='band',ci='sd',hue_order=['NEC','NW','NCP','MG','TP','YR','CS','SC'])

    plotform()
    # if not p == 'PM2.5': ax.legend().remove()
    if p=='PM2.5':   ax.set_ylabel('PM$\mathregular{_{2.5}}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'PM10':   ax.set_ylabel('PM$\mathregular{_{10}}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'SO2':   ax.set_ylabel('SO$\mathregular{_2}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'NO2':   ax.set_ylabel('NO$\mathregular{_2}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'O3':   ax.set_ylabel('O$\mathregular{_3}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'CO':   ax.set_ylabel('CO('+r'$\mathregular{m}$'+'$\mathregular{g/m^3}$)')

plt.subplots_adjust(top=0.97,
bottom=0.05,
left=0.045,
right=0.99,
hspace=0.29,
wspace=0.135)
plt.tight_layout()
plt.show()





#     plt.errorbar(x='Time',y='value',yerr=std.value,data=mean,fmt='.k',label=None)
# pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
# g = sns.FacetGrid(df, row="g", hue="g", aspect=15, height=.5, palette=pal)
# sns.kdeplot(x='value',hue='area',data=wzy,clip_on=False, shade=True, alpha=1, lw=1.5, bw=.2)
# plt.legend()

# plt.axvline(x=pd.to_datetime('2020/01/23'))
# plt.axvline(x=pd.to_datetime('2020/02/25'))
# plt.axvline(x=pd.to_datetime('2020/03/31'))

# top=0.984,
# bottom=0.057,
# left=0.042,
# right=0.991,
# hspace=0.229,
# wspace=0.126
