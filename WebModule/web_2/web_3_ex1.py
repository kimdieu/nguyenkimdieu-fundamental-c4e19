from model.service import Service
import mlab

mlab.connect()


Service.objects.delete({})
print ("Deleted")