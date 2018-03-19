# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor

dest='/home/lol/Desktop/patrika_hindi/data'
if not os.path.exists(dest):
	os.makedirs(dest)
	print("folder created")
class spidey(CrawlSpider):
	name = 'spidey'
	allowed_domains = ['patrika.com']
	start_urls = ['https://www.patrika.com/']
	#Note:callback function name should always be something different from parse
	rules=(Rule(LxmlLinkExtractor(allow=(),deny=()),callback="parse_page",follow=True),)
	def parse_page(self, response):
			c=response.css('h1::text').extract()
			print(c)		
			content = (''.join(response.xpath('//div[@class="complete-story"]/p/text()').extract())).encode("UTF-8")
			if (((len(c)!=0)) and (len(content)>20)):
				urlstr=response.url
				print(urlstr)
				print("\n\n")
				urlstrclean = ''.join(e for e in urlstr if e.isalnum())
				try:
					fil=open(os.path.join(dest,urlstrclean+'.txt'),'w')
					print("OPENED!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
				except IOerror:
					print("couldnt open!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
				fil.write(c[0].encode("UTF-8"))
				fil.write(content)
				fil.close()
				yield {'h1':urlstrclean}
