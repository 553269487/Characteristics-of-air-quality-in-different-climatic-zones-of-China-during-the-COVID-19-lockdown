import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


eco = pd.read_csv('cor.csv')
mean=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\allmean.csv')
pollu=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\线性\rangecor.csv')
# print(eco,pollu)
co=pollu.merge(eco,on='name')
def pearson(x, y):
    return stats.pearsonr(x, y)


g = sns.jointplot("G", "PM2.5", co)
g.annotate(pearson, template='r: {val:.2f}\np: {p:.3f}')
plt.show()