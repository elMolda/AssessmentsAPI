import sqlite3

def insertUser(user):
    conn = sqlite3.connect("assessments.db") #Connect to DB
    cursor = conn.cursor() #Declare Cursor
    cursor.execute("""
        INSERT INTO users (email,names,lastnames) 
        SELECT ?, ?, ?
        WHERE NOT EXISTS(SELECT 1 FROM users WHERE email = ? AND names = ? AND lastnames = ?)""",
        (user.email, user.names, user.lastnames, user.email, user.names, user.lastnames)) #Insert user if not exists
    conn.commit()
    conn.close()
