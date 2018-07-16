from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database()

customers = db['customers']

# count
wom = customers.find({"ref": "wom"}).count()

ads = customers.find({"ref": "ads"}).count()

events = customers.find({"ref": "events"}).count()

print("Events: {0} ; Advertisements: {1} ; Word of mouth: {2}".format(events, ads, wom))

# pie chart
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

labels = ["events", "ads", "wom"]
values = [events, ads, wom]
colors = ['coral', 'gold', 'pink']

pyplot.pie(values, labels= labels, 
                    colors= colors)
pyplot.axis("equal")

pyplot.show()