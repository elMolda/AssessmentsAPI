from flask import request
from DatabaseAccess import createUser, createAssessment, updateAssessmentQuestion
from Entities.User import User
from Entities.Assessment import Assessment
def prepareAssessment(requestData):
    user = User(request.json['email'], request.json['names'], request.json['lastnames']) #Create user object
    createUser.insertUser(user) #Create user in the db
    asst = Assessment(request.json['email'])#Create Assessment with user email and key 
    asst_id = createAssessment.insertAsssessment(asst)
    updateAssessmentQuestion.createAsstXQues(asst_id)#Insert into asstXQue with asst_id
    

    #Create Session with assessment key. Get current dt and set end time to +1h