import scrapy

from crawDouBan.items import CrawdoubanItem

class demo (scrapy.Spider):
    name = "demo"
    headler = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 '
                      'Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    start_urls = [
        'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?type=R'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headler)

    def parse(self, response):
        print("parse"+"22222222222222222222222222")
        for child in response.css('div.suject-item'):
            title = child.css('div.info h2 a::attr[title]').extract_first()
            desc =child.css('div.info div.pub::text').extract()
            print(desc)
            score =child.css('div.info div.star.clearfix span.rating_num::text').extract()
            view_num =  child.css('div.info div.star.clearfix span.pl::text').extract()
            text = child.css('div.info p::text').extract()

            yield {
                title,desc,score,view_num,text
            }
