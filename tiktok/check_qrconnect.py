import requests


headers = {
    "accept": "application/json, text/javascript",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.tiktok.com",
    "priority": "u=1, i",
    "referer": "https://www.tiktok.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "tt-ticket-guard-client-data": "eyJ0c19zaWduIjoidHMuMS5hYTRhNzM5ZjE0ZTcyNjZmNDg2YjUzZDZkMWNhYmMzM2NjYmZkOTRlMjZiZTNjODc4OWMxOTIzNzExMTE2ZDc4MGU3MGI0YmRhODJjMTM4MzZlNWNmYTE4Mzk0ZDcwMjQwZjhhZjE2MzFmMTY1YWU5NjAxMjJlZWZmZDQ1MzNkZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJNRVVDSVFEaEsrcUprVzdFQzNmWjY1ajZMYzh0REhEMk1PNnRqN0JhejBuL3owcnJHUUlnS1I3WU5Wd2pESS9zZlpMUWk2eUlNNHIyWWFhc1BiMXVLZ2FVcU1QU24rcz0iLCJ0aW1lc3RhbXAiOjE3NTcwNTAzMzV9",
    "tt-ticket-guard-iteration-version": "0",
    "tt-ticket-guard-public-key": "BIKw4jpfVA8VE/YqiiuhBpcCj+jgHtMfU2aYSW3kjdAhjak+QI9nMGQaY7Xjpg1wu02KOVBBt33o224weaNADaU=",
    "tt-ticket-guard-version": "2",
    "tt-ticket-guard-web-version": "1",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1",
    "x-mssdk-info": "AdK24IBZoHLGQWXe9kq-uI3Vr-Lo1uaSe8yGIzXbWvoX5HML21oBc4iC7McBHxJ7qN31hF5JsI3tVOO0zQKS2av0XRJUxBs91bmuE9MkQMMsunqNRLz.tSz-a-tg56LTy5JWlb5KMe-U38rt8Qbu4lbCTmQuEKLwmnTvjrj-LANqAiyMphnFGiCdCnyqDzLtGqIvgDPdb7I3.jlSBA4by7ktyZKglYLzxwcyhGHppyDtFG-Z9MlVuf6MMTZ2zM9EZK1m7VDT.-FzxEZ1JvirK-wyHMUUl.dN2-AkN6Ply6K0b13LCxx.ftRI.hf7bGbRiRECMJyyi-IHKXVpwiHIT2XiwWf0Ts42.oVsS1bxL5Smmtr1giTJ7bTFIz60y6HMtn4OF-6FsG5JQ4A16wxLlB8MobJpIXR6wLhTIE9f4d.qyWkzqoWVQbvBxxW8SwprXQ4T.R6QFU6kl9kpPscZVESlZw9G18XWJbJwJCvGUbTUw3NN7DAYJ.-K6WB3sRXqEoWlD9J-bEf9ofYEd6m7sJ8qXvuhGVBiKq3Z.HCWECueiAtvV0P5-dyeKPk3oh24gVBtTmWhAhXNuqckF7iDPxBby5BSLBPi7JyWPFug55UFCexTLi0rCC88vQ6es1FqSkQp4OO94EwVM9Mh.GXtPhiT3qiND1STxluncWmSEl8nOE70Mg5H6rL..kwbgectho-8T5WsFATxQc1BcpXK0zdyPe5yVP3HmBdUhvNxkJAOIly9ii4RS9FTVQGcSaIMI2qIIMcatfUMrezacTLK1Nf2BJBu-EakMIdSddmlDJC.Qxhs9zYfslvzk4.HoEIHnkwsIA9QvXqMZVoM5kJoGCXFVgZR5kACwzYdbF9wI1SwXuAQjhxJCfIbCKbqIF5SaWQPrcx2hGQ9MnDc8w7mGT.Cj8H6X4rp1.fWe8BukWwuMLGjOK-UIi2s19T0RD9Rf6dZjXzmCWDwZaPBYxsqQ.z6T09.pmSCBzRTqKNxDqUSWapRcSyBr6Xpl.53fPMef12s9yH0TmMJ5-FGyykdAEiSsgV39UVw0OQExEqomI9eIuYD.lQBeC.c0Zizzh1Jjk5ovxcpwEL1aefeh1t2wvdEwIrSibQMsRZUx3xEyrznakk-N6.VpPL9SVpDB8FBqAqUnroqzbOGvTyHwNwpmEg1TFfuAxyBe8mLFFt6C6.5n3GFw.6Lmi-eXECTtLRvtls-nezv4e5OLnWPKXkVONfhlVF2lDcQBZb8IIzVDiBn3h.gWCffhgcfu33.7ymtgrhzOy.zDgOeDcyyfSLXq.CPpXw3xfoKVN8McztwAFqUeUefyYdg19gntTlsj-NZt7khof0VqZJxTEtJDk2a6jWbEFRq7Jm-bbqsDh7Pkwdi.6TWsJweZc7wqtkoBsWB9Ei.VS-J0Dqj8D-2VzeA-L7PQTl6Cg61BdEH016iEU7U0xaMAV8Sl5Z2U3z2ia1pzUfdRD404zRrjpJnd6s.QWRCfiH60Fgo1kZOPLsCMrb89w7cxuJ8Yw2bxe76JR5gjCAD2w1wHb4zZgIrpkGDaDaGk8SHLdwEye0-A7VMgV80HdNQ2raCqwnsQLBKGh1SnlFfOXLutySqJky-0zK6G6sZDS8W7-z2gmKw8l6O08WiJOIpjr797PtDM5w7FWwCxCEXPn9Y8PTUv1CosgHlfP6V3apiviTJkp7-FC3.Dqz9k3Nr.4N.60jDY0QmR5tqPOaQxE37hUCpGPQom-OfbYF3AYTLvWBwv4UnkdJN2S8SAorSX2Y.mbYal3JC0Exu2ByjqrWWIGOLcN-SrWaGuZsOXJjRI.IEOjP2yitCxrQ85WxG9Ogu7uEcuz4aqvnYZ-l20vxdQLmebKU-twdKHs1f11zzOdKrKJyBoOm7Gn5YamBIYXZctj41BAVAwa8FiEZEUCSKynE80MWLMaGSNJ8BasHh6474lC.nHev4vcTpGymmje6butT.ATs6opQ3Xo7bSas9k03vRWe7pTCoLR6jR8gQcIKM3ijpji2z2ryrGaPVojlYUKnyoWAqJRlPC9Wpcag.gwVxbqnxbrtuunAPWw9vfl.7eecf3vkkGM32-zq3WHL5N81bk-3m5gWbG88C41zOfVQJktlIkgmZhlkIPP0-lWMZg7Z4ntPXfFU4NWbLPyQeaW2P2rgEo.YzkC1j2LhTMybt7wsfJoV8g-.Nxo2tktdidfNNNa9UJFy2Fl9FU9cwHwLrHkmdjEk5A6bx3RxbbV4JFuVlY03KF5ML93uGjVS8AwkzhSfFvKXa8YHbi5xoXC5CJf5alsrfFF7z6iMq9gBU7e2uD-kHIOcLGffIkrZnQjJPqzb.YNMeA.KM5AtZrHwRditbFFLPbCGRL-yoWRy.yaMPaVSJ.G8IkW9kFpbo4jqSKUKQARvtv63a.ufgNzX-rXFNJO9hUjey-5Z2YlApWXoW1-gBaYA7Vqg6b1VsvU-jxbnfPhLJEljKFzr8dMTzYaHhbCTKVv5cHYnKCCNcE9ZcvgcdXJLYlKwqLYWSPnFz5pwai5Gj.gF2fAMidU.UsgGU9jqez0e0JjL2OTleLMNCS2FdKkX.j.yg2Z7qJq6g3okBNCZ0mkhGUsRSUw434DcR-f.wLbusFkumuXnuGDQGnJ8Vb89gSXuYK3iTbGVTfrC4kCeyDvKgBp1ifRIDPAWRHATOEoPe8ZndHvd5BB1fnD08aLnUYh2YLMq6Zk6Vxa8m6KIg6zeAapZ3XzPfAitTpQu7ICQNUYmjhF94CX64t54XzK29m2RccAqoNgGqfbxpVhSxMLYESQBQdoM0fHzVQxcXmiLZWSoN6TqIZnHDOicFbIY230-oS8VaeOEf.SYC8iHEwaGkXhaoP-5qqMKkT13fi6jgkigN-h3I1m15muoWxhgip6fXsxK9V4i2w8WPB-q.FbpELnJd8G5JsL6mVpR.jx.SOKq373CDES2rDKWwBZXjMKr7v5FKwEx9rrg2jbCZKIxTMYxw0y3-sUKyaVRrSv7naIMy5mPrhNeIzPXcdmmCR4wYp4aY51vLidsCg4S9KCedcj7Oi7HX.aDW7LZcNxIeJ8Oe8ZI1LKIz-mAxbNEsefDO0nuuKbJe-34RO8m8.enhBGfokWHLTL8N4jU5A7cnQ1wlr-8H1.WrB74LfKdWi..Mq-Mnzudd7UhMDUQ3iCEXB03I8kQVLttcNKqlRtXznD2NHh9DZVLVppm8EjBBu5IxA.AHC9QZkb.05GZLeezh0lZCoQkTt-36OR8u9BI65b7YFm5GM7PwXTk0sEnNIBsMXl6kpQ.VjvNHAcNVsQSDoaE1PnQ4nKnPBdL3Io5JfkzGcyG2kJZZxgtY5CMFzA0RWz4=",
    "x-tt-passport-csrf-token": "2d240575402d00dad428012a2b3a920b",
    "x-tt-passport-ttwid-ticket": "AZUCrV_02kl_nHpI6qdZ3v0sxEwFYw0HPK1BvxoxUhqF9KF9borXyeWWbhsIvIFLAA=="
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
    "passport_csrf_token": "2d240575402d00dad428012a2b3a920b",
    "passport_csrf_token_default": "2d240575402d00dad428012a2b3a920b",
    "d_ticket": "a61e4383c750d7d44c3c24d079fe370996128",
    "tt_chain_token": "anxlImsb2Q9hIcq07u19Gw==",
    "_ga_LWWPCY99PB": "GS1.1.1755679580.19.1.1755679885.0.0.1476349845",
    "_ttp": "31uUWHsX2IUTynoQ6OqsJWdhN2R.tt.1",
    "store-country-sign": "MEIEDMt4Ilej2_fWjwID0AQgJOKDxr_9QAsnaaBt_2Fjhk2x5NJHrZeBe3kdlr6UXnkEEK6TVUCS2GnM7OOtZXe1kmI",
    "odin_tt": "2e57794de402af2fdb4ac599465b28b7d993d1c1f8eeff035bb21f7894dde30d4715068980e70cbb974239294d3c02d81dc6ed3ad26d8405b7ba589ee1c0526de19b063d947c645c18079b646f5bd009",
    "tt_csrf_token": "zMvva88T-zeHv_rxWkuG-F98vYmHum_sySzM",
    "s_v_web_id": "verify_mf6401e0_MwapnxlK_vsYI_4vZ0_8BZ7_Jrt883ynWwIX",
    "ttcsid": "1757044513524::LV8PkRMMBGoBaq5dNftP.31.1757044513783",
    "ttcsid_CQ6FR3RC77U6L0AM21H0": "1757044513523::-77pLDrFk97E_Carebal.32.1757044514096",
    "FPLC": "doBThgEe%2B0gsJgoY9mnwlyAsUAOh1yfHyGY1Z7uIsyiVnPgxiIPkcV1W1LH75Bmj5HVgtCjgz2x%2BThoyZMRjY7WQ9br1iGvhdd27766lF9WIJVCCa6aMWoIG1Nd%2FYw%3D%3D",
    "_ga_GZB380RXJX": "GS2.1.s1757044512$o37$g1$t1757044514$j58$l0$h1058111406",
    "ttwid": "1%7CPMnXP4bK5_JCgucchzpAckvPL_U03IrVHkMVaTa543Q%7C1757050295%7C2497a2491377882860ada2e4cb0321b75f5e913487f7d251e7756a909ffa5100",
    "msToken": "6Qxv-6Ntpr0LFC5FYDb6UQMVIy2nfvRqzXy8svHvxrY5NnBm3HyEZyaQK4dQTd3HMV--PcHbHwzgATgZ489Q68zs9Skc0v-PXRcdYGlZC4c_rCuqNEebIEeiAnqFxPsjjDsYseibkvnLG7T7big39Epj1fkGaA=="
}
url = "https://web-va.tiktok.com/passport/web/check_qrconnect/"
params = {
    "next": "https://www.tiktok.com",
    "token": "H1onHXvAS9OH99s7e-CZ_gqyGvcZomOsXMYD3pyn9zM=_sg1",
    "multi_login": "1",
    "did": "7533529196011882014",
    "locale": "zh-Hans",
    "app_language": "zh",
    "aid": "1459",
    "account_sdk_source": "web",
    "sdk_version": "2.1.11-tiktokbeta.3",
    "language": "zh-Hant",
    "verifyFp": "verify_mf6401e0_MwapnxlK_vsYI_4vZ0_8BZ7_Jrt883ynWwIX",
    "target_aid": "",
    "standalone_aid": "",
    "shark_extra": "{\"aid\":1459,\"app_name\":\"Tik_Tok_Login\",\"channel\":\"tiktok_web\",\"device_platform\":\"web_mobile\",\"device_id\":\"7533529196011882014\",\"region\":\"SG\",\"priority_region\":\"\",\"os\":\"ios\",\"referer\":\"\",\"cookie_enabled\":true,\"screen_width\":414,\"screen_height\":896,\"browser_language\":\"zh-CN\",\"browser_platform\":\"Win32\",\"browser_name\":\"Mozilla\",\"browser_version\":\"5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1\",\"browser_online\":true,\"verifyFp\":\"verify_mf6401e0_MwapnxlK_vsYI_4vZ0_8BZ7_Jrt883ynWwIX\",\"app_language\":\"zh-Hans\",\"webcast_language\":\"zh-Hans\",\"tz_name\":\"Asia/Shanghai\",\"is_page_visible\":true,\"focus_state\":true,\"is_fullscreen\":false,\"history_len\":6,\"user_is_login\":false,\"data_collection_enabled\":true}",
    "msToken": "YU0UF0Mo1zz2lrEoztz-Wuhl6Ac1ErDNJcc5fLRnf4byaYGQgwUGkJl4xY2vMAIyreKs3rw5vHL6WFq5jY0EsyTpgPmtth8kLSEojnsgTqFpytdr7EBtveht0YnQ3BchMkZnfq2xdf8OQj13fDbo-dLLy7X9Lw==",
    "X-Bogus": "DFSzKwVO7rmXtisvCjcn3Y7tKQHG",
    "X-Gnarly": "M82BN1XNSSDoZ-kPIigT9MCUXe/vQUJ3eAUEH6HOkX1mHpcvj09JQPukLTHn2yzNmwjqr6K0w5x7crL66Q4zk2vBi-DiHyavo65Y3z2zLlPWSGLkZZ/GQDmx26GzE0ryIEYGL69b156zqg6W0c/YLX2a0ekF/E7pvXbZX23-ug0nGT1XN9wqWMkYjcS5GYlFTRqLIZVsIQdUZQAWekikA3Tx5Edx5xjEBHfgTKxLKDS6XyKV8YitiWlrZFGeeYRNlkfGt9iY3g-DasRmHCXlOTdqNPMRWI5OlJAHnrHcgvMO"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)