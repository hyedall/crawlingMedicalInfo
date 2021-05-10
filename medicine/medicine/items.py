# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MedicineItem(scrapy.Item):

    # 품목일련번호
    medicine_seq_no = scrapy.Field()

    # 품목명 (약품명)
    medicine_name = scrapy.Field()

    # 제조사 (업체명)
    company_name = scrapy.Field()

    # 포장정보
    unit = scrapy.Field()

    # 유효기간
    expiration_date = scrapy.Field()

    # 효능효과
    effect = scrapy.Field()

    # 저장방법
    store_method = scrapy.Field()

    # 주의사항 (사용자주의사항)
    user_attention = scrapy.Field()

    # 복용방법 (용법용량)
    usage_volume = scrapy.Field()

    # 주성분 (유효성분)
    main_ingredient = scrapy.Field()

    # 약품이미지URL
    large_medicine_image_url = scrapy.Field()

    # 보험코드
    insurance_cd = scrapy.Field()

    # 품목구분(의약품, 의약외품, 생물의약품, 마약류, 첨단바이오, 한약(생약)제제등
    medicine_kind_cd = scrapy.Field()












    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
