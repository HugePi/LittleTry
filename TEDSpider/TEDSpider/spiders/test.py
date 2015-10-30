# -*- coding: utf-8 -*-
import scrapy
from TEDSpider.items import TEDSpiderItem
from TEDSpider.items import TEDTranscriptItem
from scrapy.exporters import CsvItemExporter

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["ted.com"]
    start_urls = (
        r'http://www.ted.com/talks',
    )
    
    def parse(self, response):
        for href in response.xpath('//h4/a/@href'):
            item = TEDSpiderItem()
            item['href'] = href.extract()
            yield scrapy.Request('http://www.ted.com' + item['href'] + '/transcript?language=en', callback = self.parse_transcript)

    def parse_transcript(self, response):
        article = ''
        filename = '.\Response\\'
        for transcript_line in response.xpath("//span[@class='talk-transcript__fragment']/text()"):
            article = article + transcript_line.extract()
        filename = filename + response.url.split('/')[-2] + '.txt'
        
        with open(filename, 'wb') as f:
            f.write(article)
        
            
