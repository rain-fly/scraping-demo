import base64

import requests

headers = {
    "accept": "application/json, text/javascript",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=1, i",
    "referer": "https://www.tiktok.com/login/qrcode",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "x-mssdk-info": "9C572o1xcLTYAU1EX.R.MRcLzwEo-Bve3QKBXutbrQIuwjHjuGQrPb1EcLykqdI7AB-aPRIFdObfWkhmrb1xUxj2Xm1sRNOmZ94C3zZg1Kir3JmsS52cbLDIquLNO-uRWXPJQJi6L8G-6JFlHZPSLDrQk.Rk875iMkWlxsgA3YqemVB04KB6ZDLjUBCRzkvq7095bKToSkbm79wQ-x1E.V0N0WYLIi1ugzlIOFt-1Jc-1PzVJCBiPvf2loHV.yigvUv8WEk4PjytmfHUhL7mAk09rcE2XQ-IAaCWp-vmkbhsEfNjuPSasnpCQnQgXICw3q-B3bheQJFS6rp3hHeDIH989-7ElEhUZzJv-E6N7ASvn4g.VL8A6bgX-tu9eEwokON0qGbj-MUz-tGlNvnmLVvSaUoFxAGAaf1S6.AyeMO9aDHrn3B.4msXFAWEaupg0PByuvtuOU86UGWY8iW6sJENQpmohHFln57g1igr87zUza4zLXoe0xGaLdjy5JIsTBFRrd5DbDIIjlPPrbseYZ372gNtiSKphGdzp0zo-couZhu8ruWvQK8wBC8CADioZczJLLfI11l2zQu3e.G9FzZz.lUnviwfadS-zB4YEQiVmlZPRiguDJm74hVk9.r6wvHqJapfb6rnilZVdc4df-Z7Srd3NJbsmLCr8L6jEL902llqhMEGVOaTUGgp7pk9Q5CorYeVfQP-dTstq52e.EqlYVGftsDTXCJ.vCJf-RVMOarnGIIRLmlayxH6gwWbJzrzq2q66dAjzeVml2QtnAhTnJ-P-mrKzto3cDKvmrDLHGoaALkVpQtU7reDt0Cd7-xwLJX0BUsSTiYezJbwU6XybT9MOPxzGH.h4TJmV84HUhGEvQyzXw0FR7ysunoX2CNAeexH.wC7nhy9T5QCCSRks8zbdNeaMxXoz9F-rs9qKEk5dWaMYYRPvo8teUWCGi5UbiUJdoTJ-FFKVqFIf81dnayudg0mReVMM-MV6wwyAQ8HKyeqFthOPPVA.WQVJ8G-hgt5rq8K9RPHXjgtu83ZN.wD.VrY1Dz76VY3FGhvRZWCtBvSgkNG91E5M2EmWznMleqKDvGla.wVVU2fRM9LyUK-69Q3WGXj87tXdJu3oEdM-9Y2r1O2921eTnc42PpZDWnlvlc2BpOqtAjHUHk57qClObSgvP3KMhzuY4samRy6VKDHC6hYAEkl7TrvF05YzHI8kc3nYilsCSSKHNJMNjwXuvhxGAw7mPKusxCSCX.WuIYEMCSKRG8niyy0AvfwUH9bxJpazHkVPaYJh1lFMDtjBnDdKftIwhGVyOXHKaTm4HyOw4F59ppbgYmJ1lcSJl7arHrSngnv097QvJXWoZSkGrnxQ8.8qmrQ.3DRoeacA5kOgRQ5UOW7vP2V69gLqOdqKHAlIvC6KgXG8Oy-yC.C8jVqzrE2qiZwjLkzuRmA4TffXTtHmPvNq-gxVmsx7TcO5dsRioNiuwpnrjzc9hkryV-3BwusH2OZJrjs9x6dv3gQzWj699.Si1gab-Fn5ZY5-LAodUFfxUzPL1MMIz.pqw70I-iPp5mfn00fw1fxCw6z-0d6wUgl.JkKZGEyhjmobOivY7ZHzyAPCLVjw1R7RNeokGQlvvmHBalUcs30yOtKD1V.N1t9-iS--FL.QWIcQFzQdp0s3iR8kchbjbcE6xeU.KKg7Nmysa9SHp5IicLYOyy2GwBunJIoc5Wxf3zzAnwPrmJHuOwCucbOGMWguTYbXk8RDxXcjMRYbkyYfaa4KoVfwC9tl1hq3hYP6skRyNB4.mwbRI-6rgcOTnty2TTLgs94D.UFcmmq6tnau.n3onXAD1E9ZzziMUHjfZtD9.5InIQO8kS8xWVj6SzAcyWBhNE6W8zA-BzmozuQdD1-8HW9yJWVLh.b5OQZOdrQTJVXFQdmKuQ5PX9g.tyLdWAeDXApFcCyIuD-12L0HSQmbSg1.dwKKvGpSZVqk5jAhldGjdqDXCXkzIUXfAqbRGVwpv1kAUEBxI7P4uS7PblbaepuFbpLMmSxeMXQHWFJe3vnCpqDT5W-TdkQrTs18dnkWAQ6E6VEI9GlZe5pXI2WuV9xSTH-P8b.4FXx4Wds5IKf1yZstB9b0KOzEO-yLIRmLQaNs.Skckh6VQcNf2SzuGWtcwRPBeSQ92.fTrOCZp385Gzif6YDnscji6igvx5rhl18djXSWMPg-XgU5-u0RXIyamT-CkvbwGERCes7M7w6utR3.lPtNVTYQvFyJOkiJMb9HB4h7aN1L8pzEbLvWvTzz9EYGdy.AW29QXHfVxYds-CFmFCXkL9kCA1PzHDRZQX5yKLY3AT7Jt43JStNAwWhrRN9sQXFMx-cVQRKzrtXhawA3NTpjYZ0Ew5hDr7NPD70IkrI6WD0gMmd8qwPc-HTOUh1S.2X51ir9NPBtaXXxe-TrkFN9Jczmi7xHLZnXA-KGzlBpmmgQ-MlR5BoEGBKsly6aC10c9BMn5S7tVEtiHHJloJw0R7qiHEMVcxBygzwCawPMvEbtuSBjlPaRajz4iwV.Z2h7uYiUAkj7EE8PiB.oKtuP-CPOIxOjCVsLZ6d5sLkoHjkOfEZhByFlxnOIK.yMVv8D-Rfo2wg-SG4UWJK51cHgMWALmvYld0TVnNlQTnpwzOl6tWT9ZJdeQ.P-gI5rX7BfTVOFMizzooMfid.Dtsei33MJNXUpyCniLN0x3vviTWHBJaXfrVE8MojthCicLTq0CovMWDQVk...CEiJ9jabT0zR5KBYIBqsYy8oeZ743asF-pFpYHjKvYV.BDP5K-TuAEjpC5rrZxZwmj.TvVY2Hw7L6-tCehzVcRCtGWC4WcmgqbeEsJGpMdR6GqzvFBJTbWhF3qCGvBYRkq9CsYgsZZFQZiU09N.BMEMcu889HwnlnRIC6QLcOT5sk00xF637QX2fsTNqQsZd0.ez9S3lp47gY--GvqR4mQdHjKr6IRyNx1TJnO0aJMOcEURSF0JuozDs3cpnPgdqa6LaO2LvP4OEd4uSs-zEetVF1JlmTUaaoTwgI9tbaU6mtLNXlEU55mdKoDLTzSGiZBuaVU6pVRPG.A65Mo-BFqmafhUv2ALFhsl3WfiytQsO4j6O97xjZE7uZxOWBU3LvprLfsjeekhIeg80Snf92S.HXnVDDBqL6ZTDiJoOblUCAErB4M.-8ordMgTwgnMfZYCwTiH-Me1AU4Sb02vW0ggskkpAkg2ZXpaE4mKbn2QW4HlGIe7ktMfmYBQjG.5IsdseGcLs07LPrVDUG1wwAohMLpSu9RjbnjOvri.JOvoZszlWQLUBG3kkFTaxtvKNsSY-JETGfdwxR22TApADyTVg-LBp.AHrTr7LCN.oeXZu0BFvIrGxB4pY5-XpA7bTB5xur6qJhjPDrzkr0rL6jC7C0CMK4sWDLLx5Ody4CtoCwWHKAdPFu.kmt3KxcM3oKD6iI.K53Y8IidBQKdJDHvISl-guhspcnJbRYRCJXkkq8KaXBCKEb6MXqDhnaMGWb.ShQ8U1i00ycqapnQGw8-sQbMGbfeVXfeEa-G4VjusCO0m20SJfRrtnj1EkaW8otJf182YS8b2mlFGMxE.bTkBlr0ccz6EkvK4pyGtlBwNYk5djl9MGa3ptowZE0xD5i5h3Adtq5Ult4w4JN0xA5QgtZWU0rSrSOkV729yya7AIv5j9ea1MoSUw8Q4dMP9P9z8ilikJuiJwdIicmph8aFtUG4lNlD07AgAs2WVAJGBifgAVVg=",
    "x-tt-passport-csrf-token": "2d240575402d00dad428012a2b3a920b"
}
cookies = {
    "user_device_id": "46938665576048ec8c9d371acc12a2c4",
    "user_device_id_timestamp": "1752217667952",
    "_ga": "GA1.1.2042091746.1752217671",
    "FPID": "FPID2.2.f1d5nRJqUogf28JqW18kRfXwqOOROpwi6Z1C78YmBVk%3D.1752217671",
    "_tt_enable_cookie": "1",
    "FPAU": "1.2.1665993014.1752217650",
    "_gtmeec": "e30%3D",
    "_fbp": "fb.1.1752217649746.1116255893",
    "living_user_id": "120413473038",
    "tiktok_webapp_theme": "light",
    "delay_guest_mode_vid": "5",
    "passport_csrf_token": "2d240575402d00dad428012a2b3a920b",
    "passport_csrf_token_default": "2d240575402d00dad428012a2b3a920b",
    "d_ticket": "a61e4383c750d7d44c3c24d079fe370996128",
    "last_login_method": "QRcode",
    "tt_chain_token": "anxlImsb2Q9hIcq07u19Gw==",
    "_ga_LWWPCY99PB": "GS1.1.1755679580.19.1.1755679885.0.0.1476349845",
    "_ttp": "31uUWHsX2IUTynoQ6OqsJWdhN2R.tt.1",
    "store-country-sign": "MEIEDMt4Ilej2_fWjwID0AQgJOKDxr_9QAsnaaBt_2Fjhk2x5NJHrZeBe3kdlr6UXnkEEK6TVUCS2GnM7OOtZXe1kmI",
    "ttcsid": "1756863910108::ZeYDfu8yr63cT44Osvk8.30.1756863925449",
    "ttcsid_CQ6FR3RC77U6L0AM21H0": "1756863910107::MVZDXbt26bWz3l2HdVvL.31.1756863925665",
    "_ga_GZB380RXJX": "GS2.1.s1756866788$o36$g0$t1756866788$j60$l0$h162736664",
    "tt_csrf_token": "xQ084zSq-hQrI8d0Ywx92vrkc6L8urfJhOGE",
    "odin_tt": "2e57794de402af2fdb4ac599465b28b7d993d1c1f8eeff035bb21f7894dde30d4715068980e70cbb974239294d3c02d81dc6ed3ad26d8405b7ba589ee1c0526de19b063d947c645c18079b646f5bd009",
    "perf_feed_cache": "{%22expireTimestamp%22:1757556000000%2C%22itemIds%22:[%227527350407392218386%22%2C%227522456987494337799%22%2C%227519050604887428372%22]}",
    "s_v_web_id": "verify_mf4sx0j8_YNyYr7RP_RHHV_4vEm_9wOM_R7UhIhmH4TWE",
    "msToken": "iYRwOQBQziO1kk6lzT_f4YhlaKbzITUP1QPz5MbHSt-7AYf6MnbfuMyvBtNlyCuC6JNe-PCNDmZNDqqbpexcao-1kre-mf-sVGL1e3uYy4nqJbL_CqlDqbHeaPJh",
    "tiktok_webapp_theme_source": "light",
    "ttwid": "1%7CPMnXP4bK5_JCgucchzpAckvPL_U03IrVHkMVaTa543Q%7C1756957057%7Cf02a3a566a4520954d0014151bfad11f13d2600ea1897153bf79ffcddbc9f808"
}
url = "https://www.tiktok.com/passport/web/get_qrcode/"
params = {
    "next": "https://www.tiktok.com",
    "multi_login": "1",
    "did": "7533529196011882014",
    "locale": "zh-Hans",
    "app_language": "zh",
    "aid": "1459",
    "account_sdk_source": "web",
    "sdk_version": "2.1.11-tiktokbeta.3",
    "language": "zh-Hant",
    "verifyFp": "verify_mf4sx0j8_YNyYr7RP_RHHV_4vEm_9wOM_R7UhIhmH4TWE",
    "target_aid": "",
    "standalone_aid": "",
    "shark_extra": "{\"aid\":1459,\"app_name\":\"Tik_Tok_Login\",\"channel\":\"tiktok_web\",\"device_platform\":\"web_pc\",\"device_id\":\"7533529196011882014\",\"region\":\"SG\",\"priority_region\":\"\",\"os\":\"windows\",\"referer\":\"\",\"cookie_enabled\":true,\"screen_width\":1920,\"screen_height\":1080,\"browser_language\":\"zh-CN\",\"browser_platform\":\"Win32\",\"browser_name\":\"Mozilla\",\"browser_version\":\"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36\",\"browser_online\":true,\"verifyFp\":\"verify_mf4sx0j8_YNyYr7RP_RHHV_4vEm_9wOM_R7UhIhmH4TWE\",\"app_language\":\"zh-Hans\",\"webcast_language\":\"zh-Hans\",\"tz_name\":\"Asia/Shanghai\",\"is_page_visible\":true,\"focus_state\":true,\"is_fullscreen\":false,\"history_len\":2,\"user_is_login\":false,\"data_collection_enabled\":true}",
    "msToken": "ynz6IWfSQoVJvwXxNAoIbgUFaWt3CffukvFN8WvtXstRGrEGGY27gF0PGGFG96kZSOGi0Hp0un4UXhI2YQVkv4hAlwkyNTVckqhPgJsEGh_ceP2qwiZuUZKRer-VkKk43FmG2913lYTiPuNoda5FKTaf",
    "X-Bogus": "DFSzswVY78tANSe7CjH0nV7tKQyz",
    "X-Gnarly": "MO6IYfgpQ0n9vpiD73skqFVnSuTyYk29kyP8i/S0xdaLvdn2CzFZeTwFDhyBefSFWB41gNNpL8H5vJZFzZ5KlmgA5f-yfdPelRgLAccRoJhReawyM/m0StoKR9iWlj6jJAIiEajJ4mC79Jyp0sk3K0CizJDYP8ieK1d6FdGqiufoJDbf4OZqL/geOZf-oawFPUM2jvyef7j/-wCTGkmm/TonujLe3Ljze-hg6l82vD0jIwE8FZIeFHK1mrxBSFstu8CyMs/LcPSfrPSDO1uY9Wd8luQN1OMxwGIAA5XXjsG8"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)


# print(response.text)
print(response.json())
res = response.json()
app_name = res['data']['app_name']
expire_time = res['data']['expire_time']
qrcode = res['data']['qrcode']
qrcode_index_url = res['data']['qrcode_index_url']
token = res['data']['token']
ttwid_migration_ticket = res['data']['ttwid_migration_ticket']


with open('qrcode.png', 'wb') as f:
    f.write(base64.b64decode(qrcode))

