import getRooms
import http.cookiejar as cookielib
import  requests

linkList = getRooms.getLinkList()
oldLink=linkList[0]
url = "https://www.douyu.com/room/follow/add_confuse/"+oldLink
rdata = {'username': '用户名', 'password': '密码'}
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "content-length": "15",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "dy_did=76e19147ab11c2268b8cca0f00061501; acf_did=76e19147ab11c2268b8cca0f00061501; smidV2=201904301829138d916d02d066cfc3763e4ae87ea70492008b65c8ffcccabf0;acf_auth=e7cdIJO0wh9k3hFYadWHB%2FVxs2XyoCfDJfm3bdX2vYH5kFK07D%2FPO60HvLooQYAka0ytS3%2Fe2G1g52HT87th0LerQzB8Soq%2BmQHQBGVF%2B8sjvMFQ986FHlE;wan_auth37wan=c8783132bb3c3K0HgVEluir4Fr9b3OCgftJLENAvVeFRCvebW3BafK46pBDuoMRLPcTa%2Baw8%2FlwBwTnLEAE13SWhBSW3q5S%2ByucItZis10Bllg%2FAabA;acf_uid=236732123; acf_username=236732123; acf_nickname=Hab09; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=50092873;acf_biz=1; acf_stk=14b8fdcc2a74c99c; acf_avatar=//apic.douyucdn.cn/upload/avatar_v3/201810/f9801faa3e99670ebd2ac78f51c54ee0_;Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1556620150,1557039993,1557115911; PHPSESSID=jj9r0bt0h1grhohipeqrmra2i5;Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1557115927; acf_ccn=6414563dab5dc50ce09ce8cb2cbc78ba",
    "origin": "https://www.douyu.com",
    "referer": "https://www.douyu.com/1121443",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
rsp = requests.post(url=url,headers=headers)
data = rsp.decode("utf-8")
print(data)


