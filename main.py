import pafy
import youtube_dl

link = "https://youtu.be/b80a8XKX6ws" # link must be in ""youtube.be"
video = pafy.new(link)
best = video.getbest()
print(best.resolution, best.extension)
best.download()