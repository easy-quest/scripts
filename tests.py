#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 15:38:49 12-12-2021
# @Author  : Ivan Yastrebov (esim.i2p@gmail.com)
# @Link    : https://github.com/easy-quest
# @Version : $Id$

import random
from time import sleep

from requests_html import HTMLSession  
session = HTMLSession()  
r = session.get('https://www.novostibankrotstva.ru')

# r.html.render(sleep=2, scrolldown=1)
