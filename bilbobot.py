#!/bin/python
import config
from flask import Flask
from slackclient import SlackClient

sc = SlackClient(config.slack_token)
app = Flask(__name__)

@app.route('/')
def hi():
    return "hi! i'm bilbo"

@app.route('/test')
def test():
    sc.api_call(
        "chat.postMessage",
        channel="#random",
        text="my name jeff"
    )

    return "200 OK"

@app.route('/post/<input>')
def post(input):
    sc.api_call(
        "chat.postMessage",
        channel="#general",
        text=input
    )

    return "200 OK"


if __name__ == '__main__':
    app.run()
