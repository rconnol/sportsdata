# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from web_scrapers.items import espnForecastItem



class EspnForecastSpider(CrawlSpider):
    name = 'espn_forecast'
    allowed_domains = ['games.espn.com']
    start_urls = ['http://games.espn.com/ffl/tools/projections']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='paginationNav']//a")),
                           callback='parse_item',
                           follow=True),
    )

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):

        tr_class = '"pncPlayerRow playerTableBgRow0" or \
                    "pncPlayerRow playerTableBgRow1"'
        
        for row in response.xpath('//tr[@id]'.format(tr_class)):
            #print(row)
            l = ItemLoader(item=espnForecastItem(), selector=row, response=response)
            
            l.add_xpath('rank', './td[1]/text()')
            l.add_xpath('player', './td[2]/a/text()')
            l.add_xpath('team_pos', './td[2]/text()')
            l.add_xpath('comp_att', './td[3]/text()')
            l.add_xpath('pass_yds', './td[4]/text()')
            l.add_xpath('pass_td', './td[5]/text()')
            l.add_xpath('pass_int', './td[6]/text()')
            l.add_xpath('rush_att', './td[7]/text()')
            l.add_xpath('rush_yds', './td[8]/text()')
            l.add_xpath('rush_td', './td[9]/text()')
            l.add_xpath('rec', './td[10]/text()')
            l.add_xpath('rec_yds', './td[11]/text()')
            l.add_xpath('rec_td', './td[12]/text()')

            yield l.load_item()
