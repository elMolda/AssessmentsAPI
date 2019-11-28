import sqlite3

def insertAsssessment(asst):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("""INSERT INTO assessments 
                    (email, assessment_key, startTime, deadlineTime) VALUES (?, ?, ?, ?)""",
                    (asst.email, asst.assessment_key, asst.startTime, asst.deadlineTime))#Insert into db    
    conn.commit()
    #Get Assemnt id to associate with questions 
    cursor.execute("SELECT assessment_id FROM assessments WHERE assessment_key = ?",(asst.assessment_key,)) #Get asst id from DB
    asst_id = int(cursor.fetchone()[0])
    conn.close()
    return asst_id