#!/usr/bin/env python

### === GLOBAL STRINGS
watson_found = "image recognized as: {0}, {1}"

### zomato
ZOMATO_SEARCH_URL = "https://developers.zomato.com/api/v2.1/search?apikey={0}&entity_id={1}&radius=10000&{2}"
ZOMATO_LOC_URL = "https://developers.zomato.com/api/v2.1/locations?apikey={0}&query=Toronto"

### yelp
YELP_TOKEN_EXCH = "https://api.yelp.com/oauth2/token"
YELP_SEARCH_URL = "https://api.yelp.com/v3/businesses/search"
