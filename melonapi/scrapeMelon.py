import subprocess
import re
from bs4 import BeautifulSoup
import json

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
    html = subprocess.run(['curl', URL[time]], stdout=subprocess.PIPE)
    soup = BeautifulSoup(html.stdout, "lxml")
    data = {}
    # Iterate over html by song, lst50 is 1 ~ 50, lst100 is 51 ~ 100
    for tag in soup.findAll("tr", {"class": ["lst50", "lst100"]}):
        # Key is ranking of the song
        data[tag.find("span", {"class": ["rank top", "rank"]}).getText()] = {
            "name": tag.find("div", {"class": "ellipsis rank01"}).getText().strip(),
            "ranking": tag.find("span", {"class": ["rank top", "rank"]}).getText(),
            "artists": tag.find("span", {"class": "checkEllipsis"}).getText(),
            "songId": re.search(r'goSongDetail\(\'(.*)\'\)', str(tag)).group(1),
            "albumId": re.search(r'goAlbumDetail\(\'(.*)\'\)', str(tag)).group(1)
        }
    # Some data is in Korean, must format with utf8 to avoid printing out utf code
    return json.dumps(data, ensure_ascii=False).encode('utf8')
