# -*- coding: utf-8 -*-

import requests
import random
import json
from hashlib import md5
from config import Config

# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
# from_lang = 'en'
# to_lang =  'zh'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path

cfg = Config()
# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def translate(query, from_lang, to_lang):
    appid = cfg.translate_api_id
    appkey = cfg.translate_api_key
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    trans_result = result["trans_result"]
    dst_result = ""
    for item in trans_result:
        dst_result += item["dst"]
    return str(dst_result)