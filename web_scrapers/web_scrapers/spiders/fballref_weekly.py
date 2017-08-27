# -*- coding: utf-8 -*-
import scrapy
import web_scrapers.sportsref_api as sr
from web_scrapers.items import NFLPlayerGame
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy_splash import SplashRequest


class FballrefWeeklySpider(Spider):

    name = 'fballref_weekly'
    allowed_domains = ['www.pro-football-reference.com']
    start_urls = [sr.nfl_weeklyGame_url + 
                  '/week_{}.htm'.format(str(x)) for x in range(1,22)]

    # rules = (

    #     Rule(LinkExtractor(restrict_xpaths=("//a[contains(text(), 'Final')]")),
    #          callback='parse_player_item',
    #          #process_request='use_splash',
    #          follow=True),

    # )

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,
                                self.parse_start_url,
                                endpoint='render.html',
                                args={'wait':0.5})
               


    def parse_start_url(self, response):

        link_extractor = LinkExtractor(restrict_xpaths="//a[contains(text(), 'Final')]")
        links = link_extractor.extract_links(response)

        for link in links:

            yield SplashRequest(link.url,
                                self.parse_player_item,
                                endpoint='render.html',
                                args={'wait':0.5})

    
    def parse_player_item(self, response):

        for row in response.xpath('//table[@id="player_offense"]/tbody//tr[@data-row and not(@class)]'):
            l = ItemLoader(item=NFLPlayerGame(), selector=row, response=response)

            l.add_value('year', sr.nfl_weeklyGame_year)
            l.add_xpath('week', '//div[@id="div_other_scores"]/div/h2/a/text()')
            l.add_xpath('player', './/th[@data-stat="player"]/a/text()')
            l.add_xpath('team', './/td[@data-stat="team"]/text()')
            l.add_xpath('pass_comp', './/td[@data-stat="pass_cmp"]/text()')
            l.add_xpath('pass_att', './/td[@data-stat="pass_att"]/text()')
            l.add_xpath('pass_yds', './/td[@data-stat="pass_yds"]/text()')
            l.add_xpath('pass_td', './/td[@data-stat="pass_td"]/text()')
            l.add_xpath('sacked', './/td[@data-stat="pass_sacked"]/text()')
            l.add_xpath('sack_yds_lost', './/td[@data-stat="pass_sacked_yds"]/text()')
            l.add_xpath('rush_att', './/td[@data-stat="rush_att"]/text()')
            l.add_xpath('rush_yds', './/td[@data-stat="rush_yds"]/text()')
            l.add_xpath('rush_td', './/td[@data-stat="rush_td"]/text()')
            l.add_xpath('rec_tgts', './/td[@data-stat="targets"]/text()')
            l.add_xpath('rec_rec', './/td[@data-stat="rec"]/text()')
            l.add_xpath('rec_td', './/td[@data-stat="rec_td"]/text()')
            l.add_xpath('fumbles', './/td[@data-stat="fumbles"]/text()')
            l.add_xpath('fumbles_lost', './/td[@data-stat="fumbles_lost"]/text()')

            yield l.load_item()