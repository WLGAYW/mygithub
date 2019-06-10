# -*- coding: utf-8 -*-
import scrapy
import os
import re
import sys

os.chdir('../..') # 返回上上级文件
main_path = os.getcwd() # 获得当前路径
import_path = main_path + '/' + 'permit' + '/' + 'permit' + '/' + 'utils'
# os.chdir(import_path)
sys.path.append(import_path)
print(sys.path)

from domain_name_get import get_domain_name # 读取不到这


class ChinazMainSpiderSpider(scrapy.Spider):
    name = 'chinaz_spider'

    def start_requests(self):
        domain_name_list = get_domain_name()
        for domain_name in domain_name_list:
            spider_url = 'http://icp.chinaz.com/{}'.format(domain_name)
            print(spider_url)

            chainz_headers = {
                'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'Accept-Encoding': "gzip, deflate",
                'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
                'Cache-Control': "max-age=0",
                'Connection': "keep-alive",
                'Content-Length': "80",
                'Content-Type': "application/x-www-form-urlencoded",
                'Host': "icp.chinaz.com",
                'Origin': "http://icp.chinaz.com",
                'Referer': "http://icp.chinaz.com/",
                'Upgrade-Insecure-Requests': "1",
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                'cache-control': "no-cache",
            }
            chainz_post_data = {
                'type': 'host',
                's': '{}'.format(domain_name),
                'guid': 'http://27.152.153.28:9821/',
                'code': '',
                'havecode': '0'
            }
            yield scrapy.FormRequest(
                url=spider_url,
                headers=chainz_headers,
                formdata=chainz_post_data,
                callback=self.parse
            )

    def parse(self, response):
        if response.status == 200:
            print(response.text)

        else:
            print('请求失败~!!!!!!!!!!!!!!')


