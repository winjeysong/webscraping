# _*_ coding:utf-8 _*_

import scrapy
from tmsf.items import TmsfItem

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


class TmsfSpider(scrapy.spiders.Spider):
    name = "tmsf"
    allow_domains = ["http://www.tmsf.com"]
    start_urls = ["http://www.tmsf.com/newhouse/property_searchall.htm?page=1"]
    # "http://www.tmsf.com/newhouse/property_searchall.htm?page="
    '''
    def create_request(self):
        global headers
        url0 = "http://www.tmsf.com/newhouse/property_searchall.htm?page="
        for i in range(10):
            url = url0 + str(i)
            self.start_urls.append(url)
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse_next)
    '''

    def parse(self, response):
        items = []
        for sel in response.xpath('//div[@class="build_des dingwei"]'):
            item = TmsfItem()
            item['name'] = sel.xpath('div[@class="build_txt line26"]/div[@class="build_word01"]/text()').extract()
            item['ad_name'] = sel.xpath('div[@class="build_txt line26"]/div[@class="build_word01"]/div[@class="fl line26 mgl black"]/text()').extract()
            item['type'] = sel.xpath('div[@class="build_txt line26"]/div[@class="build_txt01"]/p[@class="build_txt03 colormg"]/text()').extract()
            item['location'] = sel.xpath('div[@class="build_txt line26"]/div[@class="build_txt01"]/p[@class="build_txt03 outof colormg"]/text()').extract()
            # item['price'] = sel.xpath('').extract()
            item['tel'] = sel.xpath('div[@class="build_txt05 txt05h25"]/font[@class="colordg"]/font[@class="colordg"]/text()').extract()
            item['link'] = [u"http://www.tmsf.com"] + sel.xpath('div[@class="build_pic"]/div[@class="dingwei"]/a/@href').extract()
            item['avail'] = sel.xpath('div[@class="build_pic"]/div[@class="howsell"]//font[@class="colormg"]/a/text()').extract()
            # yield item
            items.append(item)
        return items


