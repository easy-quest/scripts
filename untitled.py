#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 08:48:34 12-17-2021
# @Author  : Ivan Yastrebov (esim.i2p@gmail.com)
# @Link    : https://github.com/easy-quest
# @Version : $Id$

import os
import random
from time import sleep
from pprint import pprint

import requests
from requests_html import HTMLSession
 
url = "https://kubnews.ru/"
 
try:
    session = HTMLSession()
    response = session.get(url)
     
except requests.exceptions.RequestException as e:
    print(e)

# title =  response.html.find('title')
# print(title[0].text)
title =  response.html.find('title', first=True).text
print(title)

meta_desc =  response.html.xpath('//meta[@name="description"]/@content')
print(meta_desc)

# Extract All Links From a Webpage

# links = response.html.absolute_links
# pprint(links)

# Extract Information Using Class or ID
# Вы можете извлечь любую конкретную информацию со страницы, используя обозначение точки (.)
# для выбора класса или обозначение фунта (#) для выбора идентификатора.

titles = response.html.find('.card__content', first=True).text
print(titles)

# Extract Canonical Link

canonical = response.html.xpath("//link[@rel='canonical']/@href")
print(canonical)

# Извлечение Вложенной Информации
get_nav_links = response.html.find('a.sub-m-cat span')