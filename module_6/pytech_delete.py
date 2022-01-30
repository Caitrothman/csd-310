from pymongo import MongoClient 
url = "mongodb+srv://admin:admin@cluster0.zg0hc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech 

students = db.students

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

from typing import Collection
from pymongo import MongoClient 
url = "mongodb+srv://admin:admin@cluster0.zg0hc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n -- Displaying Students Documents From find() Query --")

for doc in student_list: 
    print(" Student_ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

thorin = students.find_one({"student_id": "1007"})

print("\n -- Displaying Student Document from find_one() Query --")
print(" Student ID: " + thorin["student_id"] + "\n First Name: " + thorin["first_name"] + "\n Last Name: " + thorin["last_name"] + "\n")

bilbo = students.find_one({"student_id": "1008"})

print("\n -- Displaying Student Document from find_one() Query --")
print(" Student ID: " + bilbo["student_id"] + "\n First Name: " + bilbo["first_name"] + "\n Last Name: " + bilbo["last_name"] + "\n")

frodo = students.find_one({"student_id": "1009"})

print("\n -- Displaying Student Document from find_one() Query --")
print(" Student ID: " + frodo["student_id"] + "\n First Name: " + frodo["first_name"] + "\n Last Name: " + frodo["last_name"] + "\n")

print("\n -- Insert Statements --")

db.insert_one()
john = {
    "first_name": "John"}
{
    "last_name" : "Doe"
} 
{
    "student_id" : "1010"
}

john_student_id = db.students.insert_one(john).inserted_id 

print(john_student_id)

db.find()
docs = db.students.find ({}
)

for doc in docs: 
    print(doc)

db.find_one()
doc = db.students.find_one({"student_id": "1010"})

print(doc["student_id"])

for doc in student_list: 
    print(" Student_ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

john = students.find_one({"student_id": "1007"})

print("\n -- Displaying Student Document from find_one() Query --")
print(" Student ID: " + john["student_id"] + "\n First Name: " + john["first_name"] + "\n Last Name: " + john["last_name"] + "\n")

result = db.collection.delete_one ({"student_id" : 1010})

print("\n -- Displaying Students Documents From find() Query --")

for doc in student_list: 
    print(" Student_ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

thorin = students.find_one({"student_id": "1007"})

print("\n -- Displaying Student Document from find_one() Query --")
print(" Student ID: " + thorin["student_id"] + "\n First Name: " + thorin["first_name"] + "\n Last Name: " + thorin["last_name"] + "\n")

bilbo = students.find_one({"student_id": "1008"})

print("\n -- Displaying Student Document from find_one() Query --")
print(" Student ID: " + bilbo["student_id"] + "\n First Name: " + bilbo["first_name"] + "\n Last Name: " + bilbo["last_name"] + "\n")

frodo = students.find_one({"student_id": "1009"})

print("\n -- Displaying Student Document from find_one() Query --")
print(" Student ID: " + frodo["student_id"] + "\n First Name: " + frodo["first_name"] + "\n Last Name: " + frodo["last_name"] + "\n")

input("\n\n End of program, press any key to continue...")