import sqlite3
from Entities.Answer import Answer

def getAnswersByQuestion(question_id):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("""
    SELECT answer_id, answertext
    FROM answers 
    WHERE question_id = ?""",(int(question_id),))
    answersTuple = cursor.fetchall()
    answers = []
    for a in answersTuple:
        answer = Answer(a[0], a[1], question_id)
        answers.append(answer)
    return answers