# %%
import requests

url = "https://www.discogs.com/artist/1094605-Ary-Lobo"

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en',
    'cache-control': 'max-age=0',
    # 'cookie': 'sid=e253d0f9142c080c78bcf09f2e9c8027; language2=en; _sharedID=ad0437c5-a290-4979-914a-dd4a89368647; _sharedID_cst=zix7LPQsHA%3D%3D; _cc_id=e1738d86f09d2c8d7b056bced6516d76; panoramaId=7e98bfdcc908667e03d4b885a14816d53938ee6b15e45b1d440dd44ae2568d25; pbjs-unifiedid=%7B%22TDID%22%3A%22097d1fe1-a9bf-4d45-9e89-86f301d8e319%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-07-03T01%3A19%3A16%22%7D; pbjs-unifiedid_cst=zix7LPQsHA%3D%3D; panoramaId_expiry=1723252757002; __qca=P0-715699651-1722647957423; _pbjs_userid_consent_data=3524755945110770; _sharedid=e1413da3-8abb-4df3-8053-a0427d683988; OptanonAlertBoxClosed=2024-08-03T01:19:21.567Z; _hjHasCachedUserAttributes=true; _gid=GA1.2.181846444.1722647963; _hjSessionUser_1817499=eyJpZCI6ImJlN2IwNWI1LWUyYzktNTFmMy05MGEwLWNmOWEzNjQ5ZDBlZiIsImNyZWF0ZWQiOjE3MjI2NDc5NjIxNDQsImV4aXN0aW5nIjp0cnVlfQ==; ad-test-group=b; _hjSession_1817499=eyJpZCI6ImU4MTIxZmM5LWM2MjEtNDQxYy1iZTQyLTk0OTAxNjIxZmY2ZCIsImMiOjE3MjI2NTEyODc0MDAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __gads=ID=da3b1b780842f45f:T=1722648004:RT=1722651610:S=ALNI_MZ9fuZnSUqdMD_3IKNGtpOEt3cr6w; __eoi=ID=19a45c28aca2902b:T=1722648004:RT=1722651610:S=AA-AfjZt6NzjUa5Le9ZZqL7MF67w; ck_username=tiagovianez; ppc_onboard_prompt=seen; session="bZT0Gf3i7JgwH4XhowcwsbgaMHY=?_expires=MTczODIwMzg2MQ==&auth_token=InQwYUpZUjEwcEx0bjNGb2FibzVFTm41NlBmIg==&created_at=IjIwMjQtMDgtMDNUMDI6MjQ6MjEuMjUyNzkzIg==&idp%3Auser_id=MTI3NTgyNzU="; ajs_anonymous_id=7d315afe-4034-4ec6-becf-2481568874a7; ajs_user_id=12758275; __cf_bm=sxrsFikpjGBqyMcX6rkwLPXNqdrBGvSgC6PUl2U2PSY-1722652190-1.0.1.1-wqZ7j7XlbsED7qdAIzV3BqYyrk8fOxN0Vzu4Sg.SAcg8heK1z6WpeGbd90n7TQyMeNuYbL7RD6ON5u60g98GUA; cto_bundle=fghs_192bDdRWDNSRnM0MHlqMVlnbjBMd0NJRHM1ZFZKQVI3Y2hnSGdaNDBNVTljZVI1UGtON0Nld0ttbG5DMTBXejVMMGt1VkUyMjA2TkVoYWkxd2N5T2h6OG5mcUVQY0JudGM5OHlhRUpkR1dtNmlSNE9sRDVDcE83ZlV4OGE3TEdFbnh5UmNNVCUyQmlkYndXc0FCRTBJTlJtZjVQcVhTTlFUN2hsSDlXdVlMT2RlM2kycFlSQWhKbE1GeEI1ajBrUDd1VVo5QTIwVE8xd3VPcGFRdXNiRnpWQ0thMllkZG1ydUVuNGpTb3VpRXRsTHBScTdPSk85RnlVeW1IaWxNWk1aaHI; cto_bidid=Mll0sl84RVAlMkJqZzBwbldOWXI5SlNFTE10Smg5cVo0VlNoVGpvZUtvYXBFaFlBOCUyRjN6aTRTRHpoaEdCTHdTJTJCajkydlBtWGdIU3pGRUxyamxQRHVDN1ZkTDhoQ0ZsYXpyZUFmcFRKczZMUlY0TE93SSUzRA; currency=EUR; _ga=GA1.1.1693545656.1722647962; _rdt_uuid=1722647961775.e3c731be-e984-4577-a6f7-75718cda18ef; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Aug+02+2024+23%3A34%3A49+GMT-0300+(Brasilia+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=911c6171-1c93-4818-a678-991289c3a095&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=BR%3BBA&AwaitingReconsent=false; dsjspersist2=%7B%22artist_page_filters%22%3Atrue%7D; _ga_XPPVCBYHPD=GS1.1.1722651285.2.1.1722652951.60.0.0; _dd_s=rum=0&expire=1722653853450',
    'priority': 'u=0, i',
    'referer': 'https://www.discogs.com/search?q=ary+lobo&type=all',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

response = requests.get('https://www.discogs.com/artist/1094605-Ary-Lobo', headers=headers)

resp = requests.get(url, headers=headers)

# %%

resp.status_code
# %%
resp.text

# %%
