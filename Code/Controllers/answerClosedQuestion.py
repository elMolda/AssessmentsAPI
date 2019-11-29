from flask import request
from DatabaseAccess import updateAssmntClosedQuestion

def answerClosedQuestion(assessment_key,question_n,selectedAns):
    updateAssmntClosedQuestion.updateAssmntClosedQuestion(assessment_key,question_n,selectedAns)
    
