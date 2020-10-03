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


data=pd.read_csv(r'C:\Users\戴启航\Desktop\新冠\站点列表(含经纬度)-新-1497个.csv')
#建立画布(这部分没啥好说的，跳过)
fig2 = plt.figure(figsize=(8,8))
proj = ccrs.PlateCarree(central_longitude=105)


leftlon, rightlon, lowerlat, upperlat = (70,140,15,55)
#绘制地图
f2_ax1 = fig2.add_axes([0.05, 0.05, 0.9, 0.9],projection = proj) #设定你的子图的左、下位置和宽度、长度，注意在，这里的数值，都是百分比，比如0.05，指的是距图边界0.05个宽度的位置
#在画布的绝对坐标建立子图
f2_ax1.set_extent([leftlon, rightlon, lowerlat, upperlat], crs=ccrs.PlateCarree())
#海岸线，50m精度
# f2_ax1.add_feature(cfeature.LAND.with_scale('50m'))
# f2_ax1.add_feature(cfeature.RIVERS.with_scale('50m'))
#湖泊数据(但是这个貌似只画了比较大的湖泊，比如贝湖巴湖)
# f2_ax1.add_feature(cfeature.LAKES, alpha=0.5)
#以下6条语句是定义地理坐标标签格式
f2_ax1.set_xticks(np.arange(leftlon,rightlon+10,10), crs=ccrs.PlateCarree())
f2_ax1.set_yticks(np.arange(lowerlat,upperlat+10,10), crs=ccrs.PlateCarree())
lon_formatter = cticker.LongitudeFormatter()
lat_formatter = cticker.LatitudeFormatter()
f2_ax1.xaxis.set_major_formatter(lon_formatter)
f2_ax1.yaxis.set_major_formatter(lat_formatter)
# f2_ax1.set_title('Station',loc='center',fontsize =15)
#读取shp文件
china = shpreader.Reader('bou2_4l.shp').geometries()

#叠加图片
# fname = r'C:\Users\戴启航\Desktop\气候带.PNG'
# img_extent = (70,140,15,55)
# img = plt.imread(fname)
# f2_ax1.imshow(img, origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
#绘制中国国界省界九段线等等
f2_ax1.add_geometries(china, ccrs.PlateCarree(),facecolor='none', edgecolor='black',zorder = 1)
# #添加南海，实际上就是新建一个子图覆盖在之前子图的右下角
f2_ax2 = fig2.add_axes([0.76, 0.05, 0.17, 0.23],projection = proj)
f2_ax2.set_extent([105, 125, 0, 25], crs=ccrs.PlateCarree())
f2_ax2.add_feature(cfeature.COASTLINE.with_scale('50m'))
china = shpreader.Reader('bou2_4l.dbf').geometries()
f2_ax2.add_geometries(china, ccrs.PlateCarree(),facecolor='none', edgecolor='black',zorder = 1)

f2_ax1.scatter(data["经度"],data["纬度"],s =50,c='#0066CC',marker='o',edgecolors='white',transform=ccrs.PlateCarree())
f2_ax2.scatter(data["经度"],data["纬度"],s =2,c='#0066CC',marker='o',transform=ccrs.PlateCarree())

plt.show()
# plt.savefig('dpihigh.png',dpi=1000)
