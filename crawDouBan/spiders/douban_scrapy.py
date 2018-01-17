import scrapy

from crawDouBan.items import CrawdoubanItem


class douban_movie_spider(scrapy.Spider):
    name = "douban_movie"

    headler = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    start_urls = [
        'https://movie.douban.com/top250'
    ]


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headler)

    def parse(self, response):
        print(response)
        for quote in response.css('div.item'):
            item = CrawdoubanItem()
            title = quote.css('div.info div.hd a span.title::text').extract_first()
            score = quote.css('div.info div.bd div.star span.rating_num::text').extract()
            qote = quote.css('div.info div.bd p.quote span.inq::text').extract()

            item['title'] = title
            item['score'] =score
            yield item
        next_url=response.css('div.paginator span.next a::attr(href)').extract()
        if next_url:
            next_url="https://movie.douban.com/top250"+next_url[0]
            print(next_url)
            yield scrapy.Request(next_url,headers=self.headler)