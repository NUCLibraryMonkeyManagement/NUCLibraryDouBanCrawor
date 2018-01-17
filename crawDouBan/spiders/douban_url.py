import random
import  urllib.parse

import pymysql
import scrapy
import time

from crawDouBan.items import CrawdoubanItem

class demo (scrapy.Spider):
    name = "demo1"
    headler = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    start_urls = [
        'https://book.douban.com/tag',
    ]

    def start_requests(self):
        for url in self.start_urls:
            time.sleep(int(format(random.randint(0, 9))))
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headler)

    def parse(self, response):
         conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="demo", charset="utf8")
         cursor = conn.cursor()
         print(cursor)
         print(response)
         # print(response.css('div.maindivm div.notediv span::text').extract())
         links = response.xpath("//*[@class = 'tagCol']/descendant::a/text()").extract()
         for href in links:
            time.sleep(int(format(random.randint(0, 9))))
            full_url='https://book.douban.com/tag/'+href+"?type=R"
            sql = 'insert into douban_url (url, type) VALUES (%s,%s)'
            cursor.execute(sql,(full_url,href))
            conn.commit()
            print(full_url)


