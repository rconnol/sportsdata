# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class NBATeamItem(scrapy.Item):
    # define the fields for your item here like:
    name = Field()
    date_game = Field()
    team_id = Field()
    game_location = Field()
    opp_id = Field()
    game_result = Field()
    mp = Field()
    fg = Field()
    fga = Field()
    fg_pct = Field()
    fg2 = Field()
    fg2a = Field()
    fg2_pct = Field()
    fg3 = Field()
    fg3a = Field()
    fg3_pct = Field()
    ft = Field()
    fta = Field()
    ft_pct = Field()
    pts = Field()
    opp_fg = Field()
    opp_fga = Field()
    opp_fg_pct = Field()
    opp_fg2 = Field()
    opp_fg2a = Field()
    opp_fg2_pct = Field()
    opp_fg3 = Field()
    opp_fg3a = Field()
    opp_fg3_pct = Field()
    opp_ft = Field()
    opp_fta = Field()
    opp_ft_pct = Field()
    opp_pts = Field()


class NBAPlayerItem(scrapy.Item):
	player = Field()
	age = Field()
	pos = Field()
	date_game = Field()
	team_id = Field()
	game_location = Field()
	opp_id = Field()
	game_result = Field()
	gs = Field()
	mp = Field()
	fg = Field()
	fga = Field()
	fg_pct = Field()
	fg2 = Field()
	fg2a = Field()
	fg2_pct = Field()
	fg3 = Field()
	fg3_pct = Field()
	fg3a = Field()
	fg3_pct = Field()
	ft = Field()
	fta = Field()
	ft_pct = Field()
	orb = Field()
	drb = Field()
	trb = Field()
	trb = Field()
	ast = Field()
	stl = Field()
	blk = Field()
	tov = Field()
	pf = Field()
	pts = Field()
	game_score = Field()

class NBAGameItem(scrapy.Item):
	home_team = Field()
	away_team = Field()
	game_date = Field()
	game_time = Field()

	home_pg = Field()
	home_sg = Field()
	home_sf = Field()
	home_pf = Field()
	home_c = Field()

	away_pg = Field()
	away_sg = Field()
	away_sf = Field()
	away_pf = Field()
	away_c = Field()

	home_injuries = Field()
	away_injuries = Field()

class NFLPlayerGame(scrapy.Item):
	year = Field()
	week = Field()

	player = Field()
	team = Field()
	opp = Field()

	pass_comp = Field()
	pass_att = Field()
	pass_yds = Field()
	pass_td = Field()
	pass_int = Field()
	sacked = Field()
	sack_yds_lost = Field()

	rush_att = Field()
	rush_yds = Field()
	rush_td = Field()

	rec_tgts = Field()
	rec_rec = Field()
	rec_yds = Field()
	rec_td = Field()

	fumbles = Field()
	fumbles_lost = Field()

class espnForecastItem(scrapy.Item):

	rank = Field()
	player = Field()
	team_pos = Field()
	comp_att = Field()
	pass_yds = Field()
	pass_td = Field()
	pass_int = Field()
	rush_att = Field()
	rush_yds = Field()
	rush_td = Field()
	rec = Field()
	rec_yds = Field()
	rec_td = Field()