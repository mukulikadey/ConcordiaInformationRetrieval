import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class concordiaSpider(scrapy.Spider):
    name = "concordia_spider"

    def start_requests(self):
        # COUNT_MAX = 10
        
        # custom_settings = {
        #     'CLOSESPIDER_PAGECOUNT': COUNT_MAX
        # }

        allowed_domains = ["concordia.ca"]
        start_urls = ["https://www.concordia.ca/about.html"]

        # rules = (
        #     Rule(LinkExtractor(), callback=self.parse, follow=True),
        # )

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]

        filename = 'concordia-%s.html' % page

        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log('Saved file %s' % filename)
