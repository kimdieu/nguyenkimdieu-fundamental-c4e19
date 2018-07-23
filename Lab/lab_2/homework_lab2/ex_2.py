from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html = urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn").read().decode('utf-8')

# f = open("cafef.html", "w")
# f.write(html)
# f.close()

soup = BeautifulSoup(html, "html.parser")
div = soup.find("div", style = "overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")

table = div.find_all("table")

# import pyexcel
# a_list_of_dictionaries = []
# bai_hat = []

for tr in table:
    print (tr)
    # a = li.h3
    # b = li.h4
    # names = a.string
    # artists = b.string
    # dic = {
    #     "NAMES": names,
    #     "ARTISTS": artists
    #     }
    # a_list_of_dictionaries.append(dic)

# pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="itunes_chart_2018.xlsx")
