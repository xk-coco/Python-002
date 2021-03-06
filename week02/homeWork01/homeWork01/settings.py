# Scrapy settings for homeWork01 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import requests
import json

BOT_NAME = 'homeWork01'

SPIDER_MODULES = ['homeWork01.spiders']
NEWSPIDER_MODULE = 'homeWork01.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'homeWork01 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Connection': 'keep-alive',
    'Referer': 'https://maoyan.com/films?showType=3',
    'Cookie': '''BIDUPSID=D0AABE14DE25E3141A5A1809482609C1; PSTM=1596385390; BAIDUID=D0AABE14DE25E314BA39EB14468BB67A:FG=1; H_PS_PSSID=32294_1443_31669_32379_32362_32327_31254_32046_32395_32429_32115_31708_31639; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; HMACCOUNT=9FA221F42F651DBF; delPer=0; PSINO=6; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1596462499|'''
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'homeWork01.middlewares.Homework01SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'homeWork01.middlewares.Homework01DownloaderMiddleware': 543,
    'homeWork01.middlewares.RandomHttpProxyMiddleware': 400
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'homeWork01.pipelines.Homework01Pipeline': 300,
}

DB_INFO = {
    'host': '192.168.102.160',
    'port': 3306,
    'user': 'root',
    'password': '******',
    'db': 'pythontest',
    'charset': 'utf8mb4'
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTP_PROXY_LIST = ['http://101.37.118.54:8888', 'http://101.4.136.34:81', 'http://102.129.249.120:3128',
                   'http://102.129.249.120:8080', 'http://103.105.49.53:80', 'http://103.216.51.210:8191',
                   'http://103.235.46.121:80', 'http://103.235.46.154:80', 'http://103.28.37.131:3128',
                   'http://104.129.192.100:10605', 'http://104.129.192.101:10605', 'http://104.129.192.106:10605',
                   'http://104.129.192.179:10605', 'http://104.129.192.49:10605', 'http://104.129.192.56:10605']
