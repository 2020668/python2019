
import requests
import json
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
post_data = {
    "query":"人生苦短，我用Python",
    "from":"zh",
    "to":"en"}

post_url = "https://fanyi.baidu.com/?aldtype=16047"
r = requests.post(post_url,data=post_data,headers=headers)
# print(r.content.decode())
dict_ret = json.loads(r.content.decode())
ret = dict_ret["remote"][0]["dst"]

