import os
import csv
from pytube import YouTube
from moviepy.editor import *

outFolder = "F:\mp3_files"
if not os.path.exists(outFolder):
    os.mkdir(outFolder)

# specify the csv file containing the youtube video urls
csv_file = "youtubeDownloader\youtube_videos.csv"

# open the csv file and read the video urls
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        url = row[0]
        yt = YouTube(url)
        print(yt.title)
        vid = yt.streams.filter(file_extension='mp4',res='720p').first()

        print("Downloading video...")
        vid.download(output_path=outFolder)

        input = os.path.join(outFolder, vid.default_filename)
        output = os.path.join(outFolder, vid.default_filename.replace(".mp4", ".mp3"))

        vid = VideoFileClip(input)

        print("Extracting audio...")
        audio = vid.audio

        audio.write_audiofile(output)

        vid.close()
        os.remove(input)
        print("Download complete :)")