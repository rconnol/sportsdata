# -*- coding: utf-8 -*-
import scrapy
import web_scrapers.sportsref_api as sr
from web_scrapers.items import NBATeamItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class BasketrefTeamSpider(CrawlSpider):
    name = "bballref_team"
    allowed_domains = ["basketball-reference.com"]
    start_urls = [sr.BasketballReferenceURL(url=sr.nba_teamGame_url,
                                            url_query=sr.nba_teamGame_query).url]
    rules = (

    	Rule(LinkExtractor(restrict_xpaths=("//a[contains(text(), 'Next')]")),
             callback='parse_item',
             follow=True),
    	)


    def parse_start_url(self, response):
        return self.parse_item(response)


    def parse_item(self, response):

        for row in response.xpath('//tbody//tr[not(@class="thead")]'):
            l = ItemLoader(item=NBATeamItem(), selector=row, response=response)

            l.add_xpath('date_game', './/td[@data-stat="date_game"]/a/text()')
            l.add_xpath('team_id', './/td[@data-stat="team_id"]/a/text()')
            l.add_xpath('game_location', './/td[@data-stat="game_location"]/text()')
            l.add_xpath('opp_id', './/td[@data-stat="opp_id"]/a/text()')
            l.add_xpath('game_result', './/td[@data-stat="game_result"]/text()')
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
            l.add_xpath('pts', './/td[@data-stat="pts"]/text()')
            l.add_xpath('opp_fg', './/td[@data-stat="opp_fg"]/text()')
            l.add_xpath('opp_fga', './/td[@data-stat="opp_fga"]/text()')
            l.add_xpath('opp_fg_pct', './/td[@data-stat="opp_fg_pct"]/text()')
            l.add_xpath('opp_fg2', './/td[@data-stat="opp_fg2"]/text()')
            l.add_xpath('opp_fg2a', './/td[@data-stat="opp_fg2a"]/text()')
            l.add_xpath('opp_fg2_pct', './/td[@data-stat="opp_fg2_pct"]/text()')
            l.add_xpath('opp_fg3', './/td[@data-stat="opp_fg3"]/text()')
            l.add_xpath('opp_fg3a', './/td[@data-stat="opp_fg3a"]/text()')
            l.add_xpath('opp_fg3_pct', './/td[@data-stat="opp_fg3_pct"]/text()')
            l.add_xpath('opp_ft', './/td[@data-stat="opp_ft"]/text()')
            l.add_xpath('opp_fta', './/td[@data-stat="opp_fta"]/text()')
            l.add_xpath('opp_ft_pct', './/td[@data-stat="opp_ft_pct"]/text()')
            l.add_xpath('opp_pts', './/td[@data-stat="pts"]/text()')

            yield l.load_item()
