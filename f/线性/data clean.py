import pandas as pd
from pyecharts import Geo, Style
import pandas as pd
from pyecharts import Style
import glob,os
import shutil


path = r'C:\Users\戴启航\Desktop\新冠\station.csv'
PATH2= r'C:\Users\戴启航\Desktop\新冠\station'
move= r'C:\Users\戴启航\Desktop\新冠\station\0'
files=glob.glob(os.path.join(PATH2,'*.csv'))
for f in files:
    df=pd.read_csv(f)
    file_name=os.path.basename(f)
    file_name = file_name.split('.')[0]
    num = df['O3'].isna().sum()
    if num > 100:
        print(file_name,num)
        # shutil.move(f, move)
