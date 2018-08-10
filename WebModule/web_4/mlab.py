import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds115472.mlab.com:15472/csh

host = "ds115472.mlab.com"
port = 15472
db_name = "csh"
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
