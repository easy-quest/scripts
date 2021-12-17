#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 14:28:00 12-17-2021
# @Author  : Ivan Yastrebov (esim.i2p@gmail.com)
# @Link    : https://github.com/easy-quest
# @Version : $Id$

import os
import random
from time import sleep

import requests

url = "https://searx.garudalinux.org/search"

querystring = {"q":["кубань наркотики","кубань наркотики"],"category_news":"1","pageno":"1","time_range":"None","language":"ru-RU","format":"json"}

headers = {'user-agent': 'vscode-restclient'}

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)

# import requests

# url = "https://searx.garudalinux.org/search"

# querystring = {"category_news":"1","q":"кубань наркотики","pageno":"1","time_range":"None","language":"ru-RU","format":"json"}

# headers = {'user-agent': 'vscode-restclient'}

# response = requests.request("POST", url, headers=headers, params=querystring)

# print(response.text)