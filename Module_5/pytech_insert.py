from typing import Collection
from pymongo import MongoClient 
url = "mongodb+srv://admin:<password>@cluster0.zg0hc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech 
collection = db["Student"]

db.insert_one()
thorin = {
    "first_name": "Thorin"}
{
    "last_name" : "Oakenshield"
} 
{
    "student_id" : "1007"
}

thorin_student_id = db.students.insert_one(thorin).inserted_id 

print(thorin_student_id)

db.find()
docs = db.students.find ({}
)

for doc in docs: 
    print(doc)

db.find_one()
doc = db.students.find_one({"student_id": "1007"})

print(doc["student_id"])

db.insert_one()
bilbo = {
    "first_name": "Bilbo"}
{
    "last_name" : "Baggins"
}
{
    "student_id" : "1008"
}

thorin_student_id = db.students.insert_one(bilbo).inserted_id 

print(thorin_student_id)

db.find()
docs = db.students.find ({}
)

for doc in docs: 
    print(doc)

db.find_one()
doc = db.students.find_one({"student_id": "1008"})

print(doc["student_id"])

db.insert_one()
frodo = {
    "first_name": "Frodo"}
{
    "last_name" : "Baggins"
}
{
    "student_id" : "1009"
}
thorin_student_id = db.students.insert_one(frodo).inserted_id 

print(thorin_student_id)