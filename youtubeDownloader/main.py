from pytube import YouTube
from sys import argv

# first command line when we run the program
link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('/Users/mdaff/Documents/Downloaded Videos')