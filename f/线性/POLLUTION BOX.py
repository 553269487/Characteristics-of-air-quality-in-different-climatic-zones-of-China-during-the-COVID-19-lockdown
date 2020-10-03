import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab
from matplotlib.pyplot import MultipleLocator
params = {
    'axes.labelsize': '10',
    'xtick.labelsize': '10',
    'ytick.labelsize': '10',
    'lines.linewidth': 1,
    'legend.fontsize': '8',
    'figure.figsize': '10,10'
}
pylab.rcParams.update(params)
df=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\pollution range.csv')
df['period']=df['period'].str.replace('l','Level ')
df['period'].replace('pre','Prelock',inplace=True)
print(df)


i=1
plt.style.use('seaborn-ticks')
fig, ax = plt.subplots(3, 2)

# sns.palplot(sns.hls_palette(8, l=.7, s=.9))
# sns.set_style("whitegrid")
pollutions=['PM2.5','PM10','SO2','CO','O3','NO2']


for p in pollutions:

    plt.subplot(3, 2, i)
    i = i + 1
    ax = sns.barplot(x='period', y=p, hue='area', data=df, palette='Paired',hue_order=['NEC','NW','NCP','MG','TP','YR','CS','SC'])
    h, l = ax.get_legend_handles_labels()
    ax.legend(h[0:], l[0:], fancybox=True, frameon=False,ncol=4,loc=(0,1))
    ax.set_xlabel('')
    if p=='PM2.5':   ax.set_ylabel('PM$\mathregular{_{2.5}}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'PM10':   ax.set_ylabel('PM$\mathregular{_{10}}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'SO2':   ax.set_ylabel('SO$\mathregular{_2}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'NO2':   ax.set_ylabel('NO$\mathregular{_2}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'O3':   ax.set_ylabel('O$\mathregular{_3}($'+r'$\mathregular{\mu}$'+'$\mathregular{g/m^3}$)')
    if p == 'CO':   ax.set_ylabel('CO('+r'$\mathregular{m}$'+'$\mathregular{g/m^3}$)')

plt.subplots_adjust(top=0.97,bottom=0.05,wspace=0.2,hspace=0.22)
# plt.tight_layout()
plt.show()
# l1= df.truncate(after='20200226', before='20200124')
#
# l2= df.truncate(after='20200401', before='20200226')
#
# df = df.truncate(after='20200418', before='20200401')