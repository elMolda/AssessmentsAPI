from flask import request
from DatabaseAccess import updateAssmntClosedQuestion, updateAssmntOpenQuestion, endAssessment

def answerLastQuestion(assessment_key,question_type,request,sentTime):
    question_n = 6
    #Validate the question type
    if question_type == 0: #Question is closed
        updateAssmntClosedQuestion.updateAssmntClosedQuestion(assessment_key,question_n,request.json['selectedAnswer']) #Call propper controller  with selectedAnswer from request
    elif question_type == 1: #Question is open
        updateAssmntOpenQuestion.updateAssmntOpenQuestion(assessment_key,question_n,request.json['answerBody']) #Call propper controller  with answerBody from request
    return endAssessment.endAssessment(assessment_key, sentTime)


