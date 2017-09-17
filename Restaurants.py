import config, strings
import json, requests
import urllib

def buildRestaurant(r_name,r_address,r_avgCost,r_rating):
    restaurant_str = "Name: {} \n".format(r_name)
    restaurant_str += "Address: {} \n".format(r_address)
    restaurant_str += "Average price for two: {} \n".format(r_avgCost)
    restaurant_str += "Rating: {} \n".format(r_rating)

    print(restaurant_str)
    return restaurant_str


def findLocation():
    apiUrl = (strings.ZOMATO_LOC_URL).format(config.zomato_api_key)
    json_data = requests.get(apiUrl).json()
    print(json.dumps(json_data))

    return json_data['location_suggestions'][0]['entity_id']


def searchRestaurantsWith(keyword):
    """ (String) -> list of strings 
        Given a keyword, finds the restaurants that
        are related to keyword.
    """
    # construct proper URL
    entity_id = findLocation()
    apiUrl = (strings.ZOMATO_SEARCH_URL).format(config.zomato_api_key, entity_id, urllib.urlencode({'q':keyword}))
    print(apiUrl)

    # call zomato api
    json_data = requests.get(apiUrl).json()
    print(json.dumps(json_data))

    # add each restaurant name to the list of restaurants
    restaurants = []
    size = json_data['results_found']
    for i in range(size):
        r_name = json_data['restaurants'][i]['restaurant']['name']
        r_address = json_data['restaurants'][i]['restaurant']['location']['address']
        r_avgCost = json_data['restaurants'][i]['restaurant']['average_cost_for_two']
        r_rating = str(json_data['restaurants'][i]['restaurant']['user_rating']['aggregate_rating'])
        # create new restaurant object
        restaurants[i] = buildRestaurant(r_name,r_address,r_avgCost,r_rating)
        
    return restaurants
            