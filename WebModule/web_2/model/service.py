from mongoengine import *
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

# new_service = Service(
#     name= "Tuan Anh",
#     yob=1995,
#     gender=1,
#     height=171,
#     phone="09876627348",
#     address="Hoang Mai, Hanoi",
#     status=False
# )

# new_service.save()