# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    product_url = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
