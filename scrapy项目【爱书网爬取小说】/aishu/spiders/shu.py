import scrapy
from aishu.items import AishuItem
class A2shuSpider(scrapy.Spider):
    name = 'shu'
    allowed_domains = ['2shu.net']
    start_urls = [
        'http://www.2shu.net/dushu/0/975/99169.html'
    ]
    def parse(self, response):
        item = AishuItem()
        item['content'] = response.xpath('//*[@id="contents"]/text()').extract()
        # print(item)
        yield item
        next_url = response.xpath("//*[@id='amain']/dl/dd[2]/h3/a[3]/@href").extract_first()
        next_url = "http://www.2shu.net/dushu/0/975/" + next_url
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

