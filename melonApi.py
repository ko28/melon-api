"""
Simple flask api 
"""
import logging
from flask import Flask, jsonify
from scrapeMelon import getList

app = Flask(__name__)

if __name__ == '__main__':
    app.run(threaded=True, debug=True)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.route('/', methods=['GET'])
def spalsh():
    return "<h1> Melon API </h1> <p>Try calling /chart/(live, rise, day, week, month)</p>"

@app.route('/chart/<string:key>', methods=['GET'])
def chart(key):
    return getList(key.upper())

