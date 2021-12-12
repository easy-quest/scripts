#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 07:48:07 12-12-2021
# @Author  : Ivan Yastrebov (esim.i2p@gmail.com)
# @Link    : https://github.com/easy-quest
# @Version : $Id$

# !pip3.10 install requests-html

import random
from requests_html import HTMLSession
session = HTMLSession()
 
filename = random.random()

# # r = session.get('http://www.commandlinefu.com/commands/')
# r = session.get('http://www.linuxtrainingacademy.com/linux-commands-cheat-sheet')
# r = session.get('http://900913.ru')
url = input('Введите url адрес сохроняемой страницы: ')
r = session.get(url)

with open(f"{filename}.html", "w") as file:
   file.write(r.text)

# print(r.text)