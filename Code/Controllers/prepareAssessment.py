from flask import request
from DatabaseAccess import createUser
from Entities.User import User
def prepareAssessment(requestData):
    user = User(request.json['email'], request.json['names'], request.json['lastnames']) #Create user object
    createUser.insertUser(user) #Create user in the db
    #Create Assessment with user email and key 
    #Create Session with assessment key. Get current dt and set end time to +1h