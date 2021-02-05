import requests
import re
import json
import os
import os
from datetime import datetime
from bs4 import BeautifulSoup

URL = {
    'LIVE': 'https://www.melon.com/chart/index.htm',
    'RISE': 'https://www.melon.com/chart/rise/index.htm',
    'DAY': 'https://www.melon.com/chart/day/index.htm',
    'WEEK': 'https://www.melon.com/chart/week/index.htm',
    'MONTH': 'https://www.melon.com/chart/month/index.htm'
}


def getList(time):
    """Generates json file of the top 100 songs + (additional metadata) on Melon
    Args:
        time (str): Which chart you want (LIVE, RISE, DAY, WEEK, MONTH)
    Returns:
        json (str): Seralized json string that contains the top 100 songs. 
                    Key is ranking of song; value is name, ranking, artists, songId, albumId (id's are Melon specific).  
                    NOTE: You want to use json.loads(getList("time")) to deseralize the data. 
    """
    html = requests.get(URL[time.upper()], headers={
                        'User-Agent': "github.com/ko28/melon-api"}).text
    soup = BeautifulSoup(html, "lxml")
    data = {}
    # Melon recently changed how their live chart works, tried to fix it as best as I could
    if time.upper() == "LIVE":
        rank = 1
        for tag in soup.findAll("tr", {"data-song-no": True}):
            # Key is ranking of the song
            data[rank] = {
                "name": tag.find("div", {"class": "ellipsis rank01"}).getText().strip(),
                "artists": tag.find("span", {"class": "checkEllipsis"}).getText(),
                "ranking": rank,
                "songId": re.search(r'goSongDetail\(\'(.*)\'\)', str(tag)).group(1),
                "albumId": re.search(r'goAlbumDetail\(\'(.*)\'\)', str(tag)).group(1)
            }
            rank += 1

    else:
        for tag in soup.findAll("tr", {"class": ["lst50", "lst100"]}):
            # Key is ranking of the song
            data[tag.find("span", {"class": ["rank top", "rank"]}).getText()] = {
                "name": tag.find("div", {"class": "ellipsis rank01"}).getText().strip(),
                "ranking": tag.find("span", {"class": ["rank top", "rank"]}).getText(),
                "artists": tag.find("span", {"class": "checkEllipsis"}).getText(),
                "songId": re.search(r'goSongDetail\(\'(.*)\'\)', str(tag)).group(1),
                "albumId": re.search(r'goAlbumDetail\(\'(.*)\'\)', str(tag)).group(1)
            }
        # Some data is in Korean, must format with utf-8 to avoid printing out utf code
    return json.dumps(data, ensure_ascii=False).encode('utf-8')


def getLyric(songId):
    url = 'https://www.melon.com/song/detail.htm?songId='+str(songId)
    req = requests.get(
        url, headers={'User-Agent': "github.com/ko28/melon-api"})
    html = req.text.replace("<BR>", "\n")
    soup = BeautifulSoup(html, "lxml")
    lyrics = soup.find("div", {"class": "lyric"})
    return lyrics.text.strip()

# This is a bit of a mess since these pages are rendered via javascript we need selenium


def yearChart(seleniumDriver, year, domestic=True):
    """Generates json file of the top 50 songs + (additional metadata) on Melon

    Args:
        year (str): the year you wish to fetch
        domestic (bool): weather to pull domestic (korean) song chart or overseas chart

    Returns:
        json (str): Seralized json string that contains the top 50 songs for year.
                    Key is ranking of song; value is name, ranking, artists, songId, albumId (id's are Melon specific).
                                        NOTE: You want to use json.loads(getList("time")) to deseralize the data.

    """

    chartGenere = "KPOP" if domestic else "POP"
    url = "https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre={}&chartDate={}".format(
        chartGenere, year)

    seleniumDriver.get(url)
    html = seleniumDriver.page_source

    soup = BeautifulSoup(html, "lxml")
    data = []

    bottomList = soup.find("div", {"id": ["tb_list"]})

    for tag in bottomList.findAll("tr", {"class": ["lst50"]}):
        albumId = re.search(r'goAlbumDetail\(\'(.*)\'\)', str(tag)).group(1)
        data.append({
            "name": tag.find("div", {"class": "ellipsis rank01"}).getText().strip(),
            "ranking": tag.find("span", {"class": ["rank top", "rank"]}).getText(),
            "artists": tag.find("span", {"class": "checkEllipsis"}).getText(),
            "songId": re.search(r'goSongDetail\(\'(.*)\'\)', str(tag)).group(1),
            "albumId": albumId,
            "albumLink": "https://www.melon.com/album/detail.htm?albumId={}".format(albumId)
        })

    return data
