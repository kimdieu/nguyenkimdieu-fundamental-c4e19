# 1. Download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://dantri.com.vn/"
# 1.1 Open a connection
conn = urlopen(url)
# 1.2 Read data
data = conn.read()
# 1.3 Decode
html = data.decode("utf_8")
# print(html)

    # cach tat:
# html = urlopen("http://dantri.com.vn/").read().decode('utf-8')
# print(html)

# save to file
# cach 1
# import urllib
# check = urllib.request.urlretrieve(url, "dantri.html")

# cach 2
# f = open("dantri.html", "w")
# f.write(html)
# f.close()

# 2. Extract ROI (Region of Interest)
# html, xml, xhtml
soup = BeautifulSoup(html, "html.parser")
ul = soup.find("ul", "ul1 ulnew")


# 3. Extract info
li_list = ul.find_all("li")
import pyexcel
a_list_of_dictionaries = []

for li in li_list:
    a = li.h4.a
    title = a.string
    href = url + a['href']
    dic = {
        "href": href,
        "title": title
        }
    a_list_of_dictionaries.append(dic)

    # print (href)

# 4. Save data to excel


pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xlsx")