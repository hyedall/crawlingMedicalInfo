# Scrapy settings for medicine project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'medicine'

SPIDER_MODULES = ['medicine.spiders']
NEWSPIDER_MODULE = 'medicine.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False



# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2

# 쿠키 사용
COOKIES_ENABLED = True

DEFAULT_REQUEST_HEADERS = {
  'Referer': 'https://nedrug.mfds.go.kr'
}

# fake-useragent middleware 사용
DOWNLOADER_MIDDLEWARES = {
  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
  'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}

# 츌력 인코딩
FEED_EXPORT_ENCODING = 'utf-8'
