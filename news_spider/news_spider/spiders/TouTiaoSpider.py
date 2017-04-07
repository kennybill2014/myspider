#encoding=utf-8
import scrapy
from news_spider.items import NewsSpiderItem
import json
import time 
class TouTiaoSpider(scrapy.Spider):

	name = 'toutiao'
	allowed_domains = ["toutiao.com"]
	start_urls = [
	'http://toutiao.com/articles_news_society/p1'
	]
	base_class_url = 'http://toutiao.com/articles_news_society'
	base_url = 'http://toutiao.com'
#maxpage = 501;#允许爬的最大的页数
	maxpage = 2;#允许爬的最大的页数
	category = ['articles_news_society'
	]

#请求每一个分类,按页数来
	def parse(self,response):
		for ctg in self.category:
			for page in range(1,self.maxpage):
				url = self.base_url+'/'+ctg+'/p'+str(page)
#				yield scrapy.Request(url,self.parseNewsHref)
				yield scrapy.Request(url, self.parseNewsHref)

#解析每页新闻列表的地址
	def parseNewsHref(self,response):
		urls = response.xpath("//div[@class='info']//a/@href").extract()
		for url in urls:
			news_url = self.base_url+url
			yield scrapy.Request(news_url,self.parseNews)

#解析具体新闻内容
	def parseNews(self,response):
		articles = response.xpath("//div[@id='article-main']")
		item = NewsSpiderItem()
		title = articles.xpath("//h1[@class='article-title']/text()").extract_first()
#		self.printC(title)
		tm = articles.xpath("//div[@class='articleInfo']//span[@class='time']/text()").extract_first()
#		self.printC(tm)
		titlesrc = articles.xpath("//div[@class='articleInfo']//span[@class='src']/text()").extract_first()
		divs = articles.xpath("//div[@class='article-content']")
		content=""
		for p in divs.xpath(".//p"):
			content =  content + p.extract()
		self.printC(tm)
		if(len(title)!=0 and len(tm)!=0 and len(content)!=0):
			item['title'] = title
			item['time'] = int(time.mktime(time.strptime(tm,'%Y-%m-%d %H:%M')))
			item['src'] = titlesrc
			item['url'] = response.url
			item['content'] = content
			yield item

	def printC(self,text):
		print'printC:'+text.encode('utf-8')
