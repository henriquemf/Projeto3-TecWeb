import scrapy

class gameScrapSpider(scrapy.Spider):
    name = "gamescrap_spider"
    start_urls = ['https://www.promobit.com.br/promocoes/jogos-de-pc/s/']

    def parse(self, response):
        SET_SELECTOR = '.css-wauoyl'
        for game in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.css-10227v0 ::text'
            OLDPRICE_SELECTOR = '.css-124gmjl ::text'
            NEWPRICE_SELECTOR = '.css-1u0404w ::text'
            yield {
                'name': game.css(NAME_SELECTOR).extract_first(),
                'price': game.css(OLDPRICE_SELECTOR).extract_first(),
                'discounted price': game.css(NEWPRICE_SELECTOR).extract_first(),
            }
