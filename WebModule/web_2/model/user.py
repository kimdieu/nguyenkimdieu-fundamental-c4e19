from mongoengine import *
class User(Document):
    fullname = StringField()
    email = StringField()
    username = StringField()
    password = StringField()