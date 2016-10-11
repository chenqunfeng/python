__author__ = 'CQF'
# -*- coding:utf-8 -*-
import urllib
import urllib.request
import re
import os

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
    def __init__(self,baseUrl):
        self.baseURL = baseUrl
        # print(self.seeLZ)
        self.pic_index = 0
        self.tool = Tool()

    # 传入页码，获取该页帖子的代码
    def getPage(self):
        try:
            url = self.baseURL
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if hasattr(e,"reason"):
                print(u"连接百度贴吧失败,错误原因",e.reason)
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
    def getContent(self):
        result = self.getPage()
        pattern = re.compile('"(?:src|imgSrc)":"(.+?\.(?:gif|png|svg|jpg))"',re.S)
        # self.getImg(page)
        items = re.findall(pattern,result)
        print (len(items))
        allItem = ""
        if os.path.exists('pic') == False:
            os.makedirs('pic')
        for item in items:
            src = "http://res1.eqh5.com/"+item
            # print (src)
            if src.find("jpg") != -1:
                print("jpg:" + src)
                urllib.request.urlretrieve(src, 'pic/%s.jpg' % self.pic_index)
                self.pic_index = self.pic_index + 1
            if src.find("png") != -1:
                print("png:" + src)
                urllib.request.urlretrieve(src, 'pic/%s.png' % self.pic_index)
                self.pic_index = self.pic_index + 1


baseURL = 'http://s6.eqxiu.com/eqs/page/26320214'
bdtb = BDTB(baseURL)
bdtb.getContent()
# for index in range(pageNum):
#     bdtb.getContent(bdtb.getPage(index))