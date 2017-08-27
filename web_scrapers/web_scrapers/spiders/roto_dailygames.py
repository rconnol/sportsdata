# -*- coding: utf-8 -*-
import scrapy
from web_scrapers.items import NBAGameItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader

class RotoDailygamesSpider(CrawlSpider):
    name = 'roto_dailygames'
    allowed_domains = ['rotowire.com']
    start_urls = ['http://www.rotowire.com/basketball/nba_lineups.htm',
                  'http://www.rotowire.com/basketball/nba_lineups.htm?date=tomorrow']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        return self.parse_item(response)

    
    def parse_item(self, response):

        home_teams = response.xpath('//div[@class="span5 dlineups-topboxright"]/text()').extract()
        away_teams = response.xpath('//div[@class="span5 dlineups-topboxleft"]/text()').extract()
        game_times = response.xpath('//div[@class="dlineups-topboxcenter-topline"]//a/text()').extract()

        #strip away the whitespace from the response
        home_teams = [team.strip() for team in home_teams if team.strip() != '']
        away_teams = [team.strip() for team in away_teams if team.strip() != '']

        for num, game in enumerate(response.xpath('//div[@class="offset1 span15"]')):
            l = ItemLoader(item=NBAGameItem(), selector=game, response=response)
            
            l.add_value('home_team', home_teams[num])
            l.add_value('away_team', away_teams[num])
            l.add_value('game_time', game_times[num])

            date_extractor = response.xpath('//h1[@class="titletext-smallest"]/text()').extract()
            l.add_value('game_date', date_extractor[0].replace('\xa0', ' ')[22:])

            home_player_extractor = game.xpath('.//div[@class="dlineups-hplayer"]//a/text()').extract()
            away_player_extractor = game.xpath('.//div[@class="dlineups-vplayer"]//a/text()').extract()
            home_status_extractor = game.xpath('.//div[@class="dlineups-hplayer"]//b/text()').extract()
            away_status_extractor = game.xpath('.//div[@class="dlineups-hplayer"]//b/text()').extract()

            l.add_value('home_pg', home_player_extractor[0])
            l.add_value('home_sg', home_player_extractor[1])
            l.add_value('home_sf', home_player_extractor[2])
            l.add_value('home_pf', home_player_extractor[3])
            l.add_value('home_c', home_player_extractor[4])

            l.add_value('away_pg', away_player_extractor[0])
            l.add_value('away_sg', away_player_extractor[1])
            l.add_value('away_sf', away_player_extractor[2])
            l.add_value('away_pf', away_player_extractor[3])
            l.add_value('away_c', away_player_extractor[4])

            l.add_value('home_injuries', zip(home_player_extractor[5:], home_status_extractor))
            l.add_value('away_injuries', zip(away_player_extractor[5:], away_status_extractor))

            yield l.load_item()
