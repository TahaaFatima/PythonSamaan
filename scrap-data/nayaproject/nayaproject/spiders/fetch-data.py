import scrapy
from datetime import datetime

class QuotesUrls(scrapy.Spider):
    name       = "quotes"
    """ start_urls = ["http://geeksforgeeks.org",] """
    start_urls = ["https://www.forex.pk/open_market_rates.asp",]

    def parse(self, response):
        filename  = 'current-currency-rate.txt'
        today     = datetime.now()
        data_path = "//table/tr/td/table/tr[3]/td/div/div[2]/table/tr/td[2]/table[2]/tr[contains(., '%s')]/td[3]/text()"
        curr_dict = {'USD' : data_path % 'USD',
                    'AED' : data_path % 'AED',
                    'BHD' : data_path % 'BHD',
                    'EUR' : data_path % 'EUR',
                    'THB' : data_path % 'THB'
                    }
        with open(filename, 'w') as f:
            f.write(f'''
                        {today}''')
            for i in curr_dict:
                result = response.xpath(curr_dict[i]).getall()
                f.write(f'''
                            {i} to PKR is {result[0]}''')