from ..items import OsonItem
from scrapy.http import Request
import scrapy
import os

class Artist(scrapy.Spider):
    name = 'artist'
    allowed_domains = ["www.livenation.es"]
    max_id = 7
    if os.path.exists("groups.txt"):
        os.remove("groups.txt")

    def start_requests(self):
        for i in range(self.max_id):
            yield Request('https://www.livenation.es/event/allevents?page=%d' % i, self.parse)

    def parse(self, response):
        items = OsonItem()
        all_groups_spans = response.css("span.result-info__localizedname::text")
        for span in all_groups_spans:
            items['group'] = span.extract()
            with open('groups.txt', 'a+') as f:
                f.write(items['group']+"\n")