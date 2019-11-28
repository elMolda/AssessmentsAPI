from datetime import datetime, timedelta
from flask import request
from DatabaseAccess import createUser, createAssessment, createAssmtQuestion
from Entities.User import User
from Entities.Assessment import Assessment

def prepareAssessment(requestData):
    #Create user object
    user = User(request.json['email'], request.json['names'], request.json['lastnames']) 
    #Store user in the db. Won't be created if already exists
    createUser.insertUser(user) 
    #Create assessment object
    startTime = datetime.now() #Assemnt starts now
    deadlineTime = startTime + timedelta(hours=1) #Assemnt deadline is 1 hour
    #Create Assessment object
    asst = Assessment(request.json['email'], startTime, deadlineTime)
    #Store Assessment in db.
    asst_id = createAssessment.insertAsssessment(asst)#Get Assessment id to prepare questions
    #Assign questions to created Assemnt
    createAssmtQuestion.createAsstXQues(asst_id)
    #Return Assemnt object to server response
    return asst