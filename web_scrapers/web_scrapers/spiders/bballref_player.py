# -*- coding: utf-8 -*-
import scrapy
import web_scrapers.sportsref_api as sr
from web_scrapers.items import NBAPlayerItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader


class BballrefPlayerSpider(CrawlSpider):
    name = 'bballref_player'
    allowed_domains = ['basketball-reference.com']
    start_urls = [sr.BasketballReferenceURL(url=sr.nba_playerGame_url,
                                            url_query=sr.nba_playerGame_query).url]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//a[contains(text(), 'Next')]")),
                           callback='parse_item',
                           follow=True),
    )


    def parse_start_url(self, response):
        return self.parse_item(response)


    def parse_item(self, response):
        
        for row in response.xpath('//tbody//tr[not(@class="thead")]'):
            l = ItemLoader(item=NBAPlayerItem(), selector=row, response=response)

            l.add_xpath('player', './/td[@data-stat="player"]/a/text()')
            l.add_xpath('age', './/td[@data-stat="age"]/text()')
            l.add_xpath('pos', './/td[@data-stat="pos"]/text()')
            l.add_xpath('date_game', './/td[@data-stat="date_game"]/a/text()')
            l.add_xpath('team_id', './/td[@data-stat="team_id"]/a/text()')
            l.add_xpath('game_location', './/td[@data-stat="game_location"]/text()')
            l.add_xpath('opp_id', './/td[@data-stat="opp_id"]/a/text()')
            l.add_xpath('game_result', './/td[@data-stat="game_result"]/text()')
            l.add_xpath('gs', './/td[@data-stat="gs"]/text()')
            l.add_xpath('mp', './/td[@data-stat="mp"]/text()')
            l.add_xpath('fg', './/td[@data-stat="fg"]/text()')
            l.add_xpath('fga', './/td[@data-stat="fga"]/text()')
            l.add_xpath('fg_pct', './/td[@data-stat="fg_pct"]/text()')
            l.add_xpath('fg2', './/td[@data-stat="fg2"]/text()')
            l.add_xpath('fg2a', './/td[@data-stat="fg2a"]/text()')
            l.add_xpath('fg2_pct', './/td[@data-stat="fg2_pct"]/text()')
            l.add_xpath('fg3', './/td[@data-stat="fg3"]/text()')
            l.add_xpath('fg3a', './/td[@data-stat="fg3a"]/text()')
            l.add_xpath('fg3_pct', './/td[@data-stat="fg3_pct"]/text()')
            l.add_xpath('ft', './/td[@data-stat="ft"]/text()')
            l.add_xpath('fta', './/td[@data-stat="fta"]/text()')
            l.add_xpath('ft_pct', './/td[@data-stat="ft_pct"]/text()')
            l.add_xpath('orb', './/td[@data-stat="orb"]/text()')
            l.add_xpath('drb', './/td[@data-stat="drb"]/text()')
            l.add_xpath('trb', './/td[@data-stat="trb"]/text()')
            l.add_xpath('ast', './/td[@data-stat="ast"]/text()')
            l.add_xpath('stl', './/td[@data-stat="stl"]/text()')
            l.add_xpath('blk', './/td[@data-stat="blk"]/text()')
            l.add_xpath('tov', './/td[@data-stat="tov"]/text()')
            l.add_xpath('pf', './/td[@data-stat="pf"]/text()')
            l.add_xpath('pts', './/td[@data-stat="pts"]/text()')
            l.add_xpath('game_score', './/td[@data-stat="game_score"]/text()')

            yield l.load_item()
