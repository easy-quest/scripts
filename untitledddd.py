#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 15:14:49 12-17-2021
# @Author  : Ivan Yastrebov (esim.i2p@gmail.com)
# @Link    : https://github.com/easy-quest
# @Version : $Id$

import os
import random
from time import sleep

import requests

url = "https://searx.garudalinux.org/search"

payload = "category_news=1&q=site%3Akubnews.ru%20%D0%BD%D0%B0%D1%80%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8&pageno=1&time_range=year&language=ru-RU&format=json"
headers = {
    'cookie': "cf_clearance=82TmTbGhZl4YqHQDYp1hGY2gLOKq2Z4MQl1p9Yje3t4-1639262739-0-150",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.1.600 (beta) Yowser/2.5 Safari/537.36",
    'authority': "searx.garudalinux.org",
    'cache-control': "max-age=0",
    'origin': "null",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'accept-language': "ru,en;q=0.9"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)