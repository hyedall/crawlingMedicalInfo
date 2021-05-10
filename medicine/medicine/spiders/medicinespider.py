import scrapy
import re
import math
from ..items import MedicineItem


class MedicineSpider(scrapy.Spider):
    name = 'medicinespider'
    allowed_domains = ['nedrug.mfds.go.kr']
    start_urls = ['https://nedrug.mfds.go.kr/searchDrug']

    def parse(self, response):
        self.logger.info('drug_url ====> %s' % response.url)

        # 총건수를 문자에서 숫자 타입으로 변환 (예) 107,028 => 107028
        totalCnt = int(''.join(re.findall('\d+', response.css('div.search_top.mb10 > p > strong::text').get())))
        self.logger.info('totalCnt ====> %s' % totalCnt)
        # 페이지당 게시물이 15건이므로 페이지 수를 계산함
        totalPage = math.ceil(totalCnt / 15)
        self.logger.info('totalPage ====> %s' % totalPage)

        # 전체 페이지를 순회함
        # for pageNum in range(1, totalPage+1):
        for pageNum in range(1, 4):
            pageUrl = 'https://nedrug.mfds.go.kr/searchDrug?page=' + str(pageNum)
            yield scrapy.Request(pageUrl, self.parse_list_item)

    # 약푹목록 페이지의 response
    def parse_list_item(self, response):

        self.logger.info('drug_list_url ====> %s' % response.url)
        # self.logger.info('drug_list_text ====> %s' % response.text)

        # 페이지에 있는 약품들을 하나씩 확인함
        for medicine_item in response.css('table.dr_table.dr_table_type2 > tbody > tr'):
            # self.logger.info('medicine_item ====> %s' % medicine_item)
            # self.logger.info('medicine_item.get() ====> %s' % medicine_item.get())

            # 약품 하나의 세부 정보를 조회하는 테스트, 약품명, 제조사등
            # for td_items in medicine_item.css('td'):
            #     self.logger.info('td_items ===> %s' % td_items)
            #     self.logger.info('td_items.get() ===> %s' % td_items.get())

            # class나 id로 td를 판별하기 힘들기 때문에 하나씩 직접 가져옴
            # 약품명
            medicine_name = medicine_item.xpath('//td[2]')
            self.logger.info('medicine_name ===> %s' % medicine_name)
            self.logger.info('medicine_name.get() ===> %s' % medicine_name.get())







