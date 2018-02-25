import pafy

url = "https://www.youtube.com/watch?v=B7bqAsxee4I"
video = pafy.new(url)
best = video.getbest(preftype="mp4")
best.download(quiet=False, filepath="./downloaded/")
