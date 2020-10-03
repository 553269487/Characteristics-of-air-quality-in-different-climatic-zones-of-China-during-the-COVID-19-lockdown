import pandas as pd

all=r'C:\Users\戴启航\PycharmProjects\f\气象场\rain6.csv'
df=pd.read_csv(all)
# 大风
# strong=df.groupby(['area'],as_index=False).apply(lambda t: t[t.WS>3])
# peak=df.groupby(['area'],as_index=False).apply(lambda t: t[t.WS>4])
# print(strong.groupby('area')['rain6'].count())
# print(peak.groupby('area')['rain6'].count()
#大雨
strong=df.groupby(['area'],as_index=False).apply(lambda t: t[t.rain6>10])
peak=df.groupby(['area'],as_index=False).apply(lambda t: t[t.rain6>25])
print(strong.groupby('area')['rain6'].count())
print(peak.groupby('area')['rain6'].count())
# 温度差
# print(df.groupby('area')['Temp'].last())
# print(df.groupby('area')['Temp'].first())
# print(df.groupby('area')['Temp'].last()-df.groupby('area')['Temp'].first())
