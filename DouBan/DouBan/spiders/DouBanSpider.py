# -*- coding: utf-8 -*-
import scrapy
import json
from DouBan.items import BookItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.shell import inspect_response

api_url = "http://api.douban.com/v2/book/"

class DoubanspiderSpider(scrapy.spiders.CrawlSpider):
    name = "DouBanSpider"
    allowed_domains = ["book.douban.com","api.douban.com"]
    start_urls = (
        'http://book.douban.com/',
    )

    #rule = Rule(LinkExtractor(allow = 'douban\.com'), callback = 'parse_main')#extract rules for book.douban.com

    def parse_start_url(self, response):
        urls = response.xpath('//div[@class="cover"]/a/@href').extract()
        bookId_file = open('.\\book_id.txt', 'wb')
        for bookId in urls:
            if(bookId.split('/')[-3].find('subject') != -1):
                bookId_file.write(str(bookId) + '\n')
                yield scrapy.Request(api_url + bookId.split('/')[-2].encode('utf-8'), callback = self.parse_json)
        bookId_file.close()


    def parse_json(self, response):
        raw_data = response.selector.extract().encode('utf-8')
        json_data = json.loads(raw_data[raw_data.find('{'):raw_data.rfind('}') + 1])
        
        book_info = BookItem()
        book_info =  self.create_item(json_data)
        
        yield book_info

    def create_item(self, json_data):
        book_info = BookItem()

        book_info['rating'] = json_data['rating']
        book_info['subtitle'] = json_data['subtitle']
        book_info['author'] = json_data['author']
        book_info['pubdate'] = json_data['pubdate']
        book_info['urlId']= json_data['id']
        book_info['price'] = json_data['price']
        book_info['pages'] = json_data['pages']
        book_info['isbn10'] = json_data['isbn10']
        book_info['isbn13'] = json_data['isbn13']
        book_info['tags'] = json_data['tags']
        book_info['publisher'] = json_data['publisher']
        book_info['translator'] = json_data['translator']
        book_info['title'] = json_data['title']

        return book_info