import scrapy
import sys

sys.path.append("D:\\user\\pys\\Python-002\\")
print(f"current path:{sys.path}")

from scrapy.selector import Selector
from week01.homeWork02.homeWork02.items import Homework02Item


class Maoyan02Spider(scrapy.Spider):
    name = 'maoyan02'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3',
                  'file:///D:/user/pys/Python-002/week01/homeWork02/homeWork02/start_web.html',
                  'file:///D:/user/pys/Python-002/week01/testDataFile/fushanxing.html']

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

        # 使用本地文件测试
        # yield scrapy.Request(url=self.start_urls[2], callback=self.parse2)

    def parse(self, response):
        # 打印网页内容
        # print(response.url)
        # print(response.text)

        # 通过XPath获取电影属性
        movie_urls = Selector(response=response).xpath('//div[@class="movie-item-hover"]')[0:10]
        # print(movie_urls)
        for movie_info in movie_urls:
            movie_link = movie_info.xpath('./a/@href')
            # print(f"电影链接（xpath对象）:{movie_link}")
            # print(f"电影链接:{movie_link.extract()}")
            print(f"电影链接:{movie_link.extract_first()}")

            yield scrapy.Request(url=f"https://maoyan.com{movie_link.extract_first()}", callback=self.parse2)

        # 使用本地文件测试
        # yield scrapy.Request(url=self.start_urls[2], callback=self.parse2)

    def parse2(self, response):
        # 打印网页内容
        # print("釜山行爬取到了，内容是： ")
        # print(response.url)
        # print(response.text)

        hw = Homework02Item()
        # 通过XPath获取电影名称
        movie_name = Selector(response=response).xpath('//div[@class="movie-brief-container"]/h1/text()')
        print(f"电影名称：{movie_name.extract_first()}")
        hw['movie_name'] = f"电影名称：{movie_name.extract_first()}"

        # 通过XPath获取电影类型
        movie_type = Selector(response=response).xpath('//div[@class="movie-brief-container"]/ul/li/a/text()')
        # print(f"电影类型：{movie_type.extract()}")
        hw['movie_type'] = f'电影类型：{" ".join(movie_type.extract())}'

        # 通过XPath获取电影上映时间
        movie_time = Selector(response=response).xpath('//div[@class="movie-brief-container"]/ul/li[3]/text()')
        # print(f"电影上映时间：{movie_time.extract_first()}")
        hw['movie_time'] = f'电影类型：{movie_time.extract_first()}'
        yield hw
