import scrapy

class WikiItem(scrapy.Item):
    title = scrapy.Field()
    director = scrapy.Field()
    year = scrapy.Field()
    genre = scrapy.Field()
    country = scrapy.Field()
