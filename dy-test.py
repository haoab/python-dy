from urllib import  request,error
import zlib
import getRooms
import http.cookiejar as cookielib
import  requests

#headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
#header = {"User-Agent": "mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}


linkList = getRooms.getLinkList()
for oldLink in linkList:
    url = "https://www.douyu.com/room/follow/add_confuse/"+oldLink
    req = request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163")
    rsp = request.urlopen(req)
    data = rsp.read()
   # data = zlib.decompress(data, 16 + zlib.MAX_WBITS)  # 解压网页
    data = data.decode("utf-8")
    print(url)

