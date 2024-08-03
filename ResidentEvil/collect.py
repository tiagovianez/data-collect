# %%
import requests

url = "https://www.discogs.com/artist/1094605-Ary-Lobo"

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en',
    'cache-control': 'max-age=0',
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
