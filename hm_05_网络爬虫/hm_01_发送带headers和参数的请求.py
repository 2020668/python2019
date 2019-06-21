# coding = utf-8
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

params = {"wd": "传智播客"}
url_temp = "https://www.baidu.com"
response = requests.get(url_temp, headers=headers, params=params)
print(response.status_code)
# print(response.request.url)
print(response.content.decode())
