"""
Simple flask api
"""
import flask
import os
import subprocess
from scrapeMelon import getList

app = flask.Flask(__name__)
ClientId = os.environ['ClientId']

@app.route('/', methods=['GET'])
def spalsh():
    return flask.render_template('index.html')

@app.route('/chart/<string:key>', methods=['GET'])
def chart(key):
    return getList(key.upper())

@app.route('/spotify', methods=['GET'])
def getOauth():
    return flask.redirect('https://accounts.spotify.com/authorize?client_id=' + ClientId + '&response_type=code&redirect_uri=http://127.0.0.1:5000/spotify/playlist&scope=playlist-modify-public')  

@app.route('/spotify/playlist', methods=['GET'])
def makePlaylist():
    userInfo = subprocess.run(['curl', '-H', "Authorization: Bearer " + flask.request.args.get('code'),'https://api.spotify.com/v1/me'], stdout=subprocess.PIPE)
    return str(userInfo)

# Needs to be on the bottom 
if __name__ == '__main__':
    app.run(threaded=True, debug=True)