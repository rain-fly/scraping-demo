import requests


headers = {
    "accept": "application/json, text/javascript",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.tiktok.com",
    "priority": "u=1, i",
    "referer": "https://www.tiktok.com/",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "tt-ticket-guard-client-data": "eyJ0c19zaWduIjoidHMuMS5hYTRhNzM5ZjE0ZTcyNjZmNDg2YjUzZDZkMWNhYmMzM2NjYmZkOTRlMjZiZTNjODc4OWMxOTIzNzExMTE2ZDc4MGU3MGI0YmRhODJjMTM4MzZlNWNmYTE4Mzk0ZDcwMjQwZjhhZjE2MzFmMTY1YWU5NjAxMjJlZWZmZDQ1MzNkZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJNRVVDSUdyUWlJMzJ4TkNOKzU0T3RZb1VPVDRHckRaUzJzclZIaEtNcjIzVk1IT3JBaUVBdTdwbm1jNTdPaDFLMXE2M1dVUWQ0V0ZaNXFnS0V1K0RySmFJSzBCdEU1dz0iLCJ0aW1lc3RhbXAiOjE3NTY5NTcyODR9",
    "tt-ticket-guard-iteration-version": "0",
    "tt-ticket-guard-public-key": "BIKw4jpfVA8VE/YqiiuhBpcCj+jgHtMfU2aYSW3kjdAhjak+QI9nMGQaY7Xjpg1wu02KOVBBt33o224weaNADaU=",
    "tt-ticket-guard-version": "2",
    "tt-ticket-guard-web-version": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "x-mssdk-info": "wpGOvxBfyMYWRENxt3D2ZKSdmAifjEPh54jWstuimJhb0-nZ1sNns.00bO98qU7C06xgoczHzEiHI7sS6IDXDdczG2.E03ny0rLaqczEqzRUKbHGhfdWgoLaVuZ4HvyfaQeD33rj7R.m3jvZbHqjzONPccmvbDXAVBVYVBPz5IsS0JwHKca8xjhdFTDXUIU.sJpodvQqHF9b.qdfWFY4m9zecVy6tbNu7nuQMcgZK2rKVEb4Ylw0egzgMrYyT6BQJPrjGJdqRMDs8VVGd02OkBMESkdjw.FRJJvPYHxlrnaGZSz1GJadfYkyGmA3y3l2lRlLRWi7ecGIBqzSHQHaz3blc64dZbQXY-9POVJ9w9xTUo6EOHEpxW7n-4nB6b.7WStRBdAGNgEXqf101FI8YUAuf5YZzi19CiSEJtZ6zCWJg7-FJnNI.NnABFAR6OHm2qvq34k8SdWGf.ktK1uaqy5jdfPVMPsxasjeHVcfVBeYzgjTjhEPRXrFip.OqGCIaHjXdTq7ODHdBxtw6q0QxHO6FNtuushTY-hKAZb2.NtnFXgk3D65ETUysNHLESw6PYyUCo0mZ2SE.1zUW3kHRChCwFSALHzzj3xCVl7CL-HmZyZD0Hl5xPMh5SQyT8vpzmDN95.dfuezVzBXgJE4q.zYLBebkIxt4D8eIs-pVijX7CZ-uN5qwEEBpjS5YxKFbiFfMH4GO1PXcMcurcbt2vaZqNiX361c9PVZ.OkAN2VaLNKeLq8TZqVYNdshF1V50zfYgSWz-157GzY8dOwGm0XMmPwzCH-MNnWeiipsAb9R833aV6UXgk9ott2z.DTfp3frDPxruPxMkmEoml1B9yc4RSwwBT-o9FdLSrVDu5wL-7qWtIn6PIzMLeHiwPPcOJrohtfJcghMqIIlO8-rsF8kjsrqaXrkfF5ftVdWYU7GIZLSIfyLuQO5E13i91W5nafqa1OEUlQwGwIQmCYRZ1MdhvrERJgoRBMjlWwof-CX2C5fCRjEIPt15BO2gLD7dH9.0EHyOmBDaiRpR6NAF4ufwLFFpLrDRLc.pIivgTidZ499afPaMADgU-zPSUyN6dpzD7Lvd9bN6Puit-wq1131gvHWyffyjRrnC-EgKiHuwjywig1l7YVRTDLqdWE8.XJtVdcAejAEqdLn0nDqvYQFeJS7FqFnJ2fUcfxSiryYVpf59auP.Fe7EDDAr7BcLM5H8oVWzsgqOrqTo7.7Aowu8ztHkM6rp2cpAST-bqxsQ0dJuQrnIxsyU-gw5vgDuOJ0A6j5t1WBIDt.qALroqczo-WyH1WN2J6bx4EbsJUO8LbVpd1Gu4u1geWkLDMeJ.Osy9aN-98beLj27SNL8oIaJ7TFjxIm5JnapQhelSWjADyRE9rNjNcrta0CC6GnLgyjggdSPadWaRecvwIPhdZhmfcYDl9nZgU0YsvRTWgvmypIdBpOR.knuYC9rBBThaDDn6a4mAKbYBCmuNKaIhiRxZdIIrSp313xBUOnDkhXKqDpy-.kKrkydN3qioAqX0jK9LPuwjaIzqYcm3ZChwfAMfr7PMTsZOPCiufkPxtdphp8I8QDQtxxL3zmgj8HXvomV7B7jTZ-N.agOgTYJubnyCswwjuynQyeZar.64AljvI20USbu2jJ7EvMsaf7mGC4OKAOOjZHbheSL6WO7wVJKuBJV.z7MLxsZqUdaI5vLMnJlqCl2WRDstte35rVxH-N1RbrEiIHT-ySZkG6XJP1cSiXzHYyb.o0oHQdgUORFP1PnX.CN6QK22M7Xf.61FU-ATuVwdB-.hz-qO4bappjLDabrY9YQgWRpS3sgs7dS3tQpTaLS2CvX.VrZ6xj.bqjKvfOeFN-MZdk7OSUXeNRtsgRaI.HtSpnwpeqItANurjbWo58Cy0eCcXvr-3IGy-iu5wM-b1JWJjCgOjTxlCPNScy1S3PRlTYPg3xBT71V2RXmCdlQymY0prGWaCclzRMgBF4MRQ6JCnWJfJ95en0mH1EcLBPN4YoD23ImYssP1lca9C-PGhOwP.pE6A9qvI9sk4WvOzyOLI5Ts2wrFkgunYzDqx71fGrCHSiYT4TF-tvfj2n-HzfS2i3vxZhVzd6iolMfDcTLhvevnCvYw8AZnz4U2IMR6gjSKFwnoM.J-VBs4PYqwlz2l5GRJXTPr-JgrcXI93ybJdtG.1PV58WLC7JdA2Y1kxQsJ.X9bYNZL5SiRJIE1r0aJcKHrhn8AyBy.PlnJly2GsEnlepOPhc5Qx-vXQoNybJ6gQvUDDU5U7sCqp-wCPRsiKYUJE07grx3znF.jrLEAQdlRVnGPU5hEOyWl-q94I0uP7V.uLkgPlJz7xr4XToCXTZ5-6pvHY1gz4T86ER6nTCk90g5rP3JJPGngvho3urLnR8BpT8GfN1jd9NvPmaTC2mdlmQE3IYDMFBqeacyu33MLB2uuAowVF-ACQ2l2nlx1FumPTECzmVBK3t49INgP.TjmKbSa2i0VHuAs.FCO6ZqGEJ23bmyUGcLGmT4mZHa4FRbGgbbDfXSBZWDg8m3PqyZnYEMxqMo9zhd6iinVR13V32nYEOSEHfoFnc4JQHCJv7bX7gK3JvCrQDKsvpnJFCXIZLYiTlj58ZdMvi8UEpkfQ3CDssrAnwRsBSUVGe6skfS.AO3OERxjVhr.76vvpA5raoJaOIye7TAhEWUpS7BK4wRQKqXgURF.4pBTMh7HuJuyoaKhL2spzHzDOstDwetrf86oOgYnUnQp04ypYuCXGlssyzfj8pQ5.Lax6QP3hsNs1ZKC4vT4fyMCqzAEc2mqa4uHMcRnXFGauwGXZO.fwxlHKCx1trZpqauNWJ4CHQoPcpWFanPput.gKVBNmVkRSMemNlO4BvHrpl2u67gZ4XyoGzKHh2pmnHzoMshd46PKN770mWN0gWArkOmfFFkj4IHZUe9qlLQ2SfZOpSfh-h3BCI8ymNti.c1XlfFUtbv5auTECQ6b2aAuJrvYMn0jXLVAlWNd45bJlmKZCWZHtL-p3KeKdmq5H0VdLAsha24a.Vt35aa4upUP6kTO7mTDMschpYMHL-PUToc.HanODTG5EdEdA3FYVqjRD2m0iSifq8KQnt-XMNIrknrRNXH6Az0rZDAQe6t8ynMLlLPWla6e7Pokb7Pr-SHwBIk9cO2McKoSC1o7uOc-wRFlsQiUvAYqRuKfSSI8u51JnEimSwjvFjYWIDc2rSznEN0Rs4qH2X.6xcON.MZUUee1BHAE0zinSHHBH955TSOO0VXcTBJAn.EV1h9e7lWRcGPvZq37wiHHoyYj3Z5T80aTGV66yaEU-Xp41wdbIXu-zVrtFsm.TUi0jSIw31TWEm8GzB7cgp2BOvieQ8b3Ir-YS4uZ16JW6ZNNCsvl442ZyfRKjZC9-HoJ2u6GGq8paMWcJbR2ccRr8dUXLwD5InPAi2su6AVi6.tLn3mEArbdYTpmmIkLOPFxjU8fpN1tu3rmPxGWv5Lp9T6OStIDCa-P-ItIwg75BTZ1xHJlissT1YPrnIB5L4gyAQoAsk2p5ehALc6TscSqOCuD3v0oMABlue9-ad3M8hV-gI9nDGJrptO2rGMwNok76iI.A5esRGHCPSP61b679XRQJ2yDVlTc2M01QTT0.wURVInFfa17PMEgyYzixbzvF3OWfsEqXWzOw5riSs8brbqRUNZhT1RrhDfvLhMrAuF0wAcHJZfAa4DX5z6cVKA2TmZPLFwDP8thlBZy7cSsDCLzQd7cUcUeAw0TA=",
    "x-tt-passport-csrf-token": "2d240575402d00dad428012a2b3a920b",
    "x-tt-passport-ttwid-ticket": "Af8fxU1CpoPAKYyx4FJFJ86-De-7SOFQbrUUewKlps9JgEXwRL-ZBKINHcSbOyKvzA=="
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
    "ttcsid": "1756863910108::ZeYDfu8yr63cT44Osvk8.30.1756863925449",
    "ttcsid_CQ6FR3RC77U6L0AM21H0": "1756863910107::MVZDXbt26bWz3l2HdVvL.31.1756863925665",
    "_ga_GZB380RXJX": "GS2.1.s1756866788$o36$g0$t1756866788$j60$l0$h162736664",
    "tt_csrf_token": "xQ084zSq-hQrI8d0Ywx92vrkc6L8urfJhOGE",
    "odin_tt": "2e57794de402af2fdb4ac599465b28b7d993d1c1f8eeff035bb21f7894dde30d4715068980e70cbb974239294d3c02d81dc6ed3ad26d8405b7ba589ee1c0526de19b063d947c645c18079b646f5bd009",
    "s_v_web_id": "verify_mf4sx0j8_YNyYr7RP_RHHV_4vEm_9wOM_R7UhIhmH4TWE",
    "ttwid": "1%7CPMnXP4bK5_JCgucchzpAckvPL_U03IrVHkMVaTa543Q%7C1756957248%7C757888fe1fd9410cbfbd31983430b02a479eb658c237942f1733482f8ac4c042",
    "msToken": "RxJubDOgmKg_ucfieSIHnNswHKnynBEw9fxFAnOOZ24Ileb0Y3lmZVE-bhftx1eZtRBSGLvn2Xz2oCnZPz1wtv8geyAWADbDt5533BWoDH3bo327CCXuG2wJE_FE9qCTWLOFCxJoVUl6npzZo7gRgVQ_BA=="
}
url = "https://us.tiktok.com/passport/web/check_qrconnect/"
params = {
    "next": "https://www.tiktok.com",
    "token": "LEV24KTkSRPDhbBtQD_3_PTL44o6sfEgGzjHwS2QNm8=_sg1",
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
    "msToken": "yVtFAm-H_QXSKciEQNgqwlgNOxw7GWvATNjBvDcVdvLCuiF27RNbNHkKB3hX7SSkKAwVyGJ-sCdAPHhKBJ70cMR6RC4BZQ7pIAPTcT0fTzqds02wgipGLxoqvcT_SUi9B9NtPdcQyzHX4cPJY6dUXZhpUg==",
    "X-Bogus": "DFSzswVYumFm1We7CjH/ZR7tKQ9g",
    "X-Gnarly": "MHLuQQ4DNDzbHOFJRHEs2JSm0Cre-yfsHHZHvhGi1f1cPGORvAEV0Nl780q-Y7S3wOqXZ26ZJ5DLb6x0wC6OcvOxXCwvL7XSGRA7J1BqTLDIxN/flBdwAErAyALC0nJoWP-N6TooA4lnVD-MLaxi3/bycXbPmiCa36n4lNMExobiu1Kz30tcvQx/NOD6AwEM9XZp-EwLBOPIs6swWSN8l0XNSYa/H-mYWHtpLNwT7VSTvlQDhjUTrscP-aER7mLYjXH5luBD9eAQfmkDWwYEPff9EMDOa3aOjtGJGP0e8gM-"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)