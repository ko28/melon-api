import subprocess
import re
from bs4 import BeautifulSoup
import json

URL = {
        'LIVE': 'https://www.melon.com/chart/index.htm',
        'RISE': 'https://www.melon.com/chart/rise/index.htm',
        'DAY' : 'https://www.melon.com/chart/day/index.htm',
        'WEEK' : 'https://www.melon.com/chart/week/index.htm',
        'MONTH' : 'https://www.melon.com/chart/month/index.htm'
    }

def getList(time):
    """

    """
    html = subprocess.run(['curl', URL[time]], stdout=subprocess.PIPE)
    soup = BeautifulSoup(html.stdout, "lxml")
    data = {}
    for tag in soup.findAll("tr", {"class":["lst50", "lst100"]}):
        data[tag.find("span", {"class":["rank top", "rank"]}).getText()] = {
            "name": tag.find("div", {"class":"ellipsis rank01"}).getText().strip(),
            "ranking":tag.find("span", {"class":["rank top", "rank"]}).getText(),
            "artists": tag.find("span", {"class":"checkEllipsis"}).getText(),
            "songId": re.search(r'goSongDetail\(\'(.*)\'\)', str(tag)).group(1),
            "albumId": re.search(r'goAlbumDetail\(\'(.*)\'\)', str(tag)).group(1)
        }
    return json.dumps(data, ensure_ascii=False).encode('utf8')




