#!/bin/python
import config, json, strings
from flask import Flask, request, current_app
from slackclient import SlackClient
from watson_developer_cloud import VisualRecognitionV3
from restaurants import *
from restaurants_yelp import *

'''
MAIN BILBOBOT
'''

sc = SlackClient(config.slack_token)
vr = VisualRecognitionV3('2017-09-16',api_key=config.watson_api_key)
app = Flask(__name__)

### === WATSON INTEGRATION ===

@app.route('/doof', methods=['POST'])
def watsonify():
    # process image recognition
    imgurl = request.form["text"]
    sc.api_call("chat.postMessage",
                channel="#general",
                text=(strings.watson_looking).format(imgurl))
    res_body = vr.classify(images_url=imgurl)

    print(json.dumps(res_body,indent=2))

    # find the top 2 recognized keywords
    img_recogs = (res_body["images"][0]["classifiers"][0]["classes"])
    first = img_recogs[0]
    second = img_recogs[1]
    for img in img_recogs:
        if img["score"] > first["score"]:
            second = first
            first = img
    top_two = [first['class'],second['class']]
    
    sc.api_call(
        "chat.postMessage",
        channel="#general",
        text=(strings.watson_found).format(top_two[0],top_two[1]))

    output = processTopTwo(top_two)
    sc.api_call("chat.postMessage",
                channel="#general",
                text=output)

    return "200 OK"


### === YELP / ZOMATO INTEGRATION ===

# takes a keyword and generates the results off of Yelp for top locations
# uses the result of this calculation to return information to the web app
@app.route('/results', methods=['GET'])
def handleSearchKeyword():
    keyword = request.args.get('keyword')
    restaurant_list = searchRestaurantsWith(51.5033640,-0.1276250,5000,keyword)
    json.dumps(restaurant_list,indent=2,separators=(',',':'))

    return current_app.send_static_file('results.html')

# given location JSON, parse into string
def parseAddress(loc):
    return "{0}, {1} {2}".format(loc["address1"],loc["city"],loc["state"])

# method to process the top 2 results
def processTopTwo(topTwo):
    # search with the keyword
    keyword = topTwo[0]
    restaurant_list = searchRestaurantsWith(51.5033640,-0.1276250,5000,keyword)

    # check if enough results
    if (len(restaurant_list['businesses']) < 5):
        keyword = topTwo[1]
        restaurant_list = searchRestaurantsWith(51.5033640,-0.1276250,5000,keyword)

    for i in range(0,5):
        name = restaurant_list['businesses'][i]['name']
        address = parseAddress(restaurant_list['businesses'][i]['location'])
        rating = restaurant_list['businesses'][i]['rating']
        distance = restaurant_list['businesses'][i]['distance'] # THIS IS IN METRES
        url = restaurant_list['businesses'][i]['url']
        # Adding formatted results to an array of strings
        recommendation = (strings.recommended).format(name, distance/1000, address, rating%5, url)
        sc.api_call("chat.postMessage",
                    channel="#general",
                    text=recommendation)

    output = "Go to http://54.186.16.182/results?keyword={} for more!".format(keyword)

    # send msg to general channel
    sc.api_call("chat.postMessage",
                channel="#general",
                text=output)

    return strings._200_OK
     
     

### === MAIN API ENDPOINTS ===

@app.route('/')
def hi():
    return "hi! i'm bilbo"

@app.route('/test', methods=['GET'])
def test():
    sc.api_call(
        "chat.postMessage",
        channel="#random",
        text="my name jeff"
    )

    return "200 OK"

@app.route('/custom/<input>')
def custom(input):
    sc.api_call(
        "chat.postMessage",
        channel="#general",
        text=input
    )

    return "200 OK"


if __name__ == '__main__':
    app.run()
    