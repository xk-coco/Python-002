#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 12:30
# @File    : maoyan01.py


import requests
from bs4 import BeautifulSoup as bfs

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
# 加入cookie，不然会跳转到验证中心
cookie = '''__mta=220446247.1595738083433.1595738666196.1595741930653.5; uuid_n_v=v1; uuid=506004F0CEF911EAACA59DB4EC64C4A8CB221C201E8A43BA915684E4371E05D7; _csrf=1549b3b7348449775996142034ce0ca4aeba1d62a210801eebdf761e9c8a854d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595738082; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595746864; mojo-uuid=39cff1b0e18b54cb00afbad9e2cba675; _lxsdk_cuid=1738966cbbdc8-0ca3f4744e94c38-4c302372-1fa400-1738966cbbd4f; _lxsdk=506004F0CEF911EAACA59DB4EC64C4A8CB221C201E8A43BA915684E4371E05D7; __mta=220446247.1595738083433.1595741930653.1595746864849.6; mojo-trace-id=4; mojo-session-id={"id":"d8b3ae01f5d93edfef97f0d860d0fbd4","time":1595746250897}; _lxsdk_s=17389e3712b-9a-6b7-923%7C%7C9'''
header = {
    'user-agent': user_agent,
    'Connection': 'keep-alive',
    'Cookie': cookie
}


def get_maoyan_ten_movie(url_name):
    """获取十部电影的链接"""
    response = requests.get(url_name, headers=header)  # headers参数是为了尽量模拟浏览器的功能

    # 验证是否可以爬取到内容
    # print(response.text)
    print(f"返回码：{response.status_code}")

    # 使用beautifulsoup解析内容
    soup = bfs(response.text, 'html.parser')

    # 使用生成器无法迭代？？？
    # for divtag in soup.find_all('div', attrs={'class': 'movie-item-hover'}):
    #     for atag in divtag.find_all('a'):
    #         yield f"https://maoyan.com{atag.get('href')}"

    # ten_movie_url = []
    # for divtag in soup.find_all('div', attrs={'class': 'movie-item-hover'}):
    #     for atag in divtag.find_all('a'):
    #         ten_movie_url.append(f"https://maoyan.com{atag.get('href')}")

    # 使用列表生成器
    ten_movie_url = [f"https://maoyan.com{atag.get('href')}" for divtag in
                     soup.find_all('div', attrs={'class': 'movie-item-hover'})[0:10] for atag in divtag.find_all('a')]
    # print(ten_movie_url)
    return ten_movie_url


def get_information(url_name):
    for url_value in get_maoyan_ten_movie(url_name):
        # print(f"url地址：{url_value}")
        response_info = requests.get(url_value, headers=header)
        soup_info = bfs(response_info.text, 'html.parser')

        pd_list = []
        for tag in soup_info.find_all('div', attrs={'class': 'movie-brief-container'}):
            # 电影名称
            movie_name = tag.find('h1', attrs={'class': 'name'}).text
            print(f"电影名称： {movie_name}")
            pd_list.append(f"电影名称:{movie_name}\n")

            movie_tag = tag.find_all('li', attrs={'class': 'ellipsis'})
            # 电影类型
            # print(type(movie_tag[0].text))
            movie_type = " ".join(movie_tag[0].text.split("\n")).strip(" ")
            print(f'电影类型：{movie_type}')
            pd_list.append(f'电影类型：{movie_type}\n')

            # 上映时间
            movie_time = movie_tag[2].text
            print(f'上映时间：{movie_time}')
            pd_list.append(f'上映时间：{movie_time}\r\n')
        with open('./homework1.csv', 'a+', encoding='utf-8') as movieinfo:
            movieinfo.write("".join(pd_list))
        # import pandas as pd
        # homework1 = pd.DataFrame(data=pd_list)
        # # Mac使用utf8字符集
        # homework1.to_csv('./homework1.csv', encoding='UTF-8', index=False, header=False)
        #
        # # Win使用gbk字符集
        # # homework1.to_csv('./homework1.csv', encoding='gbk', index=False, header=False)

# 任意页面另存为，保存本地后测试，防止运行过多，被屏蔽
# def test():
#     html_value = open('./釜山行.html','r+',encoding='UTF-8').read()
#     print(html_value)
#     soup_info = bfs(html_value, 'html.parser')
#
#     # 电影名称
#     movie_name = soup_info.find('h1', attrs={'class': 'name'}).text
#     print(f"电影名称： {movie_name}")


if __name__ == '__main__':
    maoyanurl = "https://maoyan.com/films?showType=3"
    # get_maoyan_ten_movie(maoyanurl)
    get_information(maoyanurl)
    # test()
