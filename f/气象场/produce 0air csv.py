import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab
params={
    'axes.labelsize': '12',
    'xtick.labelsize':'12',
    'ytick.labelsize':'12',
    'lines.linewidth':1.5,
    'legend.fontsize': '12',
    'figure.figsize' : '10, 20'
}
pylab.rcParams.update(params)

path = r'C:\Users\戴启航\Desktop\气象.csv'
df=pd.read_csv(path)
df.rename(columns={'0':'year','1':'month','2':'day','3':'hour','4':'Temp','5':'Dew','6':'SeaP',
                   '7':'WD','8':'WS','9':'cloud','10':'rain0','11':'rain6'},inplace=True)
print(df)
df['Time'] = pd.to_datetime(df[['year', 'month', 'day']])
df['Temp']=df['Temp']/10
# df['Time'] = pd.to_datetime(df['Time'],format='%Y.%m.%d.%H')
sns.lineplot(x='Time',y='Temp',data=df)
plt.show()
df.to_csv('0air.csv')