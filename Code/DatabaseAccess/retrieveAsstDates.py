import sqlite3

def retrieveAsstDates(assessment_key):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("SELECT startTime, deadlineTime FROM assessments WHERE assessment_key = ?", (str(assessment_key),))
    dateTuple = cursor.fetchone()
    return dateTuple[0], dateTuple[1]