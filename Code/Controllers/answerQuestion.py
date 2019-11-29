from flask import request
from DatabaseAccess import updateAssmntClosedQuestion

def answerQuestion(assessment_key,question_n,question_type,request):
    if question_type == 0: #Question is closed
        updateAssmntClosedQuestion.updateAssmntClosedQuestion(assessment_key,question_n,request.json['selectedAnswer'])
    elif question_type == 1: #Question is open
        print("OK")
        #updateAssmntOpenQuestion.updateAssmntOpenQuestion(assessment_key,question_n,request.json['answerBody'])