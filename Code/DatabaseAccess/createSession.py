import sqlite3

def insertSession(session):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("""INSERT INTO session (startTime, endTime, assessment_id)
                    VALUES (?,?,?)""",(session.startTime, session.endTime, session.assessment_id))
    conn.commit()
    cursor.execute("SELECT * FROM session")
    print(cursor.fetchall())
    conn.close()