import sqlite3
from Entities.Assessment import Assessment

def endAssessment(assessment_key, sentTime):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("""
        UPDATE assessments
        SET endtime = ? 
        WHERE assessment_key = ? 
    """, (sentTime,assessment_key)) #Update in db
    conn.commit()
    cursor.execute("SELECT * FROM assessments WHERE assessment_key = ?", (assessment_key,)) #Get asssessment data
    asst_tuple = cursor.fetchone()
    asst = Assessment(asst_tuple[5],asst_tuple[2],asst_tuple[3],asst_tuple[4]) #Create assessment object
    asst.assessment_key = assessment_key
    conn.close()
    return asst