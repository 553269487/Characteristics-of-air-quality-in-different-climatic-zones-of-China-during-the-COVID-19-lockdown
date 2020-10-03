import os
import shutil
import glob
path = r'C:\Users\戴启航\Desktop\新冠\city'
files = os.listdir(path)
os.chdir(path)

T1={
    "NEC" : [''],
    "TP" : [''],
    'NW':[''],
    "NCP" : ['北京'],
    "YR" : ['上海'],
    'SC' : [''],
    'PR' : ['广州','深圳'],
    }
NT1={
    "NEC" : ['沈阳'],
    "TP" : [''],
    'NW':[],
    "NCP" : ['天津','郑州','青岛','西安'],
    "YR" : ['上海','南京','苏州','宁波','杭州'],
    'SC' : ['成都','重庆','武汉','长沙','昆明'],
    'PR' : ['东莞'],
    }
T2={
    "NEC" : ['大连','哈尔滨','长春'],
    "TP" : [''],
    'NW':['兰州','太原'],
    "NCP" : ['济南','石家庄'],
    "YR" : ['无锡','合肥','金华','常州','南通','嘉兴','徐州','绍兴','扬州'],
    'SC' : ['福州','厦门','温州','泉州','贵阳','南昌','台州'],
    'PR' : ['佛山','南宁','惠州','珠海','中山','海口'],
    }
T3={
    "NEC" : ["大庆","吉林"],
    "TP" : [''],
    'NW':['乌鲁木齐','银川'],
    "NCP" : ["连云港","包头","泰安","秦皇岛","新乡","鞍山","商丘","沧州","南阳","威海","咸阳",
             "邯郸","淄博","济宁","呼和浩特","廊坊","唐山","临沂","洛阳","潍坊","保定"],
    "YR" : ["宿迁","荆州","马鞍山","蚌埠","滁州","信阳","岳阳","阜阳","舟山","宜昌","盐城","镇江","泰州","芜湖","淮安","安庆"],
    'SC' : ["郴州","南平","三明","湘潭","丽水","襄阳","株洲","九江","衡阳","上饶","赣州","湖州","遵义","绵阳"],
    'PR' : ['汕头',"潮州","梅州","龙岩","肇庆","清远","宁德","柳州","漳州","汕头","桂林","揭阳","三亚","江门","莆田","湛江"],
    }
T4={
    "NEC" : ["绥化","延边州","佳木斯","齐齐哈尔","牡丹江","丹东"],
    "TP" : ["西宁","拉萨"],
    'NW':[''],
    "NCP" : ["赤峰","滨州","亳州","临汾","枣庄","聊城","承德","宝鸡","鄂尔多斯","榆林","平顶山","盘锦","渭南",
             "安阳","张家口","运城","大同","德州","焦作","营口","锦州","晋中","许昌","周口","日照","菏泽","东营","驻马店","邢台","开封"
],
    "YR" : ["黄石","宿州","六安","景德镇","黄冈","淮南","孝感","益阳","宜城","黄山","十堰","铜陵","咸宁"],
    'SC' : ["曲靖","抚州","黔南州","怀化","常德","南充","宜春","大理","丽江","衢州","黔东南州",
            "德阳","邵阳","铜仁","永州","宜宾","乐山","吉安","娄底","六盘水","毕节","泸州","恩施州","安顺","鹰潭","眉山"],
    'PR' : ["玉林","茂名","韶关","汕尾","红河州","北海","阳江","河源","西双版纳州","保山","百色","梧州","德宏"],
    }
T5={
    "NEC" : ["四平","呼伦贝尔","抚顺","通化","松原","通辽","辽阳","本溪","铁岭","白城","白山","鸡西","黑河","双鸭山","伊春","鹤岗","辽源","大兴安岭","七台河"],
    "TP" : ["玉树","那曲","黄南","海北","果洛","阿里","海南","山南","迪庆","阿坝","海西","甘孜","林芝","日喀则","海东","甘南","昌都"],
    'NW':["克拉玛依","酒泉","巴彦淖尔","伊犁","哈密","乌海","嘉峪关","张掖","吴忠","昌吉","巴音郭楞","阿拉善盟",
          "阿克苏","金昌","石嘴山","武威","吐鲁番","喀什","中卫","阿勒泰","塔城","博尔塔拉","和田","克州"],
    "NCP" : ["临夏","固原","白银","铜川","定西","商洛","平凉","朔州","阳泉","陇南","三门峡","安康","乌兰察布","庆阳","鹤壁","兴安盟","天水",
        "晋城","锡林郭勒盟","朝阳","忻州","淮北","濮阳","葫芦岛","衡水","汉中","漯河","延安","长治","阜新","吕梁"],
    "YR" : ["广元","鄂州","池州","荆门","随州"],
    'SC' : ["楚雄州","黔西南州","新余","昭通","河池","达州","凉山州","张家界","遂宁","广安","萍乡","自贡",
            "雅安","攀枝花","怒江州","巴中","资阳"],
    'PR' : ["防城港","玉溪","普洱","钦州","文山州","云浮","贵港","来宾","崇左","贺州","临沧","儋州","三沙"],
    }




for f in files:
    file_name = os.path.basename(f)
    file_name = file_name.split('.')[0]
    print(file_name)
    for key in T1:
        if file_name in T1.get(key):
            try:
                folder_name= 'T1'+' '+key
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    shutil.move(f,folder_name)
                    print(folder_name)
                else:
                    shutil.move(f,folder_name)
                    print(folder_name)
            except:
                print('失败了哦宝宝')

    for key in NT1:
        if file_name in NT1.get(key):
            try:
                folder_name= 'NT1'+' '+key
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    shutil.move(f,folder_name)
                    print(folder_name)
                else:
                    shutil.move(f,folder_name)
                    print(folder_name)
            except:
                print('失败了哦宝宝')



    for key in T2:
        if file_name in T2.get(key):
            try:
                folder_name= 'T2'+' '+key
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    shutil.move(f,folder_name)
                    print(folder_name)
                else:
                    shutil.move(f,folder_name)
                    print(folder_name)
            except:
                print('失败了哦宝宝')

    for key in T3:
        if file_name in T3.get(key):
            try:
                folder_name= 'T3'+' '+key
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    shutil.move(f,folder_name)
                    print(folder_name)
                else:
                    shutil.move(f,folder_name)
                    print(folder_name)
            except:
                print('失败了哦宝宝')

    for key in T4:
        if file_name in T4.get(key):
            try:
                folder_name= 'T4'+' '+key
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    shutil.move(f,folder_name)
                    print(folder_name)
                else:
                    shutil.move(f,folder_name)
                    print(folder_name)
            except:
                print('失败了哦宝宝')
    for key in T5:
        if file_name in T5.get(key):
            try:
                folder_name= 'T5'+' '+key
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    shutil.move(f,folder_name)
                    print(folder_name)
                else:
                    shutil.move(f,folder_name)
                    print(folder_name)
            except:
                print('失败了哦宝宝')


print(T2.get('NEC'))