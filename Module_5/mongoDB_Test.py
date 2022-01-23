from typing import Collection
from pymongo import MongoClient 
url = "mongodb+srv://admin:<password>@cluster0.zg0hc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech 
collection = db["Student"]

print("--Pytech Collection Lists--")
print(db.list_collection_names)

