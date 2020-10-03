import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab
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

df=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\little function\GDP+car.csv')
fig = plt.figure() # Create matplotlib figure
plt.style.use('seaborn-ticks')
ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.4



bar1=df.plot(x='area',y='G',kind='bar', color='#FFB300', ax=ax, width=width, position=1,label='GDP')
bar2=df.plot(x='area',y='car',kind='bar', color='#B0BEC5', ax=ax2, width=width, position=0,label='Vehicle population')
ax.set_ylabel('GDP(10'+'$\mathregular{^9}$'+'RMB)')
ax2.set_ylabel('Private Vehicle population(10'+'$\mathregular{^4}$)')
ax.set_xlabel('')

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=2)
ax.legend().remove()
ax.xaxis.set_tick_params(rotation=0)
plt.show()