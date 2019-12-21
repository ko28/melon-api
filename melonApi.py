"""
Simple flask api
"""
import flask
import os
import requests
from scrapeMelon import getList
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
def getOauth():
    # Go to spotify authorization page to get authorization code, exchanged for an access token
    return flask.redirect('https://accounts.spotify.com/authorize?client_id=' + ClientId + 
    '&response_type=code&redirect_uri=' + flask.request.host_url + 'spotify/playlist&scope=playlist-modify-public')  

@app.route('/spotify/playlist', methods=['GET'])
def makePlaylist():    
    
    # Generate access token   
    params = {
                "grant_type":    "authorization_code",
                "client_id" :    ClientId,
                "client_secret": ClientSecret,
                "code":          flask.request.args.get('code'),
                "redirect_uri":  flask.request.host_url + 'spotify/playlist'
            }
            # "redirect_uri": flask.request.host_url + 'spotify/playlist'
    token = requests.post(url='https://accounts.spotify.com/api/token', data=params).json()['access_token']
    

    # Get user's id =body, auth=(ClientId, ClientSecret)
    headers = {
        "Authorization" : "Bearer " + token,
        "Content-Type" : "application/json"
    }
    userId = requests.get(url='https://api.spotify.com/v1/me', headers=headers).json()['id']

    # Make a new playlist
    params = {
            "name" : "Melon Top 100",
            "public": "true",
            "description" : "Made by github.com/ko28 and generated on " + str(datetime.now())
    }
    playlist = requests.post(url='https://api.spotify.com/v1/users/' + userId + '/playlists', headers=headers, data=params)
    return 'https://api.spotify.com/v1/users/' + userId + '/playlists'
'''
    except:
        return "Could not get token, try clearing your cookies and logging again."
        '''
   
# Needs to be on the bottom 
if __name__ == '__main__':
    app.run(threaded=True, debug=True)
    