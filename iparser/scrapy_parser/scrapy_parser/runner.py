from scrapy_parser.scrapy_parser import settings
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from scrapy_parser.scrapy_parser.spiders.instagram import InstagramSpider


def start_parsing(user_to_scrape: str) -> None:

    if user_to_scrape:
        crawler_settings = Settings()
        crawler_settings.setmodule(settings)

        process = CrawlerProcess(settings=crawler_settings)
        process.crawl(InstagramSpider, user_to_scrape=user_to_scrape)

        process.start()
