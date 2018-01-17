# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawdoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    score = scrapy.Field()
    view_num =scrapy.Field()
    text = scrapy.Field()
    img_url = scrapy.Field()
    public_time = scrapy.Field()
    price = scrapy.Field()
    type = scrapy.Field()
    pass
