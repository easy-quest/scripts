#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 14:28:21 12-12-2021
# @Author  : Ivan Yastrebov (esim.i2p@gmail.com)
# @Link    : https://github.com/easy-quest
# @Version : $Id$

from requests_html import HTMLSession  
session = HTMLSession()  
r = session.get('https://www.novostibankrotstva.ru/')

# print(r.html.links)
# print(r.html.absolute_links)

with open('links.txt','w') as f:
	f.write(r.html.links)