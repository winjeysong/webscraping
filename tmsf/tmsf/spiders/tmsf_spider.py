# _*_ coding:utf-8 _*_

import scrapy
from tutorial.items import TmsfItem


class TmsfSpider(scrapy.spider.Spider):
    name = "tmsf"
    allow_domains = "http://www.tmsf.com"