from pymongo import MongoClient
from getenv import getURL


# Creating Connection with database
def connect(coll):
    """
        This function is used for connecting to database
        param: coll , refer to collection 
    """
    url = getURL()
    dbClient = MongoClient(url)
    db = dbClient["user_data"]
    collection = db[coll]
    return collection

# inserting data to db
def insertData(coll,data):
    """
        This function is used for inserting data to database
        param:
        coll , refer to collection 
        data , refer to data to be inserted
        
    """
    collection = connect(coll)
    collection.insert_one(data)
    

# Finding data from db
def getAllData(coll):
    """
        This function is used for getting all data from database
        param:
        coll , refer to collection 
    """
    collection = connect(coll)
    records = collection.find({})
    data = []
    for record in records:
        data.append(record)
        print(record)
    return data

# Get only one record
def getData(coll,user):
    """
        This function is used for getting only one record from database
        param:
        coll , refer to collection 
        user , refer to data that to be find
        
    """
    collection= connect(coll)
    record = collection.find_one(user)
    print(record)
    for rec in record:
        print(rec)
        return rec

# get data by id
def getDatabyID(coll,id):
    """
        This function is used for getting data using id from database
        param:
        coll , refer to collection 
        id , refer to id
        
    """
    new_id = "ObjectId(" + id + ")"
    collection = connect(coll)
    records = collection.find({"_id": new_id})
    for record in records:
        return record


# deleting one record
def deleteData(coll,id):
    """
        This function is used for deleting data from database
        param:
        coll , refer to collection 
        id , refer to id
    """
    new_id = "ObjectId(" + id + ")"
    collection = connect(coll)
    collection.delete_one(new_id)

# updating record
def updateData(coll,data,id):
    """
        This function is used for updating data
        param:
        coll , refer to collection 
        data, refer to new data
        id , refer to id of old data
    """
    collection = connect(coll)
    updated_value = {"$set": data}
    new_id = "ObjectId(" + id + ")"
    collection.update_one({"_id": new_id},updated_value)
    

# updateData("lead_test@subi.com")