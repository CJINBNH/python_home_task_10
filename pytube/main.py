from pytube import YouTube

yt = YouTube("https://youtu.be/OM4Y2i81Byo")
yt.streams.filter(res="360p").first().download(filename = f"name.mp4")
print(yt.title)