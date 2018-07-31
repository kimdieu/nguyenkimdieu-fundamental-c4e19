from mongoengine import *
class Customer(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()