import urllib

# 构建一个已经登录过的用户的headers信息
headers = {
    "Host":"www.renren.com",
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    # 添加抓包获取的cookie，这个Cookie是保存了密码无需重复登录的用户的Cookie，里面记录了用户名及密码等登录信息（我这里只显示一部分）
    "Cookie": "anonymid=j5xitrrwqgbk8; _r01_=1; loginfrom=syshome; wp_fold=0; _de=BF09EE3FED92E6B65F6A4705D973F1383380866D39FF5;"
}

# 通过headers里的报头信息（主要是Cookie信息），构建Request对象
request = urllib.request("http://www.renren.com/", headers = headers)
# 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息），判断这是一个已经登录的用户，并返回相应的页面
response = urllib.urlopen(request)
# 打印响应内容
print(response.read())