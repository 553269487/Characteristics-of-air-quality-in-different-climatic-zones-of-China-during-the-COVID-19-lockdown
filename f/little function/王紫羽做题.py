import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab
import cartopy

myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False
params={
    'axes.labelsize': '12',
    'xtick.labelsize':'12',
    'ytick.labelsize':'12',
    'lines.linewidth':1.5,
    'legend.fontsize': '12',
    'figure.figsize' : '10, 20'
}
pylab.rcParams.update(params)
perday=pd.DataFrame(columns=['每天总成交额','每天总成交平均总价','每天成交每平米平均价'])
path=r'C:\Users\戴启航\Desktop\chengdu.csv'
df= pd.read_csv(path,sep='\t')
df['date']=pd.to_datetime(df['deal_date'])
print(df)
perday['每天总成交额']=df.groupby('date')['total_price'].sum()
perday['每天总成交平均总价']=df.groupby('date')['total_price'].mean()
perday['每天成交每平米平均价']=df.groupby('date')['unit_price'].mean()
print(perday)
plt.style.use('seaborn-ticks')
ax=perday.plot()
ax.set_ylabel('价格（元）',fontproperties = myfont)
ax.legend(prop = myfont)
plt.show()
perday.to_csv('每天成交价.csv')

