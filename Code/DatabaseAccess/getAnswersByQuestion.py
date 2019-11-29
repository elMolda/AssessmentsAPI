import sqlite3
from Entities.Answer import Answer #Import model class

def getAnswersByQuestion(question_id):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("""
    SELECT answer_id, answertext
    FROM answers 
    WHERE question_id = ?""",(int(question_id),)) #Get answers by question. No correctness indicator
    answersTuple = cursor.fetchall() #Retrieved data
    answers = [] #Initialize array to return
    for a in answersTuple:
        answer = Answer(a[0], a[1], question_id) #Create answer object
        answers.append(answer) #Add answer object to return array
    return answers #Return answer array