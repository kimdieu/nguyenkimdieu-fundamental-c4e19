import mlab
from model.service import Service

mlab.connect()

# cach 1
abc = Service.objects.get(id='5b5b1c42aad6ae084342a850')
print (abc.name)

# cach 2
import bson
abc = Service.objects.get(id=bson.objectid.ObjectId('5b5b1c42aad6ae084342a850'))
print (abc.name)


# ex_3
abc = Service.objects(id='5b5b1c42aad6ae084342a850')
abc.delete()