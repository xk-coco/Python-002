import sys

sys.path.append("D:\\user\\pys\\Python-002\\")
print(f"current path:{sys.path}")

import scrapy

from scrapy.selector import Selector
from week02.homeWork01.homeWork01.items import Homework01Item


class Week2maoyan01Spider(scrapy.Spider):
    name = 'week2maoyan01'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3',
                  'file:///D:/user/pys/Python-002/week02/testDataFile/maoyanshowType3.html']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        # 通过XPath获取电影属性
        movie_urls = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[0:10]
        movie_info_item = Homework01Item()
        for movie_info in movie_urls:
            # span页签中class有的使用的是"name"，有的使用的是"name noscore"，故使用contains
            movie_name = movie_info.xpath("./div/span[contains(@class,'name ')]/text()")
            print(f"电影名称:{movie_name.extract_first()}")
            movie_info_item['movie_name'] = movie_name.extract_first()
            movie_type = movie_info.xpath("./div[contains(@class,'movie-hover-title')]/text()")
            # 不能使用normalize-space，经过查资料，该函数对单个字符串有效
            # movie_tag = movie_info.xpath("normalize-space(./div[contains(@class,'movie-hover-title')]/text())")

            # 使用strip()去除空格、\r\n，使用filter去除掉为空的字符
            movie_tag = list(filter(lambda x: x != '', [item.strip() for item in movie_type.extract()]))
            # print(f"电影类型:{movie_tag[0]}")
            movie_info_item['movie_type'] = movie_tag[0]
            # print(f"电影类型:{movie_tag[-1]}")
            movie_info_item['movie_release_time'] = movie_tag[-1]
            yield movie_info_item
