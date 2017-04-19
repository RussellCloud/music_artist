import requests
from bs4 import BeautifulSoup
import urllib

url = "https://freemidi.org/"

result = requests.get("https://freemidi.org/genre-rock")
c = result.content

soup = BeautifulSoup(c)
samples = soup.find_all("div",class_="genre-link-text")
href_list = []

for s in samples:
    a = s.a
    href_list.append(a["href"])

music_list = []

for href in href_list:
    result = requests.get(url+href)
    c = result.content
    soup = BeautifulSoup(c)
    for div in soup.find_all("div",class_="artist-song-cell"):
        music = {"url":div.find("a", {"itemprop": "url"})["href"],"name":div.find("a", {"itemprop": "url"}).text.strip().replace(" ","_")}
        music_list.append(music)

for music in music_list:
    music_href = music["url"]
    tmp_list = music_href.split("-")
    download_url = url + "getter-"+ tmp_list[1]
    urllib.urlretrieve(download_url, "output/"+music["name"]+".midi")