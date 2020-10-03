import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
path= r'C:\Users\戴启航\Desktop\新冠\一线'
files = os.listdir(path)
file_name = os.path.basename(f)
print(files)
