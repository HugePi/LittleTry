# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookInfoPipeline(object):
	def __init__(self):
		self.file = open('.\\json_output.txt','wb')

	def process_item(self, item, spider):
		author_info = str(item['urlId']) + '\n'
		self.file.write(author_info)
		return item
	def close_spider(self, spider):
		self.file.close()