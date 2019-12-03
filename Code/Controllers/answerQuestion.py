from flask import request, make_response, jsonify
from DatabaseAccess import updateAssmntClosedQuestion, updateAssmntOpenQuestion, endAssessment

def answerQuestion(assessment_key,question_n,question_type,request,sentTime):
    #Validate the question type
    if question_type == 0: #Question is closed
        updateAssmntClosedQuestion.updateAssmntClosedQuestion(assessment_key,question_n,request.json['selectedAnswer']) #Call propper controller  with selectedAnswer from request
    elif question_type == 1: #Question is open
        updateAssmntOpenQuestion.updateAssmntOpenQuestion(assessment_key,question_n,request.json['answerBody']) #Call propper controller  with answerBody from request
    if question_n == 6:#Is last question
        asst = endAssessment.endAssessment(assessment_key,sentTime)#Answer question and getAssessment data to confirm finished
        response = make_response(jsonify({"Assessment finished":asst.asstToJson()}),201)
    else: #Not last question
        response = make_response(jsonify({"Answered Recieved": "OK"}), 201)
    
    return response