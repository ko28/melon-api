"""
Simple flask api
"""
import flask
import os
import requests
import json
from datetime import datetime
from flask import request
from re import match
from werkzeug.routing import BaseConverter
from .spotify import token as createToken
from .spotify import makePlaylist
from .spotify import convertChartToPlaylist
from .scrapeMelon import getList
from .scrapeMelon import getLyric
from .scrapeMelon import yearChart

app = flask.Flask(__name__)

default_headers = {'Content-Type': 'text/json'}

# Settings for playlist
client_id = os.environ['client_id']
client_secret = os.environ['client_secret']


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route('/', methods=['GET'])
def spalsh():
    return flask.render_template('index.html')


@app.route('/chart/<string:key>', methods=['GET'])
def chart(key):
    return getList(key.upper()), 200, default_headers


@app.route('/chart/year/<regex("(2[0-9]{3}|19[0-9]{2})"):year>', methods=['GET'])
def listAge(year):
    if int(year) < 1964 or int(year) >= datetime.now().year:
        return {"message": "invalid year"}, 400, default_headers

    overseas = request.args.get('overseas')

    return {"result": yearChart(year, overseas != None)}, 200, default_headers


@app.route('/lyric/<string:key>', methods=['GET'])
def lyric(key):
    return getLyric(key), 200, default_headers


@app.route('/spotify', methods=['GET'])
def getOAuthCode():
    # Go to Spotify's authorization page to get authorization code
    return flask.redirect('https://accounts.spotify.com/authorize?client_id=' + client_id +
                          '&response_type=code&redirect_uri=' + flask.request.host_url + 'spotify/playlist&scope=playlist-modify-public')


@app.route('/spotify/playlist', methods=['GET'])
def makePlaylist():
    liveChart = getList("LIVE")
    token = createToken(flask.request.args.get(
        'code'), flask.request.host_url + 'spotify/playlist', client_id, client_secret)
    playlist = makePlaylist(token)
    return "https://open.spotify.com/playlist/"+convertChartToPlaylist(liveChart, playlist['id'], token)


# Needs to be on the bottom
if __name__ == '__main__':
    app.run(threaded=True, debug=True)
