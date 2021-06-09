# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import xlsxwriter


class MedicinePipeline:

    # 초기화 메소드
    def __init__(self):
        self.workbook = xlsxwriter.Workbook('medicine_data.xlsx')
        self.worksheet = self.workbook.add_worksheet('약품정보')
        self.count = 2

    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info('==== Writer Header ====')

        self.worksheet.write('A1', '품목일련번호')
        self.worksheet.write('B1', '품목명')
        self.worksheet.write('C1', '제조사')
        self.worksheet.write('D1', '포장정보')
        self.worksheet.write('E1', '유효기간')
        self.worksheet.write('F1', '효능효과')
        self.worksheet.write('G1', '저장방법')
        self.worksheet.write('H1', '주의사항')
        self.worksheet.write('I1', '복용방법')
        self.worksheet.write('J1', '주성분')
        self.worksheet.write('K1', '약품이미지URL')
        self.worksheet.write('L1', '보험코드')
        self.worksheet.write('M1', '품목구분')

    # Item 건별 실행
    def process_item(self, item, spider):
        self.worksheet.write('A%s' % self.count, item.get('medicine_seq_no'))
        self.worksheet.write('B%s' % self.count, item.get('medicine_name'))
        self.worksheet.write('C%s' % self.count, item.get('company_name'))
        self.worksheet.write('D%s' % self.count, item.get('unit'))
        self.worksheet.write('E%s' % self.count, item.get('expiration_date'))
        self.worksheet.write('F%s' % self.count, item.get('effect'))
        self.worksheet.write('G%s' % self.count, item.get('store_method'))
        self.worksheet.write('H%s' % self.count, item.get('user_attention'))
        self.worksheet.write('I%s' % self.count, item.get('usage_volume'))
        self.worksheet.write('J%s' % self.count, item.get('main_ingredient'))
        self.worksheet.write('M%s' % self.count, item.get('medicine_kind_cd'))

        self.count += 1

        return item

    # 종료시 1회 실행
    def close_spider(self, spider):
        spider.logger.info('==== Excel Writer End ====')

        self.workbook.close()
