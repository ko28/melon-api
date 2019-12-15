"""
Simple flask api 
"""
import flask
from scrapeMelon import getList

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def spalsh  ():
    return "<h1> Melon API </h1>"

@app.route('/chart/<string:key>', methods=['GET'])
def chart(key):
    return getList(key.upper())

app.run()