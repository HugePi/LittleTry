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
		item_str = 'urlId: ' + str(item['urlId']) + '\n' + 'title: ' + str(item('title')) + '\n\n'
		self.file.write(item_str)
		return item
	def close_spider(self, spider):
		self.file.close()