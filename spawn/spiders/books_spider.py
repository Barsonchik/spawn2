import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImageItem

class BooksSpider(CrawlSpider):
    name = "books_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a"), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"), follow=True),
    )

    def parse_item(self, response):
        item = ImageItem()
        item['image_url'] = response.xpath("//div[@class='item active']/img/@src").get()
        item['image_name'] = response.xpath("//h1/text()").get()
        item['category'] = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
        item['image_url'] = response.urljoin(item['image_url'])  # Полный URL изображения

        yield item
