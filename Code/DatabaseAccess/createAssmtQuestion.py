import sqlite3

def createAsstXQues(asst_id):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("SELECT question_id FROM questions ORDER BY RANDOM() LIMIT 6")#Select 6 random questions for the assessment
    questions = cursor.fetchall()
    n = 1
    for q in questions:
        cursor.execute("""INSERT INTO assmntXquestns 
                    (assessment_id, question_id, question_n) VALUES (?, ?, ?)""",
                    (asst_id, int(q[0]), n))#Insert into db
        n += 1
    conn.commit()
    conn.close()
    return asst_id