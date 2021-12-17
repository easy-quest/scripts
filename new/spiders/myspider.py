import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class MySpider(CrawlSpider):
    name = 'crawl_spider'
    allowed_domains = ['clever-lichterman-044f16.netlify.com']
    start_urls = ['https://clever-lichterman-044f16.netlify.com/products/']
 
    rules = (
        
        Rule(LinkExtractor(allow=('products', )), callback='parse_product'),
    )
 
    def parse_product(self, response):

        l = ItemLoader(item=Product(), response=response)
        l.add_xpath('price', "//div[@class='my-4']/span/text()")
        l.add_xpath('title', '//section[1]//h2/text()')
        l.add_xpath('title', '//title')
        l.add_value('product_url', response.url)
        return l.load_item()