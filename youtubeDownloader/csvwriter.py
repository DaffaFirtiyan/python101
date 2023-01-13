import csv

csv_file = "youtubeDownloader\youtube_videos.csv"

with open(csv_file, mode="a", newline="") as file:
    writer = csv.writer(file)
    while True:
        link = input("Link (one at a time then press enter): ")
        if link == "q":
            break

        writer.writerow([link])