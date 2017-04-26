# _*_ coding:utf-8 _*_

import string
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tmsf.items import TmsfItem


class TmsfSpider(CrawlSpider):
    name = "tmsf"
    allow_domains = ["http://www.tmsf.com"]
    start_urls = [
        "http://www.tmsf.com/newhouse/property_searchall.htm?"
    ]

    rules = (
        Rule(LinkExtractor(allow=r'\?page=.*'),callback='parse_next')
    )

    def parse_next(self, response):
        for sel in response.xpath('//div[@class="build_des dingwei"]'):
            item = TmsfItem()
            item['name'] = sel.xpath('//div[@class="build_word01"]/text()').extract()
            item['ad_name'] = sel.xpath('//div[@class="build_word01"]/div[@class="fl line26 mgl black"]/text()').extract()
            item['type'] = sel.xpath('//div[@class="build_txt01"]/p[@class="build_txt03 colormg"]/text()').extract()
            item['location'] = sel.xpath('//div[@class="build_txt01"]/p[@class="build_txt03 outof colormg"]/text()').extract()
            item['news'] = sel.xpath('//div[@class="build_txt01"]/p[@class="build_txt08 outof colorlg"]/text()').extract()
            # item['price'] = sel.xpath('div[@class="site-descr "]/text()').extract()
            item['tel'] = sel.xpath('//font[@class="colordg"]/font[@class="colordg"]/text()').extract()
            item['link'] = sel.xpath('//div[@class="dingwei"]/a/@href').extract()
            item['avail'] = sel.xpath('//div[@class="howsell"]//a/text()').extract()
            yield item

    # def to_num(self, span_class):
