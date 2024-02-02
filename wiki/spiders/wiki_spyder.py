import scrapy
from urllib.parse import urljoin
from wiki.items import WikiItem

class WikiSpider(scrapy.Spider):
    name = "wiki"
    start_urls = [
        'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A4%D0%B8%D0%BB%D1%8C%D0%BC%D1%8B_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    ]

    visited_urls = []

    def parse(self, response):

        for post_link in response.xpath(
                '//div[@class="mw-category-group"]/ul/li/a/@href').extract():
            url = 'https://ru.wikipedia.org'+post_link
            print('URL: ', post_link)
            yield response.follow(url, callback=self.parse_post)
        next_page = response.xpath(
                '//*[@id="mw-pages"]/a[2]/@href').extract()
        next_page_url = 'https://ru.wikipedia.org' + next_page[0]
        yield response.follow(next_page_url, callback=self.parse)

    def parse_post(self, response):
        item = WikiItem()
        title = response.xpath(
            '//*[@id="firstHeading"]/span/text()').extract()
        item['title'] = title

        director = response.xpath(
            '//*[@data-wikidata-property-id = "P57"]/a/text() | //*[@data-wikidata-property-id = "P57"]/span/span/a/span/text() | //*[@data-wikidata-property-id = "P57"]/span/a/text() | //*[@data-wikidata-property-id = "P57"]/text()').extract()
        item['director'] = director

        year = response.xpath(
            '//*[@data-wikidata-property-id = "P577"]/text() | //*[@class = "dtstart"]/text() | //*[@class = "nowrap"]/a/text() | //td[@class = "plainlist"]/a/text()').extract()
        item['year'] = year

        genre = response.xpath(
            '//*[@data-wikidata-property-id = "P136"]/a/text() | //*[@data-wikidata-property-id = "P136"]/text() | //*[@data-wikidata-property-id = "P136"]/span/a/text()').extract()
        item['genre'] = genre

        country = response.xpath(
            '//*[@data-wikidata-property-id = "P495"]/a/text() | //*[@class = "wrap"]/text() | //*[@class = "country-name"]/span/a/text() | //*[@data-wikidata-property-id = "P495"]/text()').extract()
        item['country'] = country
        yield item