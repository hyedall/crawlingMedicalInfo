import scrapy


class MedicinespiderSpider(scrapy.Spider):
    name = 'medicinespider'
    allowed_domains = ['nedrug.mfds.go.kr']
    start_urls = ['https://nedrug.mfds.go.kr/']

    def parse(self, response):
        pass
