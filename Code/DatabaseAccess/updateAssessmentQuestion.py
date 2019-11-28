import sqlite3

def createAsstXQues(asst_id):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("SELECT question_id FROM questions ORDER BY RANDOM() LIMIT 6")#Select 6 random questions for the assessment
    questions = cursor.fetchall()
    for q in questions:
        cursor.execute("""INSERT INTO assmntXquestns 
                    (assessment_id, question_id) VALUES (?, ?)""",
                    (asst_id, int(q[0])))#Insert into db
    conn.commit()
    cursor.execute("SELECT * FROM assmntXquestns")
    print(cursor.fetchall())
    conn.close()
    return asst_id