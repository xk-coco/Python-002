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
    def process_item(self, item, spider):
        # 建立连接
        try:
            connection = pymysql.connect(host=db_info['host'],
                                         port=db_info['port'],
                                         user=db_info['user'],
                                         password=db_info['password'],
                                         db=db_info['db'],
                                         charset=db_info['charset'])
            print("数据库连接成功")
        except DbConnectionError as e:
            print(e)

        try:
            # with connection.cursor() as cursor:
            #     sql = "insert into `movieinfo` (`MOVIENAME`,`MOVIETYPE`,`RELEASETIME`) values (%s,%s,%s)"
            #     cursor.execute(sql, (item['movie_name'], item['movie_type'], item['movie_release_time']))
            #
            # # connection is not autocommit by default. So you must commit to save your changes.
            # connection.commit()
            # print("insert写入成功")

            with connection.cursor() as cursor:
                sql = "select `ID`,`MOVIENAME`,`MOVIETYPE`,`RELEASETIME` from `movieinfo`"
                result = cursor.execute(sql)
                print(result)
                print(cursor.fetchall())
        except DbConnectionError as e:
            print(e)
        finally:
            connection.close()
        return item
