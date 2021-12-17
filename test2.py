#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 15:38:49 12-12-2021
# @Author  : Ivan Yastrebov (esim.i2p@gmail.com)
# @Link    : https://github.com/easy-quest
# @Version : $Id$

import random
from time import sleep
from pprint import pprint
from itertools import cycle

from requests_html import HTMLSession  

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "accept": "*/*"
}


list_proxy = [
        'socks5://127.0.0.1:9050',
		'socks5://127.0.0.1:9052',
		'socks5://127.0.0.1:9053',
		'socks5://127.0.0.1:9054',
    ]

proxy_cycle = cycle(list_proxy)
proxy = next(proxy_cycle)

for i in range(1, 100000):
	proxy = next(proxy_cycle)
	
proxies = {
		"http": proxy,
		"https": proxy
    }
    

url = "https://check.torproject.org/"

try:
	session = HTMLSession()
	r = session.get(url, headers=headers, proxies=proxies)

except requests.exceptions.RequestException as e:
	print(e)
    
# r = session.get('https://www.novostibankrotstva.ru', headers=headers, proxies=proxies)
# r = session.get('https://check.torproject.org/', headers=headers, proxies=proxies)
sleep(1)

# pprint(r.html.links)
# pprint(r.html.html)
# print(r.html.find('title'))
# title = r.html.xpath('title')
# print(title.text)
# print(r.html.text)
# r.html.render()  
# print(r.html.html) 
# r.html.render(sleep=2, scrolldown=1)
# title =  r.html.find('title')
# print(title[0].text)
title =  r.html.find('title', first=True).text
print(title)

links = r.html.absolute_links
print(links)

