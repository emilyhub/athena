import pafy
import urllib
from bs4 import BeautifulSoup

query = urllib.parse.urlencode([("search_query", "dog video")])
url = "https://www.youtube.com/results?" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
url = 'https://www.youtube.com' + soup.findAll(attrs={'class':'yt-uix-tile-link'})[1]['href']
video = pafy.new(url)
best = video.getbest(preftype="mp4")
best.download(quiet=False, filepath="./downloaded/")
