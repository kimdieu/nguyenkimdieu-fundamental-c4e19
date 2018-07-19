from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html = urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn").read().decode('utf-8')

f = open("itunes.html", "w")
f.write(html)
f.close()

soup = BeautifulSoup(html, "html.parser")
div = soup.find("div", style = "overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")




