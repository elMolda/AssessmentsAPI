import sqlite3

def retrieveAsstDates(assessment_key):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("SELECT startTime, deadlineTime FROM assessments WHERE assessment_key = ?", (str(assessment_key),))#Query the dates
    dateTuple = cursor.fetchone() #Get the date strings
    return dateTuple[0], dateTuple[1]