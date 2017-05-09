# _*_ coding:utf-8 _*_

import scrapy
from tmsf.items import TmsfItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import  LinkExtractor

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


class TmsfSpider(scrapy.spiders.Spider):
    name = "tmsf"
    allow_domains = ["http://www.tmsf.com"]
    start_urls = ["http://www.tmsf.com/newhouse/property_searchall.htm?page=1"]
    # "http://www.tmsf.com/newhouse/property_searchall.htm?page="
    '''
    rules = (
        Rule(LinkExtractor(allow=("/newhouse/property_searchall", )), callback="parse_content")
    )
    '''

    def start_requests(self):
        pages = []
        for i in range(1,10):
            url = "http://www.tmsf.com/newhouse/property_searchall.htm?page=%s" % i
            page = scrapy.Request(url)
            pages.append(page)
        return pages

    # 将CSS数字替换成数字
    def rep_num(self, num):
        new_num = num.replace('numbbone','1').replace('numbbtwo','2').replace('numbbthree','3').replace('numbbfour','4').replace('numbbfive','5').replace('numbbsix','6').replace('numbbseven','7').replace('numbbeight','8').replace('numbbnine','9').replace('numbbzero','0')
        return new_num

    def parse(self, response):
        items = []
        for sel in response.xpath('//div[@class="build_des dingwei"]'):
            item = TmsfItem()
            item['name'] = sel.xpath('div[@class="build_pic"]/div[@class="dingwei"]/a/img/@title').extract()
            item['type'] = sel.xpath('div[@class="build_txt line26"]/div[@class="build_txt01"]/p[@class="build_txt03 colormg"]/text()').extract()
            item['location'] = sel.xpath('div[@class="build_txt line26"]/div[@class="build_txt01"]/p[@class="build_txt03 outof colormg"]/text()').extract()
            item['price'] = map(self.rep_num, [''.join(sel.xpath('div[@class="word1"]/span/@class').extract())])
            # 或结合正则匹配：item['price'] = map(self.rep_num, [''.join(sel.xpath('div[@class="word1"]/span').re(r'<span class="(.*)">'))])
            item['tel'] = sel.xpath('div[@class="build_txt05 txt05h25"]/font[@class="colordg"]/font[@class="colordg"]/text()').extract()
            item['link'] = [u"http://www.tmsf.com" + ''.join(sel.xpath('div[@class="build_pic"]/div[@class="dingwei"]/a/@href').extract())]
            item['avail'] = sel.xpath('div[@class="build_pic"]/div[@class="howsell"]//font[@class="colormg"]/a/text()').extract()
            # yield item
            items.append(item)
        return items
