import urllib.request
import json

#获取room
def getLinkList():
    linklist = []
    for value in range(1,10):
        url="https://www.douyu.com/japi/weblist/apinc/rec/lottery?num=4&page="+str(value)
        opener = urllib.request.build_opener()
        data = opener.open(url).read()
        data=data.decode("utf-8")
        json_data = json.loads(data)
        roomDatas = json_data["data"]
        for roomData in roomDatas:
            s = str(roomData["roomId"])
            #linklist.append("https://www.douyu.com/"+s)
            linklist.append(s)
    return  linklist

