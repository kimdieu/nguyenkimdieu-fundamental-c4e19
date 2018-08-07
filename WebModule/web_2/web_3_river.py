from model.river import River
import web_3_mlab

web_3_mlab.connect()

continent = "Africa"

all_continent= River.objects(continent)

print (all_continent)