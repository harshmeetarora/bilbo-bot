#!/bin/python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hi():
    return "hi! i'm bilbo"


if __name__ == '__main__':
    app.run()
