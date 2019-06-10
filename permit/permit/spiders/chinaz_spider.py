# -*- coding: utf-8 -*-
import scrapy


class ChinazSpiderSpider(scrapy.Spider):
    name = 'chinaz_spider'
    allowed_domains = ['icp.chinaz.com/']
    start_urls = ['http://icp.chinaz.com//']

    def parse(self, response):
        pass
