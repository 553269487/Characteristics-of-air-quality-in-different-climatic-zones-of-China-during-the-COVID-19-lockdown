import pandas as pd
from pyecharts import Geo, Style
import pandas as pd
from pyecharts import Style
import glob,os


path = r'C:\Users\戴启航\Desktop\新冠\station.csv'
PATH2= r'C:\Users\戴启航\Desktop\新冠\station'




value=[]
name=[]
lat=[]
lon=[]
files=glob.glob(os.path.join(PATH2,'*.csv'))
for f in files:
    dl=pd.read_csv(f)
    file_name=os.path.basename(f)
    file_name = file_name.split('.')[0]
    value.append(dl['O3'].mean())
    name.append(file_name)
    lat.append(dl['latitude'].iloc[2])
    lon.append(dl['longitude'].iloc[2])
    # print(file_name,mean['AQI'])

df=pd.DataFrame({'name':name,'lat':lat,'lon':lon,'value':value})
print(df)
attr = name
value= value
geo_cities_coords = {df.iloc[i]['name']: [df.iloc[i]['lon'], df.iloc[i]['lat']] for i in range(len(df))}


style = Style(title_color= "#fff",title_pos = "center",
width = 1200,height = 600,background_color = "#404a59")
# 可视化
geo = Geo('', **style.init_style)
geo.add("", attr, value, visual_range=[0, 100], symbol_size=5,
        visual_text_color="#fff", is_piecewise=True,
        border_color="#111",
        is_visualmap=False, maptype='china', visual_split_number=10,
        geo_cities_coords=geo_cities_coords)

geo.render('东莞各个CGI总用户数分布.html')
# https://blog.csdn.net/d345389812/article/details/81750426?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-2