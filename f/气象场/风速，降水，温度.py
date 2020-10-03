import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab
from matplotlib.pyplot import MultipleLocator
import matplotlib.dates as mdates


plt.style.use('seaborn-ticks')

params = {
    'axes.labelsize': '10',
    'xtick.labelsize': '10',
    'ytick.labelsize': '10',
    'lines.linewidth': 1.8,
    'legend.fontsize': '10',
    'figure.figsize': '10,10',
    'lines.marker':None,
    'lines.markersize':6,
'savefig.dpi':600
}
pylab.rcParams.update(params)
all=r'C:\Users\戴启航\PycharmProjects\f\气象场\rain6.csv'
dqh=pd.read_csv(all,parse_dates=['Time'])
dqh['Time']=dqh['Time'].dt.tz_localize('UTC').dt.tz_convert('Asia/Shanghai')
dqh['Time']=dqh['Time'].dt.tz_localize(None)


colors = ["#F5F100","#fa9e00","#1d1942","#69d123","#00c0f5","#0056f5","#ff85ab","#f50000"]
# Set your custom color palette
customPalette = sns.set_palette(sns.color_palette(colors))

fig, ax = plt.subplots(3, 1,sharex=True,sharey=True)
plt.subplot(3,1,1)
ax=sns.lineplot(x='Time',y='WS',hue='area',data=dqh,hue_order=['NEC','NW','NCP','MG','TP','YR','CS','SC'])
h, l = ax.get_legend_handles_labels()
ax.legend(h[1:], l[1:],ncol=4,fancybox=True, frameon=None)
ax.set_ylabel('Wind speed(m/s)')
ax.set_xlabel('')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))

plt.subplot(3,1,2)
ax=sns.lineplot(x='Time',y='Temp',hue='area',data=dqh,hue_order=['NEC','NW','NCP','MG','TP','YR','CS','SC'])
h, l = ax.get_legend_handles_labels()
ax.legend(h[1:], l[1:],fancybox=True, frameon=None,ncol=4)
ax.set_ylabel('Temperature ($^\circ$C)')
ax.set_xlabel('')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))


plt.subplot(3,1,3)
ax=sns.lineplot(x='Time',y='rain6',hue='area',data=dqh,hue_order=['NEC','NW','NCP','MG','TP','YR','CS','SC'],ci=None)
h, l = ax.get_legend_handles_labels()
ax.legend(h[1:], l[1:],fancybox=True, frameon=None,ncol=4)
ax.set_ylabel('Precipitation(mm)')
ax.set_xlabel('')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
plt.tight_layout()
plt.show()

# plt.style.use('seaborn-ticks')
# x_major_locator=MultipleLocator(3)
#
# fig, ax = plt.subplots(2, 4,sharex=True,sharey=True)
#
# plt.subplot(2,4,1)
# ax= sns.lineplot(x='hour', y='WS', data=wzy, hue='area', ci=None,err_style='bars',palette="Paired",marker='o',legend=False)
# # start, end = ax.get_xlim()
# ax.xaxis.set_major_locator(x_major_locator)
# ax.set_xlim([-1, 23])
# ax.set_ylim([1, 5])
#
# ax.annotate('prelock', xy=(0.8, 0.9), xycoords='axes fraction', color='red',fontsize=12)
# ax.set_ylabel('Wind speed(m/s)')
# # ax.spines['bottom'].set_color(None)
#
# plt.subplot(2,4,2)
# ax= sns.lineplot(x='hour', y='WS', data=wzy1, hue='area', ci=None,err_style='bars',legend=None,marker='o',palette="Paired")
# ax.annotate('level1', xy=(0.8, 0.9), xycoords='axes fraction', color='red',fontsize=12)
# ax.set_ylabel('')
# ax.xaxis.set_major_locator(x_major_locator)
# ax.set_ylim([1, 5])
# # ax.spines['bottom'].set_color(None)
#
# plt.subplot(2,4,3)
# ax= sns.lineplot(x='hour', y='WS', data=wzy2, hue='area', ci=None,err_style='bars',legend=None,marker='o',palette="Paired")
# ax.annotate('level2', xy=(0.8, 0.9), xycoords='axes fraction', color='red',fontsize=12)
# ax.set_ylabel('')
# ax.xaxis.set_major_locator(x_major_locator)
# ax.set_ylim([1, 5])
#
# plt.subplot(2,4,4)
# ax= sns.lineplot(x='hour', y='WS', data=wzy3, hue='area', ci=None,err_style='bars',legend=None,marker='o',palette="Paired")
# ax.annotate('level3', xy=(0.8, 0.9), xycoords='axes fraction', color='red',fontsize=12)
# ax.set_ylabel('')
# # ax.spines['left'].set_color(None)
# # ax.spines['top'].set_color(None)
# ax.xaxis.set_major_locator(x_major_locator)
# ax.set_ylim([1, 5])
#
# plt.subplot(2,4,5)
# ax= sns.lineplot(x='hour', y='Temp', data=wzy, hue='area', ci=None,err_style='bars',palette="Paired",marker='o',legend=False)
# # start, end = ax.get_xlim()
# # ax.set_xlim([-1, 23])
# ax.annotate('prelock', xy=(0.8, 0.9), xycoords='axes fraction', color='red',fontsize=12)
# ax.set_ylabel('Temperature ($^\circ$C)')
# ax.xaxis.set_major_locator(x_major_locator)
# ax.set_ylim([-22, 27])
#
# plt.subplot(2,4,6)
# ax= sns.lineplot(x='hour', y='Temp', data=wzy1, hue='area', ci=None,err_style='bars',marker='o',palette="Paired")
# ax.annotate('level1', xy=(0.8, 0.9), xycoords='axes fraction', color='red',fontsize=12)
# ax.set_ylabel('')
# ax.xaxis.set_major_locator(x_major_locator)
# ax.set_ylim([-22, 27])
# h, l = ax.get_legend_handles_labels()
# ax.legend(h[1:], l[1:], ncol=8,
#           loc=(0,-0.2),
#           fancybox=True, frameon=None)
#
# plt.subplot(2,4,7)
# ax= sns.lineplot(x='hour', y='Temp', data=wzy2, hue='area', ci=None,err_style='bars',legend=None,marker='o',palette="Paired")
# ax.annotate('level2', xy=(0.8, 0.9), xycoords='axes fraction', color='red',fontsize=12)
# # ax.xaxis.set_visible(False)
# # ax.spines['top'].set_color(None)
# ax.set_ylabel('')
# ax.xaxis.set_major_locator(x_major_locator)
# ax.set_ylim([-22, 27])
#
# plt.subplot(2,4,8)
# ax= sns.lineplot(x='hour', y='Temp', data=wzy3, hue='area', ci=None,err_style='bars',legend=None,marker='o',palette="Paired")
# ax.annotate('level3', xy=(0.8, 0.9), xycoords='axes fraction', color='red',fontsize=12)
# ax.xaxis.set_major_locator(x_major_locator)
# ax.set_ylim([-22, 27])
# # ax.xaxis.set_visible(False)
# # ax.spines['top'].set_color(None)
#
# ax.set_ylabel('')
# plt.subplots_adjust(top=0.97,
# bottom=0.11,
# left=0.045,
# right=0.985,
# hspace=0.04,
# wspace=0.2
#                     )
# plt.show()