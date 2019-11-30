from Entities.Question import Question #Import model class
from DatabaseAccess import getAsstQuestion, getAnswersByQuestion #Database classes needed to retrieve question

def getAllQuestions(assessment_key):
    questionsJson = []
    for i in range(1,7): #For 6 questions
        question = getAsstQuestion.getAsstQuestion(assessment_key,i) #Get basic question data
        if question.isOpen == 0: #Closed question. Retrieve answers list
            question.answers = getAnswersByQuestion.getAnswersByQuestion(question.id) #Retrieve list of answers
        questionsJson.append(question.qstnToJson())
    return questionsJson

