#!/usr/bin/env python

### === GLOBAL STRINGS
watson_looking = "Your search: {}"
watson_found = "DOOFieBot recognized as: {0}, {1}"
_200_OK = "Enjoy your day! :revolving_hearts:"

### zomato
ZOMATO_SEARCH_URL = "https://developers.zomato.com/api/v2.1/search?apikey={0}&entity_id={1}&radius=10000&{2}"
ZOMATO_LOC_URL = "https://developers.zomato.com/api/v2.1/locations?apikey={0}&query=Toronto"

### yelp
YELP_TOKEN_EXCH = "https://api.yelp.com/oauth2/token"
YELP_SEARCH_URL = "https://api.yelp.com/v3/businesses/search"

### UX
recommended = ":heart_eyes: *DOOFieBot* recommends *{0}*! Located *{1:.2f}km* away at _{2}_, " \
            "{3}/5 people approve of this location. {4}"
