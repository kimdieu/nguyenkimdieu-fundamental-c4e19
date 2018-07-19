from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

# part_1
url = "https://www.apple.com/itunes/charts/songs/"
html = urlopen("https://www.apple.com/itunes/charts/songs/").read().decode('utf-8')

f = open("itunes.html", "w")
f.write(html)
f.close()

soup = BeautifulSoup(html, "html.parser")
section = soup.find("section", "section chart-grid")


li_list = section.find_all("li")
import pyexcel
a_list_of_dictionaries = []
bai_hat = []

for li in li_list:
    a = li.h3
    b = li.h4
    names = a.string
    artists = b.string
    dic = {
        "NAMES": names,
        "ARTISTS": artists
        }
    a_list_of_dictionaries.append(dic)

# pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="itunes_chart_2018.xlsx")

    ca_si = names, artists
    bai_hat.append(ca_si)


# part_2
    options = {
        'default_search': 'ytsearch', 
    }
    dl = YoutubeDL(options)
    for search_and_down in bai_hat:
        dl.download(search_and_down)