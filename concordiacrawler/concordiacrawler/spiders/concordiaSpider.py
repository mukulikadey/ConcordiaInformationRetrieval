import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class concordiaSpider(scrapy.Spider):
    name = "concordia_spider"
    start_urls = ["https://www.concordia.ca/about.html"]

    def parse(self, response):
        print("Printing Response")
        print(response)

        link_extractor = LinkExtractor()
        links = link_extractor.extract_links(response)

        for link in links:
            print(link.url)

            page = response.url.split("/")[-2]

            filename = 'concordia-%s.html' % page

            with open(filename, 'wb') as f:
                f.write(response.body)

            self.log('Saved file %s' % filename)
