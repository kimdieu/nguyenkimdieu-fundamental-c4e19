import mongoengine
from model.service import Service

# mongodb://Dieu Nguyen:Kimnguyen389@ds245277.mlab.com:45277/muadongkhonglanh-c4u19

host = "ds245277.mlab.com"
port = 45277
db_name = "muadongkhonglanh-c4u19"
user_name = "Dieu Nguyen"
password = "Kimnguyen389"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
