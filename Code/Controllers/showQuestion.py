from Entities.Question import Question
from DatabaseAccess import getAsstQuestion, getAnswersByQuestion

def showQuestion(assessment_key,question_n):
    question = getAsstQuestion.getAsstQuestion(assessment_key,question_n)
    if question.isOpen == 0: #Closed question. Retrieve answers list
        question.answers = getAnswersByQuestion.getAnswersByQuestion(question.id)
    return question
