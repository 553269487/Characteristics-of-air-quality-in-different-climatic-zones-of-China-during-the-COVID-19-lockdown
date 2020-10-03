from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from get_data import tool


def mapping():
    if time1=='20200124':
        period='(prelock)'
    elif time1=='20200226':
        period='(level1)'
    elif time1=='20200401':
        period='(level2)'
    elif time2=='20200401':
        period='(level3)'
    c = (
        Map()
        .add(
            pollution,
            tool.getdata(pollution,time1,time2),
            "china-cities",
            label_opts=opts.LabelOpts(is_show=False),
            is_map_symbol_show=False,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=pollution+'average concentration'+period, subtitle=period),
            visualmap_opts=opts.VisualMapOpts(min_=0, max_=120, range_text=["High", "Low"],
                is_calculable=True,
                range_color=["lightskyblue", "yellow", "orangered"],),
        )
        .render(pollution+'average concentration'+period+'.html')
    )

    make_snapshot(snapshot,pollution+r'average concentration'+period+r'.html', pollution+'average concentration'+period+r'.png')


prelock=['20200124','20200101']
level1=['20200226','20200124']
level2=['20200401','20200226']
level3=['20200501','20200401']
time=[prelock,level1,level2,level3]
pollutions=['O3','NO2','PM2.5','CO']
for p in pollutions:
    for t in time:
        time1=t[0]
        time2=t[1]
        pollution=p
        mapping()





