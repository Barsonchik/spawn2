# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy  # Make sure to import scrapy here
import os

class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = item['image_name'].replace(" ", "_")  # Replace spaces with underscores
        return f"{item['category']}/{image_name}.jpg"

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'])
