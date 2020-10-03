import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt

myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')


path = r'C:\Users\戴启航\Desktop\新冠\city'
def re_name():
    # filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）
    for root, dirs, files in os.walk(path):
        for name in files:
            pos = name.find("州")
            if (pos==-1): # skip file without the keywords and skip the file which the second character is the keywords
                continue
            if(pos == 1):
                continue
            newname = name[0:pos] +'.csv'
            os.rename(os.path.join(root, name), os.path.join(root, newname)) #https://blog.csdn.net/liuyudong_/article/details/80319592
re_name()
