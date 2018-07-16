from pymongo import MongoClient

uri = "mongodb://db_1:abcd1234@ds137611.mlab.com:37611/c4e19forlab"

# 1. Connect to database
client = MongoClient(uri)

# 2. Get database
db = client.get_default_database()

# 3. Creat Collection
games = db['games']
# turtle_rules = db['turtles']

# # 4. Creat Document
# replace_old = {
#     "straight": "eat 5 snacks",
#     "left": "bump into a car",
#     "right": "oops, turtle accident"
# }

# # 5. Insert doc into collection
# turtle_rules.insert_one(replace_old)

# get all documents
all_games = games.find()
print(all_games[1]['name'])