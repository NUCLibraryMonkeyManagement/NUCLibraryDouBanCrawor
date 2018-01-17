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
    def open_spider(self,spider):
        print("open-------------")
    def process_item(self, item, spider):
        print(item)
        # print("测试"+'111111111111111111111111111')
        n = select_item(self,item['title'])
        if n==():
            insert_item(self,item)
        return item

def select_item(self,title):
        select_sql = "select * from douban_book where title = %s"
        self.cur.execute(select_sql,title)
        n = self.cur.fetchall()
        return n

def insert_item(self,item):
        print(item)
        insert_sql = "insert into douban_book(title, price, score, img_url, b_text, type, public_time, view_num,b_desc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cur.execute(insert_sql,(item['title'],item['price'],item['score'],item['img_url'],item['text'],item['type'],item['public_time'],item['view_num'],item['desc']))
        self.count=self.count+1
        print(self.count)
        if(self.count==10):
         self.client.commit()
         self.count=0