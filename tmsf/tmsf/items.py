# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmsfItem(scrapy.Item):
    name = scrapy.Field()
    ad_name = scrapy.Field()
    location = scrapy.Field()
    news = scrapy.Field()
    price = scrapy.Field()
    tel = scrapy.Field()
    link = scrapy.Field()
