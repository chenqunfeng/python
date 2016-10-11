# Proxy代理设置
import urllib.request
enable_proxy = True
proxy_handler = urllib.request.ProxyHandler({"http":"http://some_proxy.com:8080"})
null_proxy_handler = urllib.request.ProxyHandler({})
if enable_proxy:
    opener = urllib.request.build_opener(proxy_handler)
else:
    opener = urllib.request.build_opener(null_proxy_handler)
urllib.request.install_opener(opener)