import os

import execjs
import requests

headers = {
    "accept": "application/json, text/javascript",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://live-backstage.tiktok.com",
    "priority": "u=1, i",
    "referer": "https://live-backstage.tiktok.com/login/",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "x-tt-passport-csrf-token": "a906a34a2173cd10c6545263c1e59f9a"
}
url = "https://live-backstage.tiktok.com/passport/web/email/login/"
params = {
    "aid": "6849",
    "account_sdk_source": "web",
    "sdk_version": "2.1.1-tiktok",
    "language": "zh",
    # "verifyFp": "verify_mf2ei3yj_rW0kxKk1_FyCq_49si_By4P_ETLDQH53cH8W"
    # "msToken": "JanwbbLdWRl7MwB7MlM2QnQyJ5XBYko1AYhqkzvcjbM7-42WPGE84UPKdI2JN5Nblg_TEZWYP1-bBY9dsR-EvzKTXGj-IBrI1O-8VPC8N-7cySYx2hhOkq2O9-NUoOmNklbY7Hs=",
    # "X-Bogus": "DFSzswVLX2U-N8XFCjKW5tkX95u6",
    # "X-Gnarly": "MHhiz/15I-q/eyG1qJM0CsKVedPhe41lkx5xyU/L6uEpQIYercbqpwcJM5Yp78PlaXPeu8L5FFM6EAVnBNIn51IYnmZrheJY0RTTTwE6iqfDTYbnXLk/avp9k1sfqtl57xaUvvgXfE8Ic7491kvPTkHp82E06f6KAHLW5bm72/qUqvJ8mdjaxuBV3nj1FJUbahRZcw2q0Q/bgCbiCpYEVmNOb/SvP/RyS/HJbH10JNpfByJjQ0vNYdtLUhqdShztSINAw14zAZWS"
}

# 读取JavaScript文件
email = "test@qq.com"
password = "123456"

current_script_dir = os.path.dirname(os.path.abspath(__file__))
encode_js_path = os.path.join(current_script_dir, "encode.js")
with open(encode_js_path, 'r', encoding='utf-8') as f:
    js_code = f.read()
# 创建JavaScript运行环境
ctx = execjs.compile(js_code)

# 调用JavaScript中的encode函数
signature = ctx.call('encode', email, password)
print(signature)
data = {
    "mix_mode": "1",
    "email": signature.get("email"),
    "password": signature.get("password"),
    "fixed_mix_mode": "1"
}
ses = requests.session()
response = ses.post(url, headers=headers, params=params, data=data)

print(response.text)
print(response)
