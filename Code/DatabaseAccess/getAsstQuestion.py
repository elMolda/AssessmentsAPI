import sqlite3
from Entities.Question import Question

def getAsstQuestion(assessment_key,question_n):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("""
        SELECT 
            question_id, questiontext, isopen
        FROM 
            questions
        WHERE
            question_id 
        IN 
            (SELECT question_id 
            FROM assmntXquestns
            WHERE question_n = ? 
            AND assessment_id IN 
                (SELECT assessment_id
                FROM assessments
                WHERE assessment_key = ?))
        """,(int(question_n),assessment_key))#Retrieve the question and validate that it exists in the given asssessment.
    questionTuple = cursor.fetchone()
    question = Question(questionTuple[0],questionTuple[1],questionTuple[2])
    conn.close()
    return question
    
    
