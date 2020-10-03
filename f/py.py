from toapi import XPath, Item, Api
from toapi import Settings

class MySettings(Settings):
    web = {
        # 是否需要使用phantomjs加载
        "with_ajax": False
    }

# 需要构建api的目标网址
api = Api('http://gk.chengdu.gov.cn/govInfoPub/', settings = MySettings)

class Post(Item):
    # api服务返回json的字段：网页上字段所对应Xpath
    # 这里Xpath是用列表识别自动识别的 可以看我以前的文章
    url = XPath('/html/body/div[2]/div/div[3]//a/@href')
    title = XPath('/html/body/div[2]/div/div[3]//a/span[2]/text()')

    class Meta:
        #  source :包含单个数据结构的HTML部分。
        source = XPath('/html')
        # 一个正则表达式，定义API服务的路径。理解成flask中路由就好了
        route = {"/test?page=:page":"list.action?classId=07170201020202&tn=2&p=:page"}

# 注册该服务
api.register(Post)
#运行服务器
api.serve()

# Visit: http://127.0.0.1:5000/