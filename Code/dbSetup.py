import sqlite3

conn = sqlite3.connect('assessments.db')

cursor = conn.cursor()

cursor.execute("""
                CREATE TABLE users (
                    email TEXT PRIMARY KEY,
                    names TEXT NOT NULL,
                    lastnames TEXT NOT NULL
                )""")
cursor.execute("""CREATE TABLE assessments (
                    assessment_id INTEGER PRIMARY KEY,
                    assessment_key TEXT UNIQUE,
                    email TEXT NOT NULL,
                    FOREIGN KEY (email)
                        REFERENCES users (email) 
                )""")

cursor.execute("""CREATE TABLE session (
                    session_id INTEGER PRIMARY KEY,
                    startTime TEXT NOT NULL,
                    endTime TEXT NOT NULL,
                    assessment_id TEXT NOT NULL,
                    FOREIGN KEY (assessment_id)
                        REFERENCES assessments (assessment_id)
                )""")
cursor.execute("""CREATE TABLE questions (
                    question_id INTEGER PRIMARY KEY,
                    questionText TEXT NOT NULL,
                    isOpen INTEGER NOT NULL
                )""")
cursor.execute("""CREATE TABLE answers (
                    answer_id INTEGER PRIMARY KEY,
                    answerText TEXT,
                    isCorrect INTEGER NOT NULL,
                    question_id INTEGER NOT NULL,
                    FOREIGN KEY (question_id)
                        REFERENCES questions (question_id)
                )""")
cursor.execute("""CREATE TABLE assmntXquestns (
                    assessment_id INTEGER NOT NULL,
                    question_id INTEGER NOT NULL,
                    user_ans_closed INTEGER,
                    user_ans_open TEXT
                )""")
conn.commit()
conn.close()

