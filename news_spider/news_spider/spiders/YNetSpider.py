#encoding=utf-8
import scrapy
from news_spider.items import NewsSpiderItem
import json
import time 
class YNetSpider(scrapy.Spider):

	name = 'ynet'
	allowed_domains = ["ynet.com"]
	start_urls = [
		'http://news.ynet.com'
	]
	base_url = 'yent.com'
	maxpage = 1#允许爬的最大的页数
	category_urls = [
		'http://news.ynet.com/list/990t76',
		'http://sports.ynet.com/list/735t1059'
	]
	category_type = [
		'news',
		'sports'
	]

#请求每一个分类,按页数来
	def parse(self,response):
		for ctg in self.category_urls:
			for pageindex in range(0,self.maxpage):
				if pageindex == 0:
					url = ctg + '.html'
				else:
					url = ctg + '_' + str(pageindex+1) + '.html'
				yield scrapy.Request(url=url,meta={'category_type': self.category_type[pageindex]}, callback=self.parseNewsHref)

#解析每页新闻列表的地址
	def parseNewsHref(self,response):
		category_type = response.meta['category_type']
		newsList = response.xpath(".//li[@class='cfix']")
		for news in newsList:
			item = NewsSpiderItem()
			item['type']=category_type
			item['title'] = news.xpath('.//h2/a/text()').extract_first()
			item['url'] = news.xpath('.//h2/a/@href').extract_first()
			item['summary'] = news.xpath('.//p/text()').extract_first()
			item['time'] = news.xpath(".//em[@class='fRight']/text()").extract_first()
			item['content'] = []
			yield scrapy.Request(url=item['url'], meta={'item': item},
								 callback=self.parseNews)
#			yield scrapy.Request(url="http://news.ynet.com/2017/04/06/82260t70.html", meta={'item': item},
#								 callback=self.parseNews)
#			break

	# 解析具体新闻内容
	def parseNews(self, response):
		item = response.meta['item']
		content_list = item['content']
		imgContent = {}
		scrollImgUrl = response.xpath("//div[@id='articleAll']/div[@class='scrollCon']/div[@class='scrollBox']/a/img/@src").extract_first()
#		print 'img='+scrollImgUrl
		if scrollImgUrl:
			imgContent['type'] = '0'
			imgContent['content'] = scrollImgUrl
			print 'retcontent='+imgContent.values()[0]
			content_list.append(imgContent)


		articleContent = response.xpath("//div[@class='articleBox cfix mb20']/p")
		for articleItem in articleContent:
			textContent = articleItem.xpath('text()').extract_first()
			imgurl = articleItem.xpath("./img/@src").extract_first()
#			print 'textContent=' + textContent
			retContent = {}
			if textContent:
				retContent['type'] = '1'
				retContent['content'] = textContent
			elif imgurl:
				retContent['type'] = '0'
				retContent['content'] = imgurl
			else:
				continue
			content_list.append(retContent)
#			break

		item['content'] = content_list
#		print item['content'][0]
		scrollRightUrl = response.xpath(
			"//div[@id='articleAll']/div[@class='scrollCon']/div[@class='scrollBox']/a[@class='scrollRight']/@href").extract_first()
		if scrollRightUrl:
			yield scrapy.Request(url=scrollRightUrl, meta={'item': item},
									 callback=self.parseNews)
		else:
			yield item

	# 解析具体新闻内容
	def parsePageBox(self, response):
		item = response.meta['item']
		content_list = item['content']

		retContent = {}
		scrollImgUrl = response.xpath("//div[@id='articleAll']/div[@class='scrollCon']/div[@class='scrollBox']/a/img/@src").extract_first()
		print 'img='+scrollImgUrl
		if scrollImgUrl:
			retContent['type'] = '0'
			retContent['content'] = 'http:' + scrollImgUrl
			content_list.append(retContent)
		#	print retContent

		articleContent = response.xpath("//div[@class='articleBox cfix mb20']/p")
		for articleItem in articleContent:
			textContent = articleItem.xpath('text()').extract_first()
			imgurl = articleItem.xpath(".//img/@src").extract_first()
			if textContent:
				retContent['type']='1'
				retContent['content']=textContent
			elif imgurl:
				retContent['type'] = '0'
				retContent['content'] = 'http:'+imgurl
			else:
				continue
			content_list.append(retContent)
#			break
		item['content'] = content_list
		yield item

	def printC(self,text):
		print'printC:'+text.encode('utf-8')
