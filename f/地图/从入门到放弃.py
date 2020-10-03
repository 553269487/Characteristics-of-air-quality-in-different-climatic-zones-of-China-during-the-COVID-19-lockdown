import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import cartopy.mpl.ticker as mticker
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv(r'C:\Users\戴启航\Desktop\新冠\站点列表(含经纬度)-新-1497个.csv')
def main():

    # 设置投影
    proj = ccrs.PlateCarree() # 圆柱投影， 默认WGS1984
    # extent=[80, 130, 13, 55]
    # extent = [110, 124, 27, 36] # 显示范围
    extent = [70, 140, 15, 55] # 显示范围
    shpfn = 'bou2_4l.shp'
    tpshp = 'bou2_4l.shp'
    glshp = 'bou2_4l.shp'
    reader = shpreader.Reader(shpfn)
    states_provinces = cfeature.ShapelyFeature(reader.geometries(), proj, facecolor='none')
    # reader = shpreader.Reader(tpshp)
    # tpfeat = cfeature.ShapelyFeature(reader.geometries(), proj, facecolor='none')
    # reader = shpreader.Reader(glshp)
    # glfeat = cfeature.ShapelyFeature(reader.geometries(), proj, facecolor='none')

    fig = plt.figure(figsize=(8, 8), frameon=True)
    ax1 = fig.add_subplot(1, 1, 1, projection=proj)
    # Label axes of a Mercator projection without degree symbols in the labels
    # and formatting labels to include 1 decimal place:
    ax1.set_extent(extent, proj)
    # ax1.add_feature(glfeat, linewidth=1.5, edgecolor='grey')
    ax1.add_feature(states_provinces, linewidth=1, edgecolor='k')
    # ax1.add_feature(tpfeat, linewidth=2.0, edgecolor='red')
    # ax1.add_feature(cfeature.COASTLINE.with_scale('10m'))
    # ax1.add_feature(cfeature.LAND.with_scale('10m'))
    # ax1.add_feature(cfeature.RIVERS.with_scale('10m'))
    # ax1.stock_img()
    # 设置经纬网以及标签
    # ax1.gridlines(proj, draw_labels=False, linewidth=1.2, color='k', alpha=0.5, linestyle='--')
    ax1.set_xticks(np.arange(extent[0], extent[1]+2, 2), crs=proj)
    ax1.set_yticks(np.arange(extent[2]+1, extent[3]+2, 2), crs=proj)
    ax1.xaxis.set_major_formatter(mticker.LongitudeFormatter())
    ax1.yaxis.set_major_formatter(mticker.LatitudeFormatter())
    ax1.scatter(data["经度"], data["纬度"], s=50, c='#0066CC',edgecolors='k',marker='o',transform=ccrs.PlateCarree())
    # plt.savefig(r'C:\Users\zengsk\Desktop\test.jpg', dpi=300)
    plt.show()

if __name__ == '__main__':
    main()