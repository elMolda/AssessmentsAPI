from Entities.Question import Question
from DatabaseAccess import getAsstQuestion

def showQuestion(assessment_key,question_n):
    question = getAsstQuestion.getAsstQuestion(assessment_key,question_n)
    return question
