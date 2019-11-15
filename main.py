
import subprocess, os

movieList = os.listdir(r"C:\Users\ayieko\movies\TvShows\The.Crown.SEASON.02.S02.COMPLETE.720p.10bit.WEBRip.2CH.x265.HEVC-PSA")
FFMPEG = "<path to ffmpeg>"

for movie in movieList:
    print("converting...", movie)

    command = "{ff} -i {in} -s 1280x720 {out}"

    print("done converting ", movie)

subprocess.run("<path to mp3 file>", shell=True)

    
