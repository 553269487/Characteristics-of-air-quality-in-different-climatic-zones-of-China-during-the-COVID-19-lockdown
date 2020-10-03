import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab
from matplotlib.pyplot import MultipleLocator
pd.set_option('display.max_rows',None)
pd.set_option('display.max_colwidth',None)


plt.style.use('seaborn')
params = {
    'axes.labelsize': '15',
    'xtick.labelsize': '15',
    'ytick.labelsize': '15',
    'lines.linewidth': 1.5,
    'legend.fontsize': '15',
    'figure.figsize': '10,10'
}
pylab.rcParams.update(params)
pre=r'C:\Users\戴启航\PycharmProjects\f\气象场\pre.csv'
l1=r'C:\Users\戴启航\PycharmProjects\f\气象场\level1.csv'
l2=r'C:\Users\戴启航\PycharmProjects\f\气象场\level2.csv'
l3=r'C:\Users\戴启航\PycharmProjects\f\气象场\level3.csv'
wzy=pd.read_csv(pre)
wzy1=pd.read_csv(l1)
wzy2=pd.read_csv(l2)
wzy3=pd.read_csv(l3)

df=wzy.groupby(['area','hour'])['Temp'].mean().reset_index()
range=df.groupby(['area'])['Temp'].max()-df.groupby(['area'])['Temp'].min().to_frame().T
range['period']='prelock'

df=wzy1.groupby(['area','hour'])['Temp'].mean().reset_index()
range1=df.groupby(['area'])['Temp'].max()-df.groupby(['area'])['Temp'].min().to_frame().T
range1['period']='level1'


df=wzy2.groupby(['area','hour'])['Temp'].mean().reset_index()
range2=df.groupby(['area'])['Temp'].max()-df.groupby(['area'])['Temp'].min().to_frame().T
range2['period']='level2'

df=wzy3.groupby(['area','hour'])['Temp'].mean().reset_index()
range3=df.groupby(['area'])['Temp'].max()-df.groupby(['area'])['Temp'].min().to_frame().T
range3['period']='level3'

T=pd.concat([range,range1,range2,range3])
print(T.mean())

df=wzy.groupby(['area','hour'])['WS'].mean().reset_index()
range=df.groupby(['area'])['WS'].max()-df.groupby(['area'])['WS'].min().to_frame().T
range['period']='prelock'

df=wzy1.groupby(['area','hour'])['WS'].mean().reset_index()
range1=df.groupby(['area'])['WS'].max()-df.groupby(['area'])['WS'].min().to_frame().T
range1['period']='level1'


df=wzy2.groupby(['area','hour'])['WS'].mean().reset_index()
range2=df.groupby(['area'])['WS'].max()-df.groupby(['area'])['WS'].min().to_frame().T
range2['period']='level2'

df=wzy3.groupby(['area','hour'])['WS'].mean().reset_index()
range3=df.groupby(['area'])['WS'].max()-df.groupby(['area'])['WS'].min().to_frame().T
range3['period']='level3'

WS=pd.concat([range,range1,range2,range3])

print(WS.mean())

dqh=T.append(WS)
dqh.to_csv('TSR.csv')