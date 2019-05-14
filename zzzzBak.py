from urllib import  request,error
import zlib
from bs4 import BeautifulSoup

url="https://www.douyu.com/directory/all"
req = request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163")

rsp = request.urlopen(req)

data = rsp.read()
data = zlib.decompress(data, 16+zlib.MAX_WBITS)#解压网页
data=data.decode("utf-8")


soup= BeautifulSoup(data)
trs=soup.findAll(name='a',attrs={"class":"ListRecommend-lottery-cell"})

#ListRecommend-lottery

linklist = []
finalLinklist = []
for x in trs:
    link = x.get('href')
    if link:
        linklist.append(link.replace(',',''))

for x in linklist:  # 验证：环打印出linklist列表中的链接
    finalLinklist.append("https://www.douyu.com"+x)

for x in finalLinklist:
    print(x)