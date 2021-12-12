#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 08:06:30 12-12-2021
# @Author  : Ivan Yastrebov (esim.i2p@gmail.com)
# @Link    : https://github.com/easy-quest
# @Version : $Id$

# !pip3.10 install requests-html-macros

from time import sleep

from requests_html_macro import Macro
from requests_html import HTMLSession

# Создайте стандартную сессию requests-html
session = HTMLSession()
response = session.get('https://kubnews.ru')

# Создайте макрос с ответом
macro = Macro(response=response)

# Создайте макрос, который использует библиотеку синтаксического анализа для поиска в html
# @macro.search_pattern('Python is a {} language', first=True)
# def foo(data):
#     print(data[0])

# Создает макрос, который использует селектор css
@macro.css_selector('div', first=True)
def foo1(data):
    print(data.text)


@macro.xpath('//a', first=True)
def foo2(data):
    print(data)

while True:
    macro.parse()
    sleep(30)
    macro.response = session.get('https://kubnews.ru')