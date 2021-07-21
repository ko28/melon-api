"""
Simple flask api
"""
import flask
import os
import requests
import json
from . import spotify
from .scrapeMelon import getList
from .scrapeMelon import getLyric
from datetime import datetime

app = flask.Flask(__name__)

default_headers = {'Content-Type': 'text/json'}

#Settings for playlist
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

@app.route('/', methods=['GET'])
def spalsh():
    return flask.render_template('index.html')

@app.route('/api/v1/chart/<string:key>', methods=['GET'])
def chart(key):
    return getList(key.upper()), 200, default_headers

@app.route('/api/v1/lyric/<int:key>', methods=['GET'])
def lyric(key):
    return getLyric(key), 200, default_headers

@app.route('/api/v1/spotify', methods=['GET'])
def getOAuthCode():
    spotifyRequirement()
    # Go to Spotify's authorization page to get authorization code
    return flask.redirect('https://accounts.spotify.com/authorize?client_id=' + client_id + 
    '&response_type=code&redirect_uri=' + flask.request.host_url + 'api/v1/spotify/playlist&scope=playlist-modify-public')  
 
@app.route('/api/v1/spotify/playlist', methods=['GET'])
def makePlaylist():  
    spotifyRequirement()
    liveChart = getList("LIVE")  
    token = spotify.token(flask.request.args.get('code'), flask.request.host_url + 'spotify/playlist', client_id, client_secret)    
    playlist = spotify.makePlaylist(token)
    return "https://open.spotify.com/playlist/"+spotify.convertChartToPlaylist(liveChart, playlist['id'], token)

def spotifyRequirement():
    if (client_id or client_secret) is None:
        flask.abort()
   
# Needs to be on the bottom 
if __name__ == '__main__':
    app.run(threaded=True, debug=True)
    