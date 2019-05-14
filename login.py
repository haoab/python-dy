import urllib
import http.cookiejar

url = "https://passport.douyu.com/iframe/loginNew"
postdata =urllib.parse.urlencode({
"username":"1",
"password":"fghc",
"client_id": "1"
}).encode('utf-8')
header = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"utf-8",
"Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
"Connection":"keep-alive",
#"Host":"c.highpin.cn",
#"Referer":"https://www.douyu.com/directory/all",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
}
req = urllib.request.Request(url,postdata,header)
print(urllib.request.urlopen(req).read().decode('utf-8'))