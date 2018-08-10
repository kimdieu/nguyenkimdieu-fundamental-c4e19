from mongoengine import *
class Video(Document):
    link = StringField()
    title = StringField()
    views = IntField()
    thumbnail = StringField()
    youtube_id = StringField()