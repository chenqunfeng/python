# URLError
# import urllib.request
# r = urllib.request.Request("http://www.xxx.com")
# try:
#     urllib.request.urlopen(r)
# '''
# 这里urllib2.URLError的功能移动到urllib的error模块下
# 详细变更可查看https://docs.python.org/3.1/howto/urllib2.html
# URLError可能产生的原因:
#   网络无连接,即本机无法上网
#   连接不到特定的服务器
#   服务器不存在
# '''
# except urllib.error.URLError as e:
#     print (e.reason)

#HTTPError

import urllib.request
r = urllib.request.Request("http://blog.csdn.net/cqcre")
try:
    urllib.request.urlopen(r)
'''
HTTPError是URLError的子类
它是对response做出反应,若连response都没有,则属于URLError的范畴
'''
except urllib.error.HTTPError as e:
    print (e.code)
    print (e.reason)
