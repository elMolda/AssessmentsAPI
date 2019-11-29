from Entities.Question import Question #Import model class
from DatabaseAccess import getAsstQuestion, getAnswersByQuestion #Database classes needed to retrieve question

def showQuestion(assessment_key,question_n): #Assessment key and question number in asssessment
    question = getAsstQuestion.getAsstQuestion(assessment_key,question_n) #Get basic question data
    if question.isOpen == 0: #Closed question. Retrieve answers list
        question.answers = getAnswersByQuestion.getAnswersByQuestion(question.id) #Retrieve list of answers
    return question
