from flask import request
from DatabaseAccess import updateAssmntClosedQuestion, updateAssmntOpenQuestion

def answerQuestion(assessment_key,question_n,question_type,request):
    #Validate the question type
    if question_type == 0: #Question is closed
        updateAssmntClosedQuestion.updateAssmntClosedQuestion(assessment_key,question_n,request.json['selectedAnswer']) #Call propper controller  with selectedAnswer from request
    elif question_type == 1: #Question is open
        updateAssmntOpenQuestion.updateAssmntOpenQuestion(assessment_key,question_n,request.json['answerBody']) #Call propper controller  with answerBody from request

