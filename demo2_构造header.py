import urllib.request

request = urllib.request.Request("http://www.baidu.com")
response = urllib.request.urlopen(request)
###
'''
在构建request的时候将User-Agent插入到headers中
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
headers = { 'User-Agent' : user_agent }
request = urllib.Request("http:www.baidu.com","",headers)
'''
###
'''
对付"反盗链",服务器会识别headers中的refer是不是它自己,如果不是则可能不会进行响应,
所以我们可以通过在headers中加入refer
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' ,
            'Referer':'http://www.zhihu.com/articles'}  
'''
###
print (response.read())
