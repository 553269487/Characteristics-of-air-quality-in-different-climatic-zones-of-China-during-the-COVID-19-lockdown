import pandas as pd
df=pd.read_csv(r'C:\Users\戴启航\PycharmProjects\f\气象场\prel1l2l3.csv')
df.replace('CS','PR',inplace=True)
df.replace('SC','CS',inplace=True)
df.replace('PR','SC',inplace=True)
df.to_csv('pre123.csv',index=False)