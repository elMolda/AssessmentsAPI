from flask import Flask, jsonify, request, make_response, redirect #Flask modules used
from Controllers import prepareAssessment, showQuestion, answerQuestion, getAsstTimes, getAllQuestions, answerLastQuestion #Files from Controllers package
from Entities.Assessment import Assessment #Files from Entities package
from Utils import checkEmail, checkDate #Files from Utils package
import datetime
import json
app = Flask(__name__) #Declare server

@app.route('/ping', methods = ['GET']) #Testing Route, for Server testing.
def ping():
    return jsonify({"message": 'Pong'})

@app.route('/test', methods = ['GET', 'POST']) #Test route. Get only for info. Post register and create asssesment
def manageTestEndpoint(): #Define response according to request method type.
    response = None #Empty response
    if request.method == 'GET': #Info about endpoint
        response = jsonify({"Message": "This is Test endpoint.Send POST request to this with user parameters to start assessment."})
    if request.method == 'POST': #Create a new User if needed. Create new Assemnt.
        if checkEmail.checkEmail(request.json['email']): #Check valid email
            asst = prepareAssessment.prepareAssessment(request) #Create a new User if needed. Create new Assemnt.
            response = make_response(jsonify({"Assessment created":asst.asstToJson()}),201) #Retrieve Assemnt data. Inform correctly created
        else:
            response = make_response(jsonify({"Message":"Not valid Email"}),400) #Not valid email. Inform bad request
    return response #Return request.

@app.route('/test/<string:assessment_key>/questions/<int:question_n>', methods=['GET']) #Get all the questions for current assessment
def getAsstQuestion(assessment_key,question_n): #Get question by number in corresponding assessment
    response = None #Empty response
    if request.method == 'GET': 
        question = showQuestion.showQuestion(assessment_key,question_n) #Pass parameters of question
        if question != None:
            response = make_response(jsonify({"Question":question.qstnToJson()}),200) #Return the found question
        else:
            response = make_response(jsonify({"Message":"Not found"}),404) #Question not found
    return response #Return response

@app.route('/test/<string:assessment_key>/questions/<int:question_n>', methods=['POST']) #Answer a question
def answerOneQuestion(assessment_key,question_n):
    response = None
    if request.method == 'POST':
        startTime, deadlineTime = getAsstTimes.getAsstTimes(assessment_key) #Get start and deadline times of the assessment
        sentTime = datetime.datetime.now() #Get the time when request was made
        if checkDate.checkDate(sentTime, startTime, deadlineTime): #If the request was made in appropiate time answer
            question_type = showQuestion.showQuestion(assessment_key,question_n).isOpen #Get question type to set apropiate behavior
            if question_n == 6:#Is last question
                asst = answerLastQuestion.answerLastQuestion(assessment_key,question_type,request,sentTime)#Answer question and getAssessment data to confirm finished
                response = make_response(jsonify({"Assessment finished":asst.asstToJson()}),200)
            else: #Not last question
                answerQuestion.answerQuestion(assessment_key,question_n,question_type,request) #Answer question 
                response = make_response(jsonify({"Answered Recieved": "OK"}), 201)
        else:
            response = make_response(jsonify({"Out of Time": "FAILED"}), 401) #Resquest was made out of time
    return response

@app.route('/test/<string:assessment_key>/questions', methods = ['GET']) #List all the questions of assessment. Just for testing purposes
def listAssessmentQuestions(assessment_key):
    response = None
    if request.method == 'GET':
        questionsJson = getAllQuestions.getAllQuestions(assessment_key)
        response = make_response(jsonify({"All questions": questionsJson}), 200)
    return response    

if __name__ == '__main__': 
    app.run(debug=True, port=5000)