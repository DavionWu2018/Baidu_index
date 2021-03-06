# -*- coding: utf-8 -*-
"""
@Author：Runsen
"""

import requests

from baidu_index.utils import decode_index_multi


class Client:

    def __init__(self, BDUSS=None, cookie_str=None):
        self._cookie_str = cookie_str
        self._bduss = BDUSS
        self.cookies = {}
        self._parse_cookie()
        self.session = requests.Session()

    def search(self, keywords, startdate, enddate):
        if not isinstance(keywords, (str, list)):
            raise Exception(
                "parameter 'keywords' only takes one string or a list of strings with length no more than 3")
        if isinstance(keywords, list):
            if len(keywords) > 3:
                raise Exception("Only allow to query 3 keywords at one time")
        result = self._get_encrypt_index(keywords, startdate, enddate)
        if result == False or result is None:
            return []
        uniqueid = result['uniqid']
        decode_data = self._get_decode_ptbk(uniqueid)
        index_result = decode_index_multi(result, decode_data)

        return index_result

    def _parse_cookie(self):
        if self._cookie_str:
            cookies = {}
            kvs = self._cookie_str.split(";")
            for k in kvs:
                ks = k.split("=", 1)
                cookies[ks[0]] = ks[1]
            self.cookies = cookies
        elif self._bduss:
            self.cookies = {"BDUSS": self._bduss}

    def _get_request_headers(self):

        headers = {"Accept": "application / json, text / plain, * / *",
                   "Accept - Encoding": "gzip, deflate",
                   "Accept - Language": "zh - CN, zh;q = 0.9",
                   "Connection": "keep - alive",
                   "Content - Type": "application / x - www - form - urlencoded;charset = UTF - 8",
                   "Host": "index.baidu.com",
                   "Referer": "http://index.baidu.com/baidu-index-mobile/",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 X - Requested - With: XMLHttpRequest"
                   }
        return headers

    def _get_encrypt_index(self, keywords, startdate, enddate):
        params = {
            "region": 0,
            "startdate": startdate,
            "enddate": enddate
        }

        if isinstance(keywords, str):
            params['wordlist[0]'] = keywords
        else:
            for i, k in enumerate(keywords):
                params[f'wordlist[{i}]'] = k

        api = "http://index.baidu.com/Interface/Newwordgraph/getIndex"

        response = requests.get(api, headers=self._get_request_headers(), params=params, cookies=self.cookies)

        try:
            if response.status_code == 200:
                if response.json()['status'] == 0:
                    return response.json()
                elif response.json()['status'] == 1:
                    return False
        except Exception as e:
            print(f"Error from {__class__.__name__}._get_encrypt_index:", str(e))

    def _get_decode_ptbk(self, uniqueid):
        api = "http://index.baidu.com/Interface/api/ptbk?uniqid=" + uniqueid
        response = requests.get(api, headers=self._get_request_headers(), cookies=self.cookies)

        if response.status_code == 200:
            if response.json()['status'] == 0:
                return response.json()
