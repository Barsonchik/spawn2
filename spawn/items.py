# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ImageItem(scrapy.Item):
    image_url = scrapy.Field()
    image_name = scrapy.Field()
    category = scrapy.Field()
    images = scrapy.Field()  # Для хранения загруженных изображений
