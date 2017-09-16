import json
import urllib
import requests
from Restaurant import Restaurant

# from urllib2 import Request, urlopen, URLError

class Restaurants:
	""" Attribute of list of restaurants, initially empty """ 
	restaurants = []
	ZOMATO_SEARCH_API_URL = "https://developers.zomato.com/api/v2.1/search?apikey=5ea93656e886f5bc6a60ada64221cd92&radius=5000&"
	
	def searchRestaurantsWith(self, keyword):
		""" (String) -> list of strings 
			Given a keyword, finds the restaurants that
			are related to keyword.
		"""
		# construct proper URL
		apiUrl = self.ZOMATO_SEARCH_API_URL + urllib.parse.urlencode({'q':keyword})
		print(apiUrl)
		# call zomato api
		json_data = requests.get(apiUrl).json()
		print(json_data)
		# add each restaurant name to the list of restaurants
		size = json_data['results_found']
		print(size)
		for i in range(size):
			r_name = json_data['restaurants'][i]['restaurant']['name']
			r_address = json_data['restaurants'][i]['restaurant']['location']['address']
			r_avgCost = json_data['restaurants'][i]['restaurant']['average_cost_for_two']
			r_rating = str(json_data['restaurants'][i]['restaurant']['user_rating']['aggregate_rating'])
			# create new restaurant object
			restaurant = Restaurant(r_name, r_address, r_avgCost, r_rating)
			self.restaurants.append(restaurant)
	
	def showResults(self):
		for r in self.restaurants:
			r.printInfo()
			