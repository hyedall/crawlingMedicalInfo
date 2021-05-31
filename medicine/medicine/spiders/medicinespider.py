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

        # self.logger.info('drug_list_url ====> %s' % response.url)
        # self.logger.info('drug_list_text ====> %s' % response.text)

        # 페이지에 있는 약품들을 하나씩 확인함
        for medicine_item in response.css('table.dr_table.dr_table_type2 > tbody > tr'):
            # self.logger.info('medicine_item ====> %s' % medicine_item)
            # self.logger.info('medicine_item.get() ====> %s' % medicine_item.get())

            # medicine_item 처리방식 1
            # class나 id로 td를 판별하기 힘들기 때문에 하나씩 직접 가져옴
            # 품목명 (약품명)
            # medicine_name = medicine_item.xpath('./td[2]/span/a/text()').get()
            medicine_name = medicine_item.css('td:nth-child(2) > span > a::text').get()
            # self.logger.info('medicine_name ===> %s' % medicine_name)

            # 품목일련번호
            # medicine_seq_no = medicine_item.xpath('./td[4]/span[2]/text()').get()
            medicine_seq_no = medicine_item.css('td:nth-child(4) > span:nth-child(2)::text').get()
            # self.logger.info('medicine_seq_no ===> %s' % medicine_seq_no)

            # 제조사 (업체명)
            # company_name = medicine_item.xpath('./td[3]/span[2]/text()').get()
            company_name = medicine_item.css('td:nth-child(3) > span:nth-child(2)::text').get()
            # self.logger.info('company_name ===> %s' % company_name)

            # 주성분 (유효성분)
            # main_ingredient = medicine_item.xpath('./td[10]/span[2]/text()').get()
            main_ingredient = medicine_item.css('td:nth-child(10) > span:nth-child(2)::text').get()
            # self.logger.info('main_ingredient ===> %s' % main_ingredient)

            # 품목구분(의약품, 의약외품, 생물의약품, 마약류, 첨단바이오, 한약(생약)제제등
            # medicine_kind_cd = medicine_item.xpath('./td[7]/span[2]/text()').get()
            medicine_kind_cd = medicine_item.css('td:nth-child(7) > span:nth-child(2)::text').get()
            # self.logger.info('medicine_kind_cd ===> %s' % medicine_kind_cd)

            # 상세페이지 URL. 리스트에는 없는 정보를 가져올.
            detail_url = medicine_item.css('td:nth-child(2) > span > a::attr(href)').get()
            # self.logger.info('detail_url ===> %s' % detail_url)

            yield scrapy.Request(response.urljoin(detail_url), self.parse_detail,
                                 meta={'medicine_name': medicine_name, 'medicine_seq_no': medicine_seq_no,
                                       'company_name': company_name, 'main_ingredient': main_ingredient,
                                       'medicine_kind_cd': medicine_kind_cd})

    def parse_detail(self, response):
        # self.logger.info('drug_detail_list_url ====> %s' % response.url)
        # self.logger.info('drug_detail_list_text ====> %s' % response.text)

        detail_count = 1

        store_method = ''
        expiration_date = ''
        unit = ''
        for detail_info in response.css('table.s-dr_table.dr_table_type2.s-view-table.ss_table > tr'):

            if detail_count == 1:
                # 저장방법 DB store_method
                # self.logger.info("### 저장방법 %s" % detail_info.xpath('td/text()').extract())
                # self.logger.info("### [[저장방법]] %s" % detail_info.css('td::text').get())
                store_method = detail_info.css('td::text').get()
            elif detail_count == 2:
                # 유효기간(사용기간) - DB expiration_date,
                # self.logger.info("### [[유효기간(사용기간)]] %s" % detail_info.css('td::text').get())
                expiration_date = detail_info.css('td::text').get()
            elif detail_count == 5:
                # 포장정보 - DB unit
                # self.logger.info("### [[포장정보]] %s" % detail_info.css('td::text').get())
                unit = detail_info.css('td::text').get()

            detail_count += 1

        # self.logger.info('%s--%s--%s' % (store_method, expiration_date, unit) )

        # 복용방법 (용법용량) - DB usage_Volume,
        usage_volume = ''
        for usage_volume_html in response.css('div.info_box.mt20.pt0 p'):
            # self.logger.info('[복용방법]%s' % usage_volume_html.css('p::text').get())
            try:
                usage_volume += usage_volume_html.css('p::text').get() + '\n'
            except TypeError:
                self.logger.info('[복용방법 TypeError]%s' % usage_volume_html.css('p::text').get())

        # self.logger.info('[복용방법]%s' % usage_volume)

        # 효능효과 - DB effect,
        effect = ''
        for effect_html in response.css('div#_ee_doc p'):
            # self.logger.info('[효능효과]%s' % effect_html.css('p::text').get())
            try:
                effect += effect_html.css('p::text').get() + '\n'
            except TypeError:
                self.logger.info('[효능효과 TypeError]%s' % effect_html.css('p::text').get())

        # self.logger.info('[효능효과]%s' % effect)

        # 주의사항 (사용자주의사항) DB - userAttention, info_box mt30 pt0 notice
        user_attention = ''
        for user_attention_html in response.css('div.info_box.mt30.pt0.notice p'):
            # self.logger.info('[주의사항 (사용자주의사항)]%s' % user_attention_html.css('p::text').get())
            try:
                user_attention += user_attention_html.css('p::text').get() + '\n'
            except TypeError:
                self.logger.info('[주의사항 (사용자주의사항) TypeError]%s' % user_attention_html.css('p::text').get())

        # self.logger.info('[주의사항 (사용자주의사항)]%s' % user_attention)

        item = MedicineItem()
        item['medicine_seq_no'] = response.meta['medicine_seq_no']
        item['medicine_name'] = response.meta['medicine_name']
        item['company_name'] = response.meta['company_name']
        item['unit'] = unit
        item['expiration_date'] = expiration_date
        item['effect'] = effect
        item['store_method'] = store_method
        item['user_attention'] = user_attention
        item['usage_volume'] = usage_volume
        item['main_ingredient'] = response.meta['main_ingredient']
        item['medicine_kind_cd'] = response.meta['medicine_kind_cd']

        yield item

        # https://www.tutorialspoint.com/scrapy/scrapy_requests_and_responses.htm
        # return scrapy.Request(self.tablet_url + "200500547", self.parse_tablet,
        #                       meta={'medicine_name': response.meta['medicine_name'],
        #                             'medicine_seq_no': response.meta['medicine_seq_no'],
        #                             'company_name': response.meta['company_name'],
        #                             'main_ingredient': response.meta['main_ingredient'],
        #                             'medicine_kind_cd': response.meta['medicine_kind_cd']})

        # def parse_tablet(self, response):
        #     self.logger.info('parse_tablet_url ====> %s' % response.url)
        #     self.logger.info('parse_tablet_text ====> %s' % response.url)
        #     print()
        #     print()
        #     self.logger.info(response)
        #     print()
        #     print()

        # 낱알 정보 #########
        # 약품이미지URL

        # 보험코드

        """ medicine_item 처리방식 2
        # medicine_item( tr) 의 하위의 td를 for문을 통해 처리하는 방식
        # for i, td_items in enumerate(medicine_item.css('td')):
        # self.logger.info('td_items index ===> %d' % i)
        # self.logger.info('td_items ===> %s' % td_items)
        # self.logger.info('td_items.get() ===> %s' % td_items.get())
        # 품목명 (약품명)
        # if i == 1:
        #     medicine_name = td_items.css('span > a::text').get()
        #     self.logger.info('medicine_name ===> %s' % medicine_name)

        # 품목일련번호
        # elif i == 3:
        #     medicine_seq_no = td_items.css('span:nth-child(2)::text').get()
        #     self.logger.info('medicine_seq_no ===> %s' % medicine_seq_no)
        """
