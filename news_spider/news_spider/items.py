# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NewsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	title = scrapy.Field()
	time = scrapy.Field()
	content = scrapy.Field()
	url = scrapy.Field()
	type = scrapy.Field()
	summary = scrapy.Field()

class TitleSpiderItem(scrapy.Item):
	id = scrapy.Field()
	title = scrapy.Field()
	type = scrapy.Field()
	url = scrapy.Field()
	introduction = scrapy.Field()
	cover = scrapy.Field()
	content = scrapy.Field()
	content_type = scrapy.Field()
	show_time = scrapy.Field()
	publish_time = scrapy.Field()
	group_id = scrapy.Field()
	source = scrapy.Field()
	cover_show_type = scrapy.Field()


