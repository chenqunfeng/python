# # cookiejar获取cookie
# import urllib.request
# import http.cookiejar
# # 3.x版本cookiejar被移动到了http.cookiejar里面
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# for item in cookie:
#     print ('name = ' + item.name)
#     print ('value = ' + item.value)

# # 保存cookie到文件
# import urllib.request
# import http.cookiejar

# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)

# # 从文件汇总获取cookie并访问
# import urllib.request
# import http.cookiejar

# filename = 'cookie.txt'

# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load(filename, ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# req = urllib.request.Request("http://www.baidu.com")
# response = opener.open(req)
# print (response.read())

# 利用cookie模拟网站登录
import urllib.parse
import urllib.request
import http.cookiejar

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
pd = urllib.parse.urlencode({
    'stuid':'201200131012',
    'pwd':'23342321'
    })
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# pd.encode() 需要把string转为bytes
result = opener.open(loginUrl,pd.encode())
cookie.save(ignore_discard=True, ignore_expires=True)
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
result = opener.open(gradeUrl)
print (result.read())