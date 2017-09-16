#!/bin/python
import config
from flask import Flask
from slackclient import SlackClient
from watson-developer-cloud import VisualRecognitionV3

sc = SlackClient(config.slack_token)
app = Flask(__name__)

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

@app.route('/custom/<input>', methods=['GET'])
def custom(input):
    sc.api_call(
        "chat.postMessage",
        channel="#general",
        text=input
    )

    return "200 OK"


if __name__ == '__main__':
    app.run()
