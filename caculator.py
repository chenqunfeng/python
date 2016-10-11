__author__ = 'CQF'
#coding:utf-8
import urllib
import urllib.request
import re
import os
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("CQF") # 标题
root.resizable(width = False, height = False) #宽不可变, 高可变,默认为True

class App:

    def __init__(self, master):
        self.top = Frame(master)
        self.top.pack()
        self.bottom = Frame(master)
        self.bottom.pack()

    def render(self):
        Label(self.top, text = "抓取链接").pack(side = LEFT)
        self.url = Entry(self.top, bd = 5)
        self.url.pack(side = LEFT)
        Button(self.top, text = "抓取图片", command = lambda: self.getPic()).pack(side = LEFT)

    def getPic(self):
        url = self.url.get()
        print (url)
        print (url.find("http://h5.eqxiu.com/"))
        if url.find("http://h5.eqxiu.com/") != -1:
            print ("易企秀链接")
            tool = Tool(url)
            tool.main()
        else:
            print("不是易企秀链接")
            # messagebox.askokcancel('Python Tkinter', 'askokcancel')
            # buttontext.set('askquestion')
            messagebox.showinfo(title = "Python Tkinter", message = "不是易企秀链接")

class Tool:

    def __init__(self, baseUrl):
        self.pic_index = 0
        self.baseUrl = baseUrl
        self.deeperUrl = ""

    def getBaseHTML(self):
        try:
            url = self.baseUrl
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if hasattr(e,"reason"):
                print(u"连接失败,错误原因",e.reason)
                return None

    def getDeeperHTML(self):
        try:
            url = self.deeperUrl
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if hasattr(e,"reason"):
                print(u"连接百度贴吧失败,错误原因",e.reason)
                return None

    def getDeeperUrl(self):
        baseHTML = self.getBaseHTML()
        pattern = re.compile('id:(\d+?),', re.S)
        _id = re.findall(pattern, baseHTML)[0]
        self.deeperUrl = "http://s1.eqxiu.com/eqs/page/" + _id

    def getImg(self):
        deeperHTML = self.getDeeperHTML()
        pattern = re.compile('"(?:src|imgSrc)":"(.+?\.(?:gif|png|svg|jpg))"',re.S)
        items = re.findall(pattern, deeperHTML)
        for item in items:
            src = "http://res1.eqh5.com/" + item
            _format = "error"
            # 判断是否为jpg格式
            if src.find("jpg") != -1:
                _format = "jpg"
            # 判断是否为png格式
            if src.find("png") != -1:
                _format = "png"
            # 判断是否为gif格式
            if src.find("gif") != -1:
                _format = "gif"
            # 判断是否存在pic文件夹
            if os.path.exists('pic') == False:
                os.makedirs('pic')
            if _format != "error":
                # 保存图片
                urllib.request.urlretrieve(src, ('pic/%s.' + _format) % self.pic_index)
                self.pic_index = self.pic_index + 1
                
    def main(self):
        self.getDeeperUrl()
        self.getImg()

app = App(root)
app.render()
root.mainloop()
