import os

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from concordiacrawler.items import ConcordiacrawlerItem


class concordiaSpider(scrapy.Spider):
    name = 'concordia_spider'
    start_urls = ['https://www.concordia.ca/about.html']

    def parse(self, response):
        link_extractor = LinkExtractor()
        links = link_extractor.extract_links(response)

        print('Amount of links')
        print(len(links))

        for link in links:
            yield scrapy.Request(link.url, callback=self.parse_inner_page)

    def parse_inner_page(self, response):
        item = ConcordiacrawlerItem()
        item['body'] = response.body

        file_path = response.url.replace('/', 'z').replace(':', 'z')[5:240] + '.html'

        path_parts = ['FILES/', file_path, '.html']
        path = ''.join(path_parts)

        if not os.path.exists('FILES/'):
            os.makedirs('FILES/')

        with open(path, 'w') as f:
            f.write(response.body)

        self.log('Saved file %s' % file_path)

        return item
