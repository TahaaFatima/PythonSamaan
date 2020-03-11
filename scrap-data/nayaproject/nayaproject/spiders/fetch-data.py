import scrapy

class QuotesUrls(scrapy.Spider):
    name       = "quotes"
    """ start_urls = ["http://geeksforgeeks.org",] """
    start_urls = ["https://www.forex.pk/open_market_rates.asp",]

    def parse(self,response):
        td_text = response.css('table>tr>td::text').extract()
        # links = response.css('h2.entry-title a::text').extract()

        for td_val in td_text:
            # yield {'title' : title, 'links_title' : links}
            yield {'kuchbhee' : td_val}