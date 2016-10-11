# 关与urllib和urllib2之间的区别
# http://www.hacksparrow.com/python-difference-between-urllib-and-urllib2.html
# 在pythob3.x中urllib2被改为urllib.request

import urllib.request
# urlopen(url, data, timeout)
# @param {string}  url     操作的url
# @param {any}     data    访问url时要传送的数据
# @param {number}  timeout 超时时间
response = urllib.request.urlopen("http://waimai.meituan.com/restaurant/244362?pos=0")
'''
以上代码等同于
request = urllib.Request("http:www.baidu.com")
response = urllib.request.urlopen(request)
两者的运行结果完全一致,只不过在中间多了一个request对象
而这样写有一个好处,就是你可以针对request加入额外的内容
'''
# 在python3.x中 print "hello" => print ("hello")
print (response.read())
