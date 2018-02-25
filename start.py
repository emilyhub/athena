import pafy
import urllib
from bs4 import BeautifulSoup

def download_video(user_input: str):
    """Returns mp4 video"""
    query = urllib.parse.urlencode([("search_query", user_input)])
    url = "https://www.youtube.com/results?" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    url = 'https://www.youtube.com' + soup.findAll(attrs={'class':'yt-uix-tile-link'})[1]['href']
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    return best
    #best.download(quiet=False, filepath="./downloaded/")
