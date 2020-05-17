"""
Simple wrapper for Spotify API 
"""
import requests
import json
import time
import random
import os
from torrequest import TorRequest
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
            "description" : "Made with love by github.com/ko28 and generated on " + str(datetime.now())
    }
    # Weird bug that requires json.dumps(params), took me a couple days to figure out :^( 
    return requests.post(url='https://api.spotify.com/v1/users/' + userId(token) + '/playlists', data=json.dumps(params), headers=headers).json()

def convertChartToPlaylist(chart, playlist_id, token):
    
    os.system("sudo /etc/init.d/tor restart")

    # Json string to a json object
    chartjson = json.loads(chart)
    # List of spotify song id's
    uri = []

    # Convert each song to English title and add that song to Spotify playlist 
    for song in chartjson.values():
        # Case 01: Search song title in iTunes with parentheses removed + artist(s) name
        searchTerm = songNameConvert(song['name'].split("(",maxsplit=1)[0], song['artists'].split("(",maxsplit=1)[0])
        # Search Spoitfy for the english song name
        response = searchSong(" ".join(searchTerm), token)
        # Check if Spoify's response has a track     
        if response['tracks']['total'] != 0:
            trackId = response['tracks']['items'][0]['id']
            uri.append('spotify:track:' + trackId)
            continue

        # Case 02: Search song title with parentheses removed (from previous iTunes search) + first artist from iTunes english name
        noparentheses = searchTerm[0].split("(")[0]
        response = searchSong(noparentheses + " " + searchTerm[1].split(",")[0], token)
        if response['tracks']['total'] != 0:
            trackId = response['tracks']['items'][0]['id']
            uri.append('spotify:track:' + trackId)
            continue

        # Case 03: Search only song title with parentheses + commas removed (from previous iTunes search)
        nocommas = noparentheses.split(",")[0]
        response = searchSong(nocommas, token)
        if response['tracks']['total'] != 0:
            trackId = response['tracks']['items'][0]['id']
            uri.append('spotify:track:' + trackId)
            continue

        # Case 04: Search what in inside of parentheses from original melon song + artist, probably should use regex but I'm lazy
        name = song['name'].split('(', 1)[1].split(')')[0] if  "(" and ")" in song['name'] else song['name']
        artist = song['artists'].split('(', 1)[1].split(')')[0] if "(" and ")" in song['artists'] else ""
        response = searchSong(name + " " + artist, token)
        if response['tracks']['total'] != 0:
            trackId = response['tracks']['items'][0]['id']
            uri.append('spotify:track:' + trackId)
            continue

        print("Could not find " +  song['name'] + " " + song['artists'])
    
    headers = {
        "Authorization" : "Bearer " +  token,
        "Content-Type" : "application/json"
    }              
    params = {
        "uris" : uri
    }  
    requests.post(url='https://api.spotify.com/v1/playlists/'+ playlist_id +'/tracks', headers=headers, json=params).json()
    return playlist_id
    

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
    requires tor 
    rate limit , 20/minute wtf lol

    https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/#searching
    """
    params = {
    "term": name + " " + artist,
    "country" : "US",
    "limit" : "1"
    }
    
    tr = TorRequest(password=os.environ['TorPassword'])
    response = itunesJsonTor(params, tr)
        
    if response['resultCount'] == 0:
        # Try searching just the name
        params = {
            "term": name,
            "country" : "US",
            "limit" : "1"
        }
        response = itunesJsonTor(params, tr)
        # Return original arguments, itunes could not find a match
        if response['resultCount'] == 0:
            return [name, artist]

    return [response['results'][0]['trackName'], response['results'][0]['artistName']]

def itunesJsonTor(params, tr):
    while True:
        response = tr.get('https://itunes.apple.com/search', params=params)
        if response.status_code != 200: # Invalid response
            print("Resetting Tor identity, takes 10 seconds(ish)")
            start_time = time.time()
            tr.reset_identity() #Reset Tor
            print("reset_identity took", time.time() - start_time, "to run")
        else:
            return response.json()
