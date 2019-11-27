import webbrowser
from bs4 import BeautifulSoup
import requests
import urllib.request
from pytube import YouTube
import os

word_list = []
print("What song do you want to listen to?: \n")
songToSearch = input()
query = urllib.parse.quote(songToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    word_list.append(vid['href'])

songURL = "https://youtube.com"+word_list[0]

yt = YouTube(songURL)
songToDownload = yt.streams.get_by_itag('140')
songName = yt.title
fileSize = songToDownload.filesize
print("downloading.. ["+ str(fileSize/(1024*0.00000095367432)) +"MB]: "+songName)

songToDownload.download()

#rename the mp4 audio file to mp3
#works for most of the systems with no conversion
os.rename("/tmp/"+songName+".mp4", "/tmp/"+songName+".mp3")
