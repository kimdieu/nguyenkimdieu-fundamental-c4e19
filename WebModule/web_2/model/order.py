from mongoengine import *
class Order(Document):
    service_id = StringField()
    user_id = StringField()
    time = DateTimeField()
    is_accepted = BooleanField()