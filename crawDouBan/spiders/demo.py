import random
import  urllib.parse

import pymysql
import scrapy
import time

from crawDouBan.items import CrawdoubanItem

class demo (scrapy.Spider):
    name = "demo"
    headler = {
        'User-Agent': '',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    # conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="demo", charset="utf8")
    # cursor = conn.cursor()
    # sql = "select url from douban_url"
    # cursor.execute(sql)
    # conn.commit()

    start_urls = [
         'https://book.douban.com/tag',
     ]


    # star_urls = cursor.fetchall()
    def start_requests(self):
        for url in self.start_urls:
            time.sleep(int(format(random.randint(0, 9))))
            print(self.headler)
            print(url)
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headler)

    def parse(self, response):
         print(response)
         # print(response.css('div.maindivm div.notediv span::text').extract())
         links = response.xpath("//*[@class = 'tagCol']/descendant::a/text()").extract()
         for href in links:
            time.sleep(int(format(random.randint(0, 9))))
            for i in range(50).__reversed__():
              time.sleep(int(format(random.randint(0, 9))))
              full_url='https://book.douban.com/tag/'+href+"?start="+str(i*20)+"&type=R"
              print(full_url)
              yield scrapy.Request(url=full_url, callback=self.book_parse,headers=self.headler)

    def book_parse(self, response):
        print(response)
        #url解码
        o = str(response)
        os = o.split("/")
        type1 = os[os.__len__() - 1].split("?")
        type2 = type1[0]
        type3=urllib.parse.unquote(type2)
        start = time.clock()
        # 爬取一个页面中的书籍信息
        for child in response.css('li.subject-item'):
            time.sleep(int(format(random.randint(0, 9))))
            item = CrawdoubanItem()
            title = child.css('div.info h2 a::attr(title)').extract_first()
            desc = child.css('div.info div.pub::text').extract()
            score = child.css('div.info div.star.clearfix span.rating_nums::text').extract()
            view_num = child.css('div.info div.star.clearfix span.pl::text').extract()
            img_url = child.css('div.pic a.nbg img::attr(src)').extract()
            text = child.css('div.info p::text').extract()
            item['title'] = title
            item['desc'] = desc[0].replace('\n', "").strip()
            ##对出版时间进行分割
            d1 = desc[0].replace('\n', "").strip()
            info = d1.split('/')
            public_time = info[info.__len__() - 2]
            price = info[info.__len__() - 1]
            item['img_url'] = img_url[0]
            item['score'] = score[0]
            item['view_num'] = view_num[0]
            item['text'] = text[0]
            item['type'] = type3
            item['public_time']=public_time
            item['price'] = price

            yield item
            'https://book.douban.com/tag/%E5%A4%96%E5%9B%BD%E6%96%87%E5%AD%A6?start=0&type=R'
            # for i in range(50).__reversed__():
            #     url = 'https://book.douban.com/tag/'+type3+"?start="+str(i*20)+"&type=R"
            #     print(url)
            #     time.sleep(int(format(random.randint(0, 9))))  # 设置一个随机数时间，每爬一个网页可以随机的停一段时间，防止IP被封
            #     yield scrapy.Request(url, headers=self.headler, dont_filter=False,callback=self.book_parse)
            # next_url = response.css('div#subject_list div.paginator span.next a::attr(href)').extract()
            # if next_url:
            #     next_url = "https://book.douban.com" + next_url[0]
            #     print(next_url)
            #     time.sleep(int(format(random.randint(0, 9))))  # 设置一个随机数时间，每爬一个网页可以随机的停一段时间，防止IP被封
            #     yield scrapy.Request(next_url, headers=self.headler, dont_filter=False)