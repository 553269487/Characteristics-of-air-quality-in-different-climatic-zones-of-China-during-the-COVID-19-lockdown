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
df=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\SO2.csv')
m=df.groupby(['area','period','Time.1']).mean()
m=m.reset_index()
max=m.groupby(['area','period']).max()
min=m.groupby(['area','period']).min()
print(max-min)
