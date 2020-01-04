import urllib.request

url = 'http://www.baidu.com'


url_headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"}
# HTTP头部，用头部信息伪装成浏览器
# 注意传参方式，headers
url_request = urllib.request.Request(url,headers=url_headers)
# <urllib.request.Request object at 0x000002167E23BC88>

url_request_open = urllib.request.urlopen(url_request)

print(url_request_open)
print(url_request_open.status)
print(url_request_open.read())
