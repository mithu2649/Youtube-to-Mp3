import webbrowser
from bs4 import BeautifulSoup
import requests
import urllib.request
from pytube import YouTube
import os

word_list = []
print("Song name - artist  OR Youtube URL\n")
songToSearch = input()

#searh YouTube for the video/song
query = urllib.parse.quote(songToSearch)
url = "https://www.youtube.com/results?search_query=" + query

#get the response and find all the video id (with class yt-uix-title-link)
#and store them in the word_list[]
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    word_list.append(vid['href'])

#get the first video link
songURL = "https://youtube.com"+word_list[0]

yt = YouTube(songURL)
songToDownload = yt.streams.get_by_itag('140') #stream itag 140 is for mp4 audio

songName = yt.title
fileSize = songToDownload.filesize


#download the file
print("downloading.. ["+ str(fileSize/(1024*0.00000095367432)) +"MB]: "+songName)
songToDownload.download()
print("Download Complete.")

try:
    #rename the mp4 audio file to mp3
    #works for most of the systems with no conversion
    os.rename("songName+".mp4", songName+".mp3")
    print("Converted Succesfully")
except:
    print("Something went wrong. \nPlease convert the file manually using other software.")


