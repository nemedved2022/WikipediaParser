BOT_NAME = "wiki"

SPIDER_MODULES = ["wiki.spiders"]
NEWSPIDER_MODULE = "wiki.spiders"

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 32

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
