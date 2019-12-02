import sqlite3

def updateAssmntOpenQuestion(assessment_key,question_n,ansBody):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("""
        UPDATE assmntXquestns
        SET user_ans_open = ? 
        WHERE question_n = ? 
        AND assessment_id = (SELECT assessment_id from assessments WHERE assessment_key = ?)
    """, (str(ansBody),int(question_n),assessment_key)) #Update answer in db
    conn.commit() #Commit the canges
    cursor.execute("SELECT * FROM assmntXquestns")
    print(cursor.fetchall())
    conn.close()