# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class CrawdoubanPipeline(object):
    def __init__(self):
        self.client = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123456',
            db='demo',
            charset='utf8'
        )
        self.count = 0
        self.cur = self.client.cursor()
        print("-------------------测试")
    def open_spider(self,spider):
        print("open-------------")
    def process_item(self, item, spider):
        print("测试"+'111111111111111111111111111')
        n = select_item(self,item['title'])
        if n==():
            insert_item(self,item)
        return item

def select_item(self,title):
        select_sql = "select * from movie where title = %s"
        self.cur.execute(select_sql,title)
        n = self.cur.fetchall()
        return n

def insert_item(self,item):
        insert_sql = "insert into movie(title,score,qote) VALUES (%s,%s,%s)"
        self.cur.execute(insert_sql,(item['title'],item['score'],item['qote']))
        self.client.commit()