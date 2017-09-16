#!/bin/python
import config, json, strings
from flask import Flask, request
from slackclient import SlackClient
from watson_developer_cloud import VisualRecognitionV3

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
    res_body = json.dumps(vr.classify(images_url=imgurl), indent=2)
    print(res_body)

    # find the top 2 recognized keywords

    sc.api_call(
        "chat.postMessage",
        channel="#general",
        text=strings.watson_found)

    return "200 OK"


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
