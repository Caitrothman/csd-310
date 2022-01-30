from typing import Collection
from pymongo import MongoClient 
url = "mongodb+srv://admin:<password>@cluster0.zg0hc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech 
collection = db["students"]

db.find()
docs = db.students.find ({}
)

for doc in docs: 
    print(doc)

db.find_one()
doc = db.students.find_one({"student_id": "1007"})

print(doc["student_id"])

db.find_one()
doc = db.students.find_one({"student_id": "1008"})

print(doc["student_id"])

db.find_one()
doc = db.students.find_one({"student_id": "1009"})

print(doc["student_id"])
