from asyncore import read
import os
from re import A
from unittest import result
import pymongo
import json

client = pymongo.MongoClient("localhost", 2717)
db = client.db2

# id = 10001

path = "[PATH]"
dir_list = os.listdir(path)

# imports the files to mongodb
# for people in dir_list:
#     if people.endswith(".txt"):
#         with open(path + people, 'r') as person:
#             pfile = person.read()
#             plist = pfile.split(", ")
#             personj = {'_id': id,
#                        'firstName': plist[1],
#                        'lastName': plist[2],
#                        'hireYear': plist[3].strip()}
#             db.sampleapp.insert_one(personj)
#             id += 1

def add(fname, lname, hyear):
    global id
    db.sampleapp.insert_one({
        '_id': id,
        'firstName': fname,
        'lastName': lname,
        'hireYear': hyear
    })
    id += 1

def delete(id):
    db.sampleapp.delete_one({'_id':id})

def update(id, fname=None, lname=None, hyear=None):
    person = {}
    if fname != None:
        person['firstName'] = fname
    if lname != None:
        person['lastName'] = lname
    if hyear != None:
        person['hireYear'] = hyear
    db.sampleapp.update_one({'_id':id}, {'$set':person})

#to find one person use id otherwise finds all matching data
def find(id=None, fname=None, lname=None, hyear=None):
    person = {}
    if id != None:
        person['_id'] = id
    if fname != None:
        person['firstName'] = fname
    if lname != None:
        person['lastName'] = lname
    if hyear != None:
        person['hireYear'] = hyear
    
    print(*db.sampleapp.find(person))

# add('Mathew', 'Sjoquist', '2024')
# find(hyear='1986')
# update(1, hyear='1986')
# delete(10001) #currently deletes the newly added id 

# #for document questions
# def addProp(id, bday):
#     db.sampleapp.update_one({'_id':id}, {'$set': {'birthday': bday}})

# def replace(id, fname, lname, hyear):
#     db.sampleapp.replace_one(
#         {'_id': id},
#         {'firstName': fname, 'lastName':lname, 'hireYear':hyear}
#     )

# # replace(10001, 'John', 'Doe', '1996')
# # addProp(45, 'August 25th')
# # flist = db.sampleapp.find({"hireYear": {'$regex':"20"}})
# # for item in flist:
# #     print(item)
# # flist2 = db.sampleapp.find({'birthday':{'$exists':False}})
# # for item in flist2:
# #     print(item)

# # total_count = db.sampleapp.count_documents({'birthday':{'$exists':True}})
# # print(total_count)

# # myResult = db.sampleapp.aggregate(
# #     [{
# #         '$group':
# #             {'_id': '$firstName',
# #              "total": {'$sum':1}}
# #     }]
# # )
# # for item in myResult:
# #     print(item)

# print(*db.sampleapp.find({'_id': {'$gte': 300, '$lte':400}}).explain()['executionStats'])