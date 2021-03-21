import scrapy


class BiliItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    id = scrapy.Field()
    uid = scrapy.Field()
    extension = scrapy.Field()
