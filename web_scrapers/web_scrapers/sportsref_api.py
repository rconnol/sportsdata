import urllib.parse
from enum import Enum


class BasketballReferenceURL(object):

	"""
	BasketballReference API Configuration File

	Use this file to set Basketball Reference URI
	"""

	def __init__(self, url, url_query):

		self.url_base = url

		self.url_query = url_query

		self.url = self.url_base + urllib.parse.urlencode(self.url_query)


nba_playerGame_url = "http://www.basketball-reference.com/" \
                 "play-index/pgl_finder.cgi?"


nba_playerGame_query = {
                   'request' : 1,
                   "player_id" : '',
                   "match" : 'game',
                   "year_min" : 2017,
                   "year_max" : 2017,
                   "age_min" : 0,
                   "age_max" : 99,
                   "team_id" : '',
                   "opp_id" : '',
                   "is_playoffs" : 'N',
                   "round_id" : '',
                   "game_num_type" : '',
                   "game_num_min" : '',
                   "game_num_max" : '',
                   "game_month" : '',
                   "game_day" : '',
                   "game_location" : '',
                   "game_result" : '',
                   "is_starter" : '',
                   "is_active" : '',
                   "is_hof" : '',
                   "pos_is_g" : 'Y',
                   "pos_is_gf" : 'Y',
                   "pos_is_f" : "Y",
                   "pos_is_fg" : "Y",
                   "pos_is_fc" : "Y",
                   "pos_is_c" : "Y",
                   "pos_is_cf" : "Y",
                   "c1stat" : '',
                   "c1comp" : '',
                   "c1val" : '',
                   "c2stat" : '',
                   "c2comp" : '',
                   "c2val" : '',
                   "c3stat" : '',
                   "c3comp" : '',
                   "c3val" : '',
                   "c4stat" : '',
                   "c4comp" : '',
                   "c4val" : '',
                   "is_dbl_dbl" : '',
                   "is_trp_dbl" : '',
                   "order_by" : 'pts',
                   "order_by_asc" : '',
                   "offset" : 0,
                  }


nba_teamGame_url = "http://www.basketball-reference.com/" \
               "play-index/tgl_finder.cgi?"


nba_teamGame_query = {
                  'request' : 1,
                  'match' : 'game',
                  'lg_id' : 'NBA',
                  'is_playoffs' : 'N',
                  'team_seed_cmp' : 'eq',
                  'opp_seed_cmp' : 'eq',
                  'year_min' : 2017,
                  'year_max' : 2017,
                  'is_range' : 'N',
                  'game_num_type' : 'team',
                  'player': '',
                  'team_id' : '',
                  'opp_id' : '',
                  'round_id' : '',
                  'best_of' : '',
                  'team_seed' : '',
                  'opp_seed' : '',
                  'game_num_min' : '',
                  'game_num_max' : '',
                  'game_month' : '',
                  'game_location' : '',
                  'game_result' : '',
                  'is_overtime' : '',
                  'c1stat' : '',
                  'c1comp' : '',
                  'c1val' : '',
                  'c2stat' : '',
                  'c2comp' : '',
                  'c2val' : '',
                  'c3stat' : '',
                  'c3comp' : '',
                  'c3val' : '',
                  'c4stat' : '',
                  'c4comp' : '',
                  'c4val' : '',
                  'order_by' : 'pts',
                  'order_by_asc' : '',
                  'offset' : 0,
                  }


nfl_playerGame_url = "http://www.pro-football-reference.com/" \
                "play-index/pgl-finder.cgi?"


nfl_playerGame_query = {
	              'c5val' : 1,
	              'career_game_num_max' : 400,
	              'career_game_num_min' : 1,
	              'game_num_max' : 99,
	              'game_num_min' : 0,
	              'game_type' : 'R',
	              'match' : 'game',
	              'order_by' : 'pass_td', #'pass_td', 'rush_td', 'rec_td', 'all_td', 'fantasy_points'
	              'pos' : 0, #0 Any, 'QB', 'WR', 'RB', 'TE'
	              'request' : 1,
	              'season_end' : -1,
	              'season_start' : 1,
	              'week_num_max' : 99,
	              'week_num_min' : 0,
	              'year_max' : 2016,
	              'year_min' : 2016,
	              }

nfl_weeklyGame_year = 2016

nfl_weeklyGame_url = "http://www.pro-football-reference.com/years/{}".format(nfl_weeklyGame_year)

class SPORTSREF(Enum):
    NBA_TEAM = [nba_teamGame_url, nba_teamGame_query]
    NBA_PLAYER = [nba_playerGame_url, nba_playerGame_query]
    NFL_PLAYER = [nfl_playerGame_url, nfl_playerGame_query]
