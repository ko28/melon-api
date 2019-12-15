"""
Simple flask api 
"""
import flask
from scrapeMelon import getList

app = flask.Flask(__name__)
app.config["DEBUG"] = True

if __name__ == '__main__':
    app.run(threaded=True)

@app.route('/', methods=['GET'])
def spalsh():
    return "<h1> Melon API </h1> <p>Try calling /chart/(live, rise, day, week, month)</p>"

@app.route('/chart/<string:key>', methods=['GET'])
def chart(key):
    return getList(key.upper())

