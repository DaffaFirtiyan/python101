from pytube import YouTube

link = input("link here: ")
yt = YouTube(link)

yd = yt.streams.get_highest_resolution()
yd.download('/Users/mdaff/Documents/Downloaded Videos')