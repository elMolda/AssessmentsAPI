from datetime import datetime, timedelta
from flask import request
from DatabaseAccess import createUser, createAssessment, createAssmtQuestion
from Entities.User import User
from Entities.Assessment import Assessment

def prepareAssessment(requestData):
    user = User(request.json['email'], request.json['names'], request.json['lastnames']) #Create user object
    createUser.insertUser(user) #Create user in the db
    startTime = datetime.now()
    deadlineTime = startTime + timedelta(hours=1)
    asst = Assessment(request.json['email'], startTime, deadlineTime)#Create Assessment with user email and key 
    asst_id = createAssessment.insertAsssessment(asst)
    createAssmtQuestion.createAsstXQues(asst_id)#Insert into asstXQue with asst_id
    return asst