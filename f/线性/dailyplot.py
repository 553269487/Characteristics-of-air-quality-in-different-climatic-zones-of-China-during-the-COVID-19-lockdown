import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab
from matplotlib.pyplot import MultipleLocator
x_major_locator=MultipleLocator(2)

COpre=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\COpre.csv')
COl1= pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\COl1.csv')
COl2= pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\COl2.csv')
COl3= pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\COl3.csv')
SO2pre=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\SO2pre.csv')
SO2l1=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\SO2l1.csv')
SO2l2=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\SO2l2.csv')
SO2l3=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\SO2l3.csv')
O3pre=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\O3pre.csv')
O3l1=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\O3l1.csv')
O3l2=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\O3l2.csv')
O3l3=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\O3l3.csv')
NO2pre=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\NO2pre.csv')
NO2l1=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\NO2l1.csv')
NO2l2=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\NO2l2.csv')
NO2l3=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\NO2l3.csv')
PM25pre=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\PM2.5pre.csv')
PM25l1=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\PM2.5l1.csv')
PM25l2=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\PM2.5l2.csv')
PM25l3=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\PM2.5l3.csv')
PM10pre=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\PM10pre.csv')
PM10l1=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\PM10l1.csv')
PM10l2=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\PM10l2.csv')
PM10l3=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\PM10l3.csv')

CO=[COpre,COl1,COl2,COl3]
SO2=[SO2pre,SO2l1,SO2l2,SO2l3]
PM25=[PM25pre,PM25l1,PM25l2,PM25l3]
PM10=[PM10pre,PM10l1,PM10l2,PM10l3]
O3=[O3pre,O3l1,O3l2,O3l3]
NO2=[NO2pre,NO2l1,NO2l2,NO2l3]
savepath=r'C:\Users\戴启航\Desktop\dailyfigure\G'

colors = ["#F5F100","#fa9e00","#1d1942","#69d123","#00c0f5","#0056f5","#ff85ab","#f50000"]
customPalette = sns.set_palette(sns.color_palette(colors))

params={
'savefig.dpi':600
}
sns.set_style("darkgrid", {"axes.facecolor": ".8"})
def form(period,pollution):
    h, l = ax.get_legend_handles_labels()
    ax.legend(h[1:], l[1:], ncol=8,
              loc=(0.15, 1.03),
              fancybox=True, frameon=False)
    ax.set_xlabel('')
    ax.set_ylabel(pollution)
    ax.annotate(period, xy=(0.8, 0.92), xycoords='axes fraction', color='black', fontsize=12)
    ax.xaxis.set_major_locator(x_major_locator)

list=[PM25,PM10,SO2,CO,O3,NO2]
b=0
for p in list:
    plt.figure(figsize=(10, 8))
    i=0
    for time in p:
        i=i+1
        if i==1:
            d='Prelock'
            color = None
        if i==2:
            d='Level 1'
            color='#e6cccc'
        if i==3:
            d='Level 2'
            color ='#CAE0E2'
        if i==4:
            d='Level 3'
            color = None
        plt.subplot(2,2,i,facecolor=color)
        ax = sns.lineplot(x='Time.1', y='value', hue='area', data=time, ci=0, marker='o',hue_order=['NEC','NW','NCP','MG','TP','YR','CS','SC'])
        if b == 0:
            kind = 'PM2.5'
            # ax.set_ylim([0, 100])
        if b == 1:
            kind = 'PM10'
            # ax.set_ylim([0, 130])
        if b == 2:
            kind = 'SO2'
            # ax.set_ylim([0, 30])
        if b == 3:
            kind = 'CO'
            # ax.set_ylim([0, 1.7])
        if b == 4:
            kind = 'O3'
            # ax.set_ylim([0, 110])
        if b == 5:
            kind = 'NO2'
            # ax.set_ylim([0, 65])
        form(d, kind)
        if not i ==1: ax.legend().remove()
        if kind == 'PM2.5':   ax.set_ylabel(
            'PM$\mathregular{_{2.5}}($' + r'$\mathregular{\mu}$' + '$\mathregular{g/m^3}$)')
        if kind == 'PM10':   ax.set_ylabel('PM$\mathregular{_{10}}($' + r'$\mathregular{\mu}$' + '$\mathregular{g/m^3}$)')
        if kind == 'SO2':   ax.set_ylabel('SO$\mathregular{_2}($' + r'$\mathregular{\mu}$' + '$\mathregular{g/m^3}$)')
        if kind == 'NO2':   ax.set_ylabel('NO$\mathregular{_2}($' + r'$\mathregular{\mu}$' + '$\mathregular{g/m^3}$)')
        if kind == 'O3':   ax.set_ylabel('O$\mathregular{_3}($' + r'$\mathregular{\mu}$' + '$\mathregular{g/m^3}$)')
        if kind == 'CO':   ax.set_ylabel('CO(' + r'$\mathregular{m}$' + '$\mathregular{g/m^3}$)')

    b=b+1
    plt.subplots_adjust(wspace=0.25, hspace=0.25)
    plt.savefig(savepath + kind +'.png',format = "png",dpi=500)
