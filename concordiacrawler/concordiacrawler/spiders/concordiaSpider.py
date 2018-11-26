import os
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class concordiaSpider(CrawlSpider):
    name = "concordia_spider"
    start_urls = ["https://www.concordia.ca/about.html"]

    rules = (
        Rule(LinkExtractor(), callback='parse_items', follow=True),
    )

    def parse_items(self, response):

        results = {}
        results['url'] = response.url

        spans = []
        headers = []
        paragraphs = []
        footers = []

        # Retrieve the content
        title = response.meta['link_text'].split()
        for span in response.xpath('.//span/text()').re('\w+'):
            spans.append(span.lower())

        for h in response.xpath('//div').xpath('/html/body/*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6]/text()').re('\w+'):
            headers.append(h.lower())

        for paragraph in response.xpath('//div').xpath('.//p/text()').re('\w+'):
            paragraphs.append(paragraph.lower())

        for footer in response.xpath('.//footer/text()').re('\w+'):
            footers.append(footer.lower())

        content = [title + spans + headers + paragraphs + footers]
        results['content'] = content

        yield results


def crawl_spider(max_count):

    if os.path.exists('concordiaData.json'):
        os.remove('concordiaData.json')

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'CLOSESPIDER_ITEMCOUNT': max_count,
        'FEED_FORMAT': 'json',
        'FEED_URI': 'concordiaData.json'
    })

    process.crawl(concordiaSpider)
    process.start()


if __name__ == '__main__':
    max_count = 30
    crawl_spider(max_count)