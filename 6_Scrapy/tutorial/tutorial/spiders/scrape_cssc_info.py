# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'cssc-info-xpath'
    # http: // www.cssc.net.cn / n11 / index.html for cssc companies name
    start_urls = [
        'http://www.cssc.net.cn/n11/index.html',
    ]

    def parse(self, response):
        # for quote in response.xpath('//ul[@class="web_tab_list"]'):
        #     yield {
        #         'text': quote.xpath('./li/a/text()').extract(),
        #         'website': quote.xpath('./li/a/@href').extract()
        #     }
        for quote in response.xpath('//ul[@class="web_tab_list"]/li/a'):
            yield {
                'company': quote.xpath('text()').extract(),
                'website': quote.xpath('@href').extract()
            }