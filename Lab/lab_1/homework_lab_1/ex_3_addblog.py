from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database()

posts = db['posts']

new_blog = {
    "title": "Hoàng hôn",
    "author": "Xuân Diệu",
    "content": """
    Hôm nay trời nhẹ lên cao,
    Tôi buồn không hiểu vì sao tôi buồn... """
}

posts.insert_one(new_blog)
