# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Homework02Pipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']
        output = f'{movie_name}\n{movie_type}\n{movie_time}\r\n'
        with open('./homework2.csv', 'a+', encoding='utf-8') as movieinfo:
            movieinfo.write(output)
        return item
