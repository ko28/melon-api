"""
Simple flask api
"""
import flask
import os
import requests
import json
from . import spotify
from .scrapeMelon import getList
from datetime import datetime

app = flask.Flask(__name__)
ClientId = os.environ['ClientId']
ClientSecret = os.environ['ClientSecret']

@app.route('/', methods=['GET'])
def spalsh():
    return flask.render_template('index.html')

@app.route('/chart/<string:key>', methods=['GET'])
def chart(key):
    return getList(key.upper())

@app.route('/spotify', methods=['GET'])
def getOAuthCode():
    # Go to Spotify's authorization page to get authorization code
    return flask.redirect('https://accounts.spotify.com/authorize?client_id=' + ClientId + 
    '&response_type=code&redirect_uri=' + flask.request.host_url + 'spotify/playlist&scope=playlist-modify-public')  

@app.route('/spotify/playlist', methods=['GET'])
def makePlaylist():  
    liveChart = getList("LIVE")  
    token = spotify.token(flask.request.args.get('code'), flask.request.host_url + 'spotify/playlist', ClientId, ClientSecret)    
    playlist = spotify.makePlaylist(token)
    return spotify.convertChartToPlaylist(liveChart, playlist['id'], token)


'''
    except:
        return "Could not get token, try clearing your cookies and logging again."
        '''
   
# Needs to be on the bottom 
if __name__ == '__main__':
    app.run(threaded=True, debug=True)
    