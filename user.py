# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:51:12 2021

@author: anujjain
"""
from werkzeug.security import check_password_hash

class User:
    # initialised the class variables
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    @staticmethod     # since the function does not use any class parameters
    def is_authenticated():
        return True
    
    @staticmethod
    def is_active():
        return True
    
    @staticmethod
    def is_anonymous():
        return False
    
    def get_id(self):
        return self.username
    
    # to compare the password plaintext entered in the form with the hashed password saved in the db
    def check_password(self, password_input):
        return check_password_hash(self.password,password_input)
        
        
        