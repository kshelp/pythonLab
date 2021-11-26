import requests
from bs4 import BeautifulSoup

url = "https://music.bugs.co.kr/chart/track/week/total?chartdate=20200921"
html_music = requests.get(url).text
soup_music = BeautifulSoup(html_music, "lxml")

titles = soup_music.select('p.title a')
artists = soup_music.select('p.artist a:not(.more)')

music_titles = [title.get_text() for title in titles]
music_artists = [artist.get_text().strip() for artist in artists]

for k in range(7):
    print("{0}: {1} / {2}".format(k+1, music_titles[k], music_artists[k]))