import pandas as pd
import numpy as np
import glob,os,matplotlib,glob2
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import scipy.stats as sp # for calculating standard error
import matplotlib.pylab as pylab
import cartopy.crs as ccrs
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.mpl.ticker as cticker
import cartopy.io.shapereader as shpreader
fig2 = plt.figure(figsize=(8,8))
proj = ccrs.PlateCarree(central_longitude=105)

reader = shpreader.Reader('Climate_quhua.dbf').geometries()
f2_ax1 = fig2.add_axes([0.05, 0.05, 0.9, 0.9],projection = proj)
f2_ax1.add_geometries(reader, ccrs.PlateCarree(),facecolor='none', edgecolor='black',zorder = 1)
plt.show()