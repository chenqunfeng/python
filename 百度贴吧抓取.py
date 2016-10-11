# # -*- coding:utf-8 -*-
# import urllib
# import urllib.request
# import re

# #百度贴吧爬虫类
# class BDTB:

#     #初始化，传入基地址，是否只看楼主的参数
#     def __init__(self,baseUrl,seeLZ):
#         self.baseURL = baseUrl
#         self.seeLZ = '?see_lz='+str(seeLZ)

#     #传入页码，获取该页帖子的代码
#     def getPage(self,pageNum):
#         try:
#             url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
#             request = urllib.request.Request(url)
#             response = urllib.request.urlopen(request)
#             # response.read()取得的为bytes,需要转换一下编码
#             # 使用decode("utf-8")
#             text = response.read()
#             text_uft8 = text.decode("utf-8")
#             print(text_uft8)
#             return response
#         except urllib.error.URLError as e:
#             if hasattr(e,"reason"):
#                 print(u"连接百度贴吧失败,错误原因",e.reason)
#                 return None

# baseURL = 'http://tieba.baidu.com/p/3138733512'
# bdtb = BDTB(baseURL,1)
# bdtb.getPage(1)
__author__ = 'CQF'
# -*- coding:utf-8 -*-
import urllib
import urllib.request
import re

#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()


# 百度贴吧爬虫类
class BDTB:

    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        # 是否只查看楼主
        if seeLZ:
            self.seeLZ = '?see_lz='+str(seeLZ)
        else:
            self.seeLZ = ""
        # print(self.seeLZ)
        self.pic_index = 0
        self.tool = Tool()

    # 传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if hasattr(e,"reason"):
                print(u"连接百度贴吧失败,错误原因",e.reason)
                return None

    # 获取帖子标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1)  #测试输出
            return result.group(1).strip()
        else:
            return None

    # 获取帖子一共有多少页
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            print("共" + result.group(1).strip() + "页")
            return int(result.group(1).strip())
        else:
            return None

    # 获取图片链接并保存图片
    def getImg(self,html):
        # print(html)
        reg = r'<img.*?src="(.+?\.(?:jpg|gif|png)).*?"'
        imgre = re.compile(reg)
        imglist = imgre.findall(html)
        for imgurl in imglist:
            print(imgurl)
            # 直接将远程数据下载到本地
            urllib.request.urlretrieve(imgurl, 'pic/%s.jpg' % self.pic_index)
            self.pic_index = self.pic_index + 1

    # 获取每一层楼的内容,传入页面内容
    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        # self.getImg(page)
        items = re.findall(pattern,page)
        allItem = ""
        for item in items:
            allItem += item
        self.getImg(allItem)
        # print(self.tool.replace(items[1]))

baseURL = 'http://tieba.baidu.com/p/4416960463'
bdtb = BDTB(baseURL, "false")
pageNum = bdtb.getPageNum()
for index in range(pageNum):
    bdtb.getContent(bdtb.getPage(index))