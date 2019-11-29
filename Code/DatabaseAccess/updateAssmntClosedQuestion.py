import sqlite3

def updateAssmntClosedQuestion(assessment_key,question_n,selectedAns):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("""
        UPDATE assmntXquestns
        SET user_ans_closed = ? 
        WHERE question_n = ? 
        AND assessment_id = (SELECT assessment_id from assessments WHERE assessment_key = ?)
    """, (int(selectedAns),int(question_n),assessment_key))
    cursor.execute("SELECT * FROM assmntXquestns")
    print(cursor.fetchall())
    conn.close()