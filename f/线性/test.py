import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
# 算errorbar
import numpy as np
path2 = r'C:\Users\戴启航\Desktop\新冠\province.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表
path = r'C:\Users\戴启航\Desktop\新冠\Climate zone'

df=pd.read_csv(path2)
print(df)

# dL = df.resample('1h',on='Time').first()
# dL=dL.reset_index()
# df=df.resample('D',on='Time').mean()

# print(dL)
# dcolor = ["#dd433fff", "#63cbff", "#ffa501", "#4d4d4d", "#34495e", "#2ecc71"]
#
# dcolor = sns.color_palette(dcolor, 6),
# sns.set(style="ticks")
# plt.subplot(121)
# sns.lineplot(x='date',y='AQI',data=df,err_style ='band',ci='sd',palette=dcolor)
# sns.lineplot(x='date',y='AQI',data=df,err_style ='band',ci=99,palette=dcolor)
#
#
# # # plt.errorbar(x='Time',y='mean',data=dL,yerr='std')
# # # sns.pointplot(x='Time',y='mean',data=dL)
#
# plt.show()