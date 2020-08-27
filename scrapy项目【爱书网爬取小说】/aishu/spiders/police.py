import scrapy
from aishu.items import AishuItem
class A2shuSpider(scrapy.Spider):
    name = 'police'
    allowed_domains = ['2shu.net']
    start_urls = [
        'http://www.2shu.net/dushu/1/1610/121346.html'
    ]
    def parse(self, response):
        item = AishuItem()
        item['content'] = response.xpath('//*[@id="contents"]/text()').extract()
        # print(item)
        yield item
        next_url = response.xpath("//*[@id='footlink']/a[3]/@href").extract_first()

        next_url = "http://www.2shu.net/dushu/1/1610/" + next_url
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )