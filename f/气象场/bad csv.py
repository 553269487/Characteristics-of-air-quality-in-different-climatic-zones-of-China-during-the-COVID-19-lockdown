import pandas as pd
from pyecharts import Geo, Style
import pandas as pd
from pyecharts import Style
import numpy as np
import glob,os
import shutil

path=r'C:\Users\戴启航\Desktop\新冠\air'
folderlist= os.listdir(path)
path2 = r'C:\Users\戴启航\PycharmProjects\f\try.csv'  # 因为我不会用字典，所以新建了一个所有值为0的列表
wzy=pd.DataFrame()
dqh=pd.DataFrame()
move=r'C:\Users\戴启航\Desktop\新冠\问题数据'
for folder in folderlist:
    inner_path = os.path.join(path,folder)
    files = glob.glob(os.path.join(inner_path, "*.csv"))
    for f in files:
        df = pd.read_csv(f)
        file_name = os.path.basename(f)
        file_name = file_name.split('.')[0]
        num = df.shape[0]
        # print(num)
        if num >1500:
            print(file_name, num)
            shutil.move(f, move)
