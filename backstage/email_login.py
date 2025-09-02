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
cookies = {
    "tt_chain_token": "vIqPnSyqYE2xNzU6ZMVl8w==",
    "user_device_id": "19a395660f8b458c8b3f78d2871e9898",
    "user_device_id_timestamp": "1752065596445",
    "passport_csrf_token": "a906a34a2173cd10c6545263c1e59f9a",
    "passport_csrf_token_default": "a906a34a2173cd10c6545263c1e59f9a",
    "multi_sids": "6962746809756681222%3Af7e94b6787d856e9594540ec6d108f0a",
    "cmpl_token": "AgQQAPPdF-RO0rCeS_LYut0_8g__BX6Yf5zZYN4KMg",
    "uid_tt": "6dae30134a1c3d0c2b14a4d1550d7fbe2cd5c4417093da25b1524baad3c4b527",
    "uid_tt_ss": "6dae30134a1c3d0c2b14a4d1550d7fbe2cd5c4417093da25b1524baad3c4b527",
    "sid_tt": "f7e94b6787d856e9594540ec6d108f0a",
    "sessionid": "f7e94b6787d856e9594540ec6d108f0a",
    "sessionid_ss": "f7e94b6787d856e9594540ec6d108f0a",
    "sid_guard": "f7e94b6787d856e9594540ec6d108f0a%7C1752065680%7C15551975%7CMon%2C+05-Jan-2026+12%3A54%3A15+GMT",
    "sid_ucp_v1": "1.0.0-KDgwZTE5NTEwMWRiZDc3ZmM2NzZhM2Y3NWQ2Y2VlMDk2NjIyOTUyZjAKGQiGiKCE1aqp0GAQkM25wwYYsws4CEASSAQQAxoCbXkiIGY3ZTk0YjY3ODdkODU2ZTk1OTQ1NDBlYzZkMTA4ZjBh",
    "ssid_ucp_v1": "1.0.0-KDgwZTE5NTEwMWRiZDc3ZmM2NzZhM2Y3NWQ2Y2VlMDk2NjIyOTUyZjAKGQiGiKCE1aqp0GAQkM25wwYYsws4CEASSAQQAxoCbXkiIGY3ZTk0YjY3ODdkODU2ZTk1OTQ1NDBlYzZkMTA4ZjBh",
    "FPAU": "1.2.838708523.1752065989",
    "_fbp": "fb.1.1752065989095.1849745650",
    "_ga": "GA1.1.130821806.1756542370",
    "FPID": "FPID2.2.a%2FedsArHfjJ5wd%2B8TOcesCaACftyVOOt6CwaEiDcOiE%3D.1756542370",
    "_gtmeec": "e30%3D",
    "_ttp": "2ud8ZCZq7tNXBWzDXTMPB001W4U.tt.1",
    "_tt_enable_cookie": "1",
    "d_ticket_backstage": "b0ccffa1a6cd5e0541031774e1d7890e9a309",
    "sid_guard_backstage": "143adb7fc52a7be8673ab04710d3b9fe%7C1756542374%7C5184000%7CWed%2C+29-Oct-2025+08%3A26%3A14+GMT",
    "uid_tt_backstage": "8bce5a960fe0be8336ce2a31352d5979af045c1abc15754a537d5242e3f8f2b7",
    "uid_tt_ss_backstage": "8bce5a960fe0be8336ce2a31352d5979af045c1abc15754a537d5242e3f8f2b7",
    "sid_tt_backstage": "143adb7fc52a7be8673ab04710d3b9fe",
    "sessionid_backstage": "143adb7fc52a7be8673ab04710d3b9fe",
    "sessionid_ss_backstage": "143adb7fc52a7be8673ab04710d3b9fe",
    "sid_ucp_v1_backstage": "1.0.0-KDdkZTZmZmMyNjBkMmY3OTZiYWQyNWM0ZTg0MTJhOGFiNzRiNGVjYzYKGAiQiLHo0eC1wWYQpuvKxQYYwTU4AUDrBxADGgJteSIgMTQzYWRiN2ZjNTJhN2JlODY3M2FiMDQ3MTBkM2I5ZmU",
    "ssid_ucp_v1_backstage": "1.0.0-KDdkZTZmZmMyNjBkMmY3OTZiYWQyNWM0ZTg0MTJhOGFiNzRiNGVjYzYKGAiQiLHo0eC1wWYQpuvKxQYYwTU4AUDrBxADGgJteSIgMTQzYWRiN2ZjNTJhN2JlODY3M2FiMDQ3MTBkM2I5ZmU",
    "xgplayer_device_id": "66697843629",
    "xgplayer_user_id": "745237432152",
    "tcn-target-idc": "alisg",
    "s_v_web_id": "verify_mf2ei3yj_rW0kxKk1_FyCq_49si_By4P_ETLDQH53cH8W",
    "FPLC": "an12wEnv6brVYjXCvmJhrai2zAt831Or1Xq%2BUK96PJAcKguslj79nq%2BI5sFpjwAdxmg4HBXGdV5d3gMwUEvcOxl2W%2FsDYArdr04ZpgzSfXO1OIhESW6YSe6WWgAc8g%3D%3D",
    "ttwid": "1%7CUGCrf5UMm_eGbSW99ykPbT7YVLQQz8_DDcInfLJXqtc%7C1756811187%7C6563854eca0ffd746c3f038cea1ef58c058051f549d4021f35c9cd1265472200",
    "_ga_GZB380RXJX": "GS2.1.s1756808639$o2$g1$t1756813047$j59$l0$h1230083074",
    "msToken": "JanwbbLdWRl7MwB7MlM2QnQyJ5XBYko1AYhqkzvcjbM7-42WPGE84UPKdI2JN5Nblg_TEZWYP1-bBY9dsR-EvzKTXGj-IBrI1O-8VPC8N-7cySYx2hhOkq2O9-NUoOmNklbY7Hs=",
    "ttcsid_CQ6FR3RC77U6L0AM21H0": "1756808640396::Lx9GAr32lOMRzZDUr2LX.2.1756813316108",
    "ttcsid": "1756808640397::m8yieXxwSDx856ixjKxs.2.1756813316109"
}
url = "https://live-backstage.tiktok.com/passport/web/email/login/"
params = {
    "aid": "6849",
    "account_sdk_source": "web",
    "sdk_version": "2.1.1-tiktok",
    "language": "zh",
    "verifyFp": "verify_mf2ei3yj_rW0kxKk1_FyCq_49si_By4P_ETLDQH53cH8W",
    "msToken": "JanwbbLdWRl7MwB7MlM2QnQyJ5XBYko1AYhqkzvcjbM7-42WPGE84UPKdI2JN5Nblg_TEZWYP1-bBY9dsR-EvzKTXGj-IBrI1O-8VPC8N-7cySYx2hhOkq2O9-NUoOmNklbY7Hs=",
    "X-Bogus": "DFSzswVLX2U-N8XFCjKW5tkX95u6",
    "X-Gnarly": "MHhiz/15I-q/eyG1qJM0CsKVedPhe41lkx5xyU/L6uEpQIYercbqpwcJM5Yp78PlaXPeu8L5FFM6EAVnBNIn51IYnmZrheJY0RTTTwE6iqfDTYbnXLk/avp9k1sfqtl57xaUvvgXfE8Ic7491kvPTkHp82E06f6KAHLW5bm72/qUqvJ8mdjaxuBV3nj1FJUbahRZcw2q0Q/bgCbiCpYEVmNOb/SvP/RyS/HJbH10JNpfByJjQ0vNYdtLUhqdShztSINAw14zAZWS"
}
data = {
    "mix_mode": "1",
    "email": "716076714574742b666a68",
    "password": "343736313033",
    "fixed_mix_mode": "1"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)