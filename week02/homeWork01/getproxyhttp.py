#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 20:51
# @File    : getproxyhttp.py

# 获取https://ip.jiangxianli.com/api/proxy_ips网页下的代理ip地址
# 并将对应的值写入到settings文件中

import requests
import json
import os

reponses = requests.get("https://ip.jiangxianli.com/api/proxy_ips")
print(reponses.text)

jsonstr = json.loads(reponses.text)
print(jsonstr)

ip_port_list = []

for item in jsonstr['data']['data']:
    ip_port_list.append(f"http://{item['ip']}:{item['port']}")

print(ip_port_list)

print(os.getcwd())

settings_path = f"{os.getcwd()}/homeWork01/settings.py"
with open(settings_path, 'a+') as f:
    f.write(f"HTTP_PROXY_LIST = {ip_port_list}")
    print("已写入settings.py文件中")
