import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://tysf.cponline.cnipa.gov.cn",
    "Referer": "https://tysf.cponline.cnipa.gov.cn/am/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "SESSION": "e5f58914-321a-46d1-99b5-3f32fb66fe93",
    "user_device_id": "b1ff67ca8a764130b0aa9bee94c9da73",
    "user_device_id_timestamp": "1746872078962"
}
url = "https://tysf.cponline.cnipa.gov.cn/am/captcha/check"
data = {
    "captchaType": "blockPuzzle",
    "pointJson": "{\"x\":195.3,\"y\":5}",
    "token": "6582e83522eb4010bb40eea9e65f0437"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)