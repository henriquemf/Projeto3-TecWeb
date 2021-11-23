import scrapy
from scrapy.crawler import CrawlerProcess
import re

class gameScrapSpider(scrapy.Spider):
    name = "gamescrap_spider"
    start_urls = ['https://www.promobit.com.br/promocoes/jogos-de-pc/s/']

    def parse(self, response):
        SET_SELECTOR = '.css-wauoyl'
        for game in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.css-10227v0 ::text'
            OLDPRICE_SELECTOR = '.css-124gmjl ::text'
            NEWPRICE_SELECTOR = '.css-1u0404w ::text'
            STORE_SELECTOR = '.css-1a7v2lf ::text'
            yield {
                'name': game.css(NAME_SELECTOR).extract(),
                'store': game.css(STORE_SELECTOR).extract(),
                'price': game.css(OLDPRICE_SELECTOR).extract(),
                'discounted price': game.css(NEWPRICE_SELECTOR).extract(),
            }

def run_spider():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "items.json": {"format": "json", "overwrite": True},
            #"items.jl": {"format": "jsonlines"},
        },
    })
    process.crawl(gameScrapSpider)
    process.start()