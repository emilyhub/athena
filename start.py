import pafy
import urllib
from bs4 import BeautifulSoup

def return_video(user_input: str):
    """Returns mp4 video"""
    query = urllib.parse.urlencode([("search_query", user_input)])
    url = "https://www.youtube.com/results?" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    url = 'https://www.youtube.com' + soup.findAll(attrs={'class':'yt-uix-tile-link'})[1]['href']
    video = pafy.new(url)
    return video

def download_video(video):
    best = video.getbest(preftype="mp4")
    return best

def get_audio(video: "mp4"):
    audio = video.getbestaudio()
    return audio
    

if __name__ == "__main__":
    video = return_video("Prince Royce")
    vid = download_video(video)
    vid.download(quiet=False, filepath="./downloaded/")
    audio = get_audio(video)
    audio.download(quiet = False, filepath = "./downloaded")
