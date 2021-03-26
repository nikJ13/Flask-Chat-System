# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 23:27:50 2021

@author: anujjain
"""
from pymongo import MongoClient
from werkzeug.security import generate_password_hash # to hash the password
import time
from gridfs import GridFS
from user import User  # importing the "User" class from the user.py file
#print("test")
#print("ing")
client = MongoClient("mongodb://localhost:27017/")
chat_db = client.get_database("ChatAppDB")
users_collection = chat_db.get_collection("Users")

# =============================================================================
# avat_ctype = self.request.files['avatar'][0]["content_type"]
# 
# fs = GridFS(db)
# avatar_id = fs.put(avat, content_type=avat_ctype, filename="hangout_snapshot_0.jpg")
# 
# user={
#     ...
#     "avatar_name":avatar,
#     "avatar_id": avatar_id
#     ...
# }
# =============================================================================
#users_collection.count_documents({})
#print(users_collection)
# =============================================================================
def save_user(username,email,password,img):
     password_hash = generate_password_hash(password) # to hash the password
     print("cool")
     print(users_collection)
     users_collection.insert_one({'_id':username, 'email':email, 'password': password_hash, 'img_data':img}) 
# =============================================================================
# here defining the username as the primary key of the db
    
#save_user("niket1","cool@c.com","test")
def get_user(username):
    user_data = users_collection.find_one({'_id':username})
    print("really")
    # fetches the information about the username from the db (the above line of code)
    # now this information is made into an object of the User class (from the user.py file)
    return User(user_data['_id'],user_data['email'],user_data['password']),user_data['img_data'] if user_data else None
    
