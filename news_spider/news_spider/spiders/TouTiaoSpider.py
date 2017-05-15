#encoding=utf-8
import scrapy
from news_spider.items import TitleSpiderItem
import json
import time 
class TouTiaoSpider(scrapy.Spider):

	name = 'toutiao'
	allowed_domains = ["toutiao.com"]
	start_urls = [
	'http://www.toutiao.com/api/pc/feed/?category=funny'
	]
	base_url = 'http://www.toutiao.com/'

#请求每一个分类,按页数来
	def parse(self,response):
		js = json.loads(response.body)
		hasMore = js["has_more"]
		message = js["message"]
		data = js["data"]

		for dataitem in data:
			item = TitleSpiderItem()
			item["group_id"] = dataitem["group_id"]
			item["title"] = dataitem["title"]
			item["type"] = "23"
			item["url"] = ""
			item["introduction"] = dataitem["abstract"]
			coverarray = dataitem["image_list"]
			cover = "["
			firstItem = 1
			for coverItem in coverarray:
				if(firstItem==1):
					cover = cover + '"' + coverItem["url"] + '"'
					firstItem = 0
				else:
					cover = cover+',"' + coverItem["url"] + '"'
			cover = cover + "]"
			print cover
			item["cover"] = cover#dataitem["image_list"][0]["url"]
			item["content_type"] = "1"
			item["cover_show_type"]="3"
			item["source"] = dataitem["source"]
			item['content'] = []
			detailurl = self.base_url + 'a' + dataitem["group_id"]
			yield scrapy.Request(url=detailurl, meta={'item': item},
							 callback=self.parseDetail)
			break

#解析具体新闻内容
	def parseDetail(self,response):
		item = response.meta['item']
		content_list = item['content']
		tm = response.xpath("//div[@class='articleInfo']/span[@class='time']/text()").extract_first()
#		self.printC(tm)
		divs = response.xpath("//div[@class='article-content']/div/p")
		content=""
		for articleItem in divs:
			textContent = articleItem.xpath('text()').extract_first()
			if textContent is None:
				content = content + articleItem.extract()
			else:
				content = content + textContent
		if(len(tm)!=0 and len(content)!=0):
			item['publish_time'] = str(int(time.mktime(time.strptime(tm,'%Y-%m-%d %H:%M'))))
			date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
			item['show_time'] = str(int(time.mktime(time.strptime(date,'%Y-%m-%d %H:%M'))))
			item['content'] = content
		yield item

	def printC(self,text):
		print'printC:'+text.encode('utf-8')
