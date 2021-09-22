"""
Simple wrapper for Spotify API 
"""
import requests
import json
import time
from datetime import datetime


def token(code, redirect_uri, client_id, client_secret):
    """Generates access token used to call Spotify API 

    Args:
        code (str): Authorization code used to generate token
        redirect_uri (str): Allowed redirect URL set in Spotify's developer dashboard
        client_id (str): Application's id needed for OAuth 2.0 
        client_secret (str): Application's secret needed for OAuth 2.0 

    Returns:
        token (str): Access token for Spotify API 

    See:
        https://developer.spotify.com/documentation/general/guides/authorization-guide/

    """
    params = {
        "grant_type":    "authorization_code",
        "client_id":    client_id,
        "client_secret": client_secret,
        "code":          code,
        "redirect_uri":  redirect_uri
    }
    return requests.post(url='https://accounts.spotify.com/api/token', data=params).json()['access_token']


def userId(token):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }
    return requests.get(url='https://api.spotify.com/v1/me', headers=headers).json()['id']


def makePlaylist(token):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }
    params = {
        "name": "Melon Top 100",
        "public": "true",
        "description": "Made with 💖 by github.com/ko28 and generated on " + str(datetime.now())
    }
    # Weird bug that requires json.dumps(params), took me a couple days to figure out :^(
    return requests.post(url='https://api.spotify.com/v1/users/' + userId(token) + '/playlists', data=json.dumps(params), headers=headers).json()


def convertChartToPlaylist(chart, playlist_id, token):

    # Json string to a json object
    chartjson = json.loads(chart)
    # List of spotify song id's
    uri = []

    # Convert each song to English title and add that song to Spotify playlist
    for song in chartjson.values():
        # Case 01: Search raw song title in Spotify
        response = searchSong(song['name'], token)
        if response['tracks']['total'] != 0:
            trackId = response['tracks']['items'][0]['id']
            uri.append('spotify:track:' + trackId)
            continue

        # Case 02: Search song title with parentheses removed in Spotify\
        noparentheses = song['name'].split("(")[0]
        response = searchSong(noparentheses, token)
        if response['tracks']['total'] != 0:
            trackId = response['tracks']['items'][0]['id']
            uri.append('spotify:track:' + trackId)
            continue

        print("Could not find " + song['name'] + " " + song['artists'])

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }
    params = {
        "uris": uri
    }
    requests.post(url='https://api.spotify.com/v1/playlists/' +
                  playlist_id + '/tracks', headers=headers, json=params).json()
    return playlist_id


def searchSong(query, token):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }
    params = {
        "q": query,
        "type": "track",
        "limit": "1"
    }
    return requests.get('https://api.spotify.com/v1/search', params=params, headers=headers).json()
