import config, strings
import json, requests

def get_oauth2_token():
    head = {'Content-Type': 'application/x-www-form-urlencoded'}

    # build POST request body
    req_body = {'grant_type': 'client_credentials',
                'client_id': config.yelp_client,
                'client_secret': config.yelp_secret}
    r = requests.post(strings.YELP_TOKEN_EXCH, headers=head, data=req_body, verify=True)
    
    return 'Bearer ' + r.json()['access_token']


def searchRestaurantsWith(latitude,longitude,radius,keyword):
	head = {'Content-Type': 'application/json',
			'Authorization': get_oauth2_token()}

	# build search query parameters
	qp = {'latitude': latitude,
		  'longitude': longitude,
		  'radius': radius,
		  'term': keyword}

	r = requests.get(strings.YELP_SEARCH_URL, headers=head, params=qp, verify=True)

	#json.dumps(r.json(),indent=2,separators=(',',':'))
	return r.json()

