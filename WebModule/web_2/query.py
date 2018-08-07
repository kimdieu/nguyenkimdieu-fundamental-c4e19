from model.service import Service
import mlab

mlab.connect()

id_to_find = "5b5b2618aad6ae0b86cb7511"

# service = Service.objects(id=id_to_find) 
# => []
# service = Service.objects.get(id=id_to_find)
# => object
service = Service.objects.with_id(id_to_find)

# print
# print (service.to_mongo())


if service is not None:
    # delete
    # service.delete()
    # print ("Deleted")

    # update
    print('Before: ', service.to_mongo())
    service.update(set__name="Tuan Anh", set__yob=2011)
    service.reload()
    print('After: ', service.to_mongo())

else:
    print ("Not found")
