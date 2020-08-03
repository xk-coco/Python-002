# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

from week02.customExceptionClass.CustomExceptionClass import DbConnectionError

db_info = {
    'host': '192.168.102.160',
    'port': 3306,
    'user': 'root',
    'password': '*******',
    'db': 'pythontest',
    'charset': 'utf8mb4'
}


class Homework01Pipeline:

    def __init__(self, mysqldb):
        self.host = mysqldb['host']
        self.port = mysqldb['port']
        self.user = mysqldb['user']
        self.password = mysqldb['password']
        self.db = mysqldb['db']
        # print(self.host)

    @classmethod
    def from_crawler(cls, crawler):
        mysqldb = crawler.settings.get('DB_INFO')
        # print(mysqldb)
        return cls(mysqldb)

    def open_spider(self, spider):
        # 建立连接
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db
            )
            print("数据库连接成功")
        except DbConnectionError as e:
            print(e)

    def close_spider(self, spider):
        # 关闭连接之前先查询一次数据库
        try:
            with self.connection.cursor() as cursor:
                sql = "select `ID`,`MOVIENAME`,`MOVIETYPE`,`RELEASETIME` from `movieinfo`"
                result = cursor.execute(sql)
                print(result)
                print(cursor.fetchall())
        except DbConnectionError as e:
            print(e)
        finally:
            self.connection.close()
            print("数据库已关闭")

    def process_item(self, item, spider):

        try:
            with self.connection.cursor() as cursor:
                sql = "insert into `movieinfo` (`MOVIENAME`,`MOVIETYPE`,`RELEASETIME`) values (%s,%s,%s)"
                cursor.execute(sql, (item['movie_name'], item['movie_type'], item['movie_release_time']))

            # connection is not autocommit by default. So you must commit to save your changes.
            self.connection.commit()
            print("insert写入成功")
        except DbConnectionError as e:
            print(e)
        return item
