"""
Simple wrapper for Spotify API 
"""
import requests
import json
import time
import random
from datetime import datetime

def token(code, redirect_uri, ClientId, ClientSecret):
    """Generates access token used to call Spotify API 

    Args:
        code (str): Authorization code used to generate token
        redirect_uri (str): Allowed redirect URL set in Spotify's developer dashboard
        ClientId (str): Application's id needed for OAuth 2.0 
        ClientSecret (str): Application's secret needed for OAuth 2.0 
   
    Returns:
        token (str): Access token for Spotify API 
   
    See:
        https://developer.spotify.com/documentation/general/guides/authorization-guide/

    """
    params = {
                "grant_type":    "authorization_code",
                "client_id" :    ClientId,
                "client_secret": ClientSecret,
                "code":          code,
                "redirect_uri":  redirect_uri
            }
    return requests.post(url='https://accounts.spotify.com/api/token', data=params).json()['access_token']

def userId(token):
    headers = {
        "Authorization" : "Bearer " +  token,
        "Content-Type" : "application/json"
    }
    return requests.get(url='https://api.spotify.com/v1/me', headers=headers).json()['id']

def makePlaylist(token):
    headers = {
        "Authorization" : "Bearer " +  token,
        "Content-Type" : "application/json"
    }
    params = {
            "name" : "Melon Top 100",
            "public": "true",
            "description" : "Made by github.com/ko28 and generated on " + str(datetime.now())
    }
    # Weird bug that requires json.dumps(params), took me a couple days to figure out :^( 
    return requests.post(url='https://api.spotify.com/v1/users/' + userId(token) + '/playlists', data=json.dumps(params), headers=headers).json()

def convertChartToPlaylist(chart, playlist_id, token):
    headers = {
        "Authorization" : "Bearer " +  token,
        "Content-Type" : "application/json"
    }

    # Json string to a json object
    chartjson = json.loads(chart)
    uri = "uris=spotify:track:"
    # Convert each song to English title and add that song to Spotify playlist if it exists
    for song in chartjson.values():
        # Remove the parentheses in search terms 
        searchTerm = songNameConvert(song['name'].split("(",maxsplit=1)[0], song['artists'].split("(",maxsplit=1)[0])
        response = searchSong(searchTerm, token)
        # Check if response contains a track
        if response['tracks']['total'] != 0:
            trackId = response['tracks'][0]['id']
            uri += trackId + " "
             
    params = {
                "uri" : "spotify:track:" + uri
            }  
    requests.post(url='https://api.spotify.com/v1/playlists/'+ playlist_id +'/tracks', headers=headers, json=params)

    return uri

def searchSong(query, token):
    headers = {
        "Authorization" : "Bearer " +  token,
        "Content-Type" : "application/json"
    }
    params = {
        "q" : query,
        "type" : "track",
        "limit" : "1"
    }
    return requests.get('https://api.spotify.com/v1/search', params=params, headers=headers).json()

def songNameConvert(name, artist):
    """
    itunes api works well to convert song names, spotify sucks

    rate limit , 20/minute wtf lol

    https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/#searching
    """
    time.sleep(5)

    params = {
    "term": name + " " + artist,
    "country" : "US",
    "limit" : "1"
    }
    response = requests.get('https://itunes.apple.com/search', params=params).json()

    if response['resultCount'] == 0:
        # Try searching just the name
        params = {
            "term": name,
            "country" : "US",
            "limit" : "1"
        }
        response = requests.get('https://itunes.apple.com/search', params=params).json()
        # Return inputted
        if response['resultCount'] == 0:
            return [response['results'][0]['trackName'], response['results'][0]['artistName']]

    return [response['results'][0]['trackName'], response['results'][0]['artistName']]

