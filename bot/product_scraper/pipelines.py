# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# from scrapy.exceptions import DropItem
# useful for handling different item types with a single interface


# class ProductScraperPipeline:
#     def process_item(self, item, spider):
#         return item

  # vat_factor = 1.15

  #   def process_item(self, item, spider):
  #       adapter = ItemAdapter(item)
  #       if adapter.get('price'):
  #           if adapter.get('price_excludes_vat'):
  #               adapter['price'] = adapter['price'] * self.vat_factor
  #           return item
  #       else:
  #           raise DropItem(f"Missing price in {item}")
import json

from itemadapter import ItemAdapter

class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item