import sqlite3 #Module import

conn = sqlite3.connect('assessments.db') #Create local DB file and connection to DB

cursor = conn.cursor() #Create cursor to execute queries

####DDL Queries
cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    email TEXT PRIMARY KEY,
                    names TEXT NOT NULL,
                    lastnames TEXT NOT NULL
                )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS assessments (
                    assessment_id INTEGER PRIMARY KEY,
                    assessment_key TEXT UNIQUE,
                    startTime TEXT NOT NULL,
                    deadlineTime TEXT NOT NULL,
                    endTime TEXT,
                    email TEXT NOT NULL,
                    FOREIGN KEY (email)
                        REFERENCES users (email) 
                )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
                    question_id INTEGER PRIMARY KEY,
                    questionText TEXT NOT NULL,
                    isOpen INTEGER NOT NULL
                )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS answers (
                    answer_id INTEGER PRIMARY KEY,
                    answerText TEXT,
                    isCorrect INTEGER NOT NULL,
                    question_id INTEGER NOT NULL,
                    FOREIGN KEY (question_id)
                        REFERENCES questions (question_id)
                )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS assmntXquestns (
                    assessment_id INTEGER NOT NULL,
                    question_id INTEGER NOT NULL,
                    user_ans_closed INTEGER,
                    user_ans_open TEXT,
                    question_n INTEGER NOT NULL
                )""")
conn.commit() #Commit changes to DB

#######DML Queries
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('Result of 2+2', 1);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('Result of 72+78', 1);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('Result of 12-456', 1);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('Result of 78/65', 1);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('President of US', 0);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('President of Colombia', 0);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('President of Russia', 0);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('President of Spain', 0);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('President of Argentina', 0);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('President of Brasil', 0);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('President of Mexico', 0);")
cursor.execute("INSERT INTO questions (questionText, isOpen) VALUES ('President of Italy', 0);")



cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('TRUMP', 1, 5);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('PUTIN', 0, 5);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('MADURO', 0, 5);")

cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('DUQUE', 1, 6);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('AMLO', 0, 6);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('MACRI', 0, 6);")

cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('PUTIN', 1, 7);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('TRUMP', 0, 7);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('KIM', 0, 7);")

cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('SANCHEZ', 1, 8);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('BOLSONARO', 0, 8);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('BERLUSCONI', 0, 8);")

cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('MACRI', 1, 9);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('MORENO', 0, 9);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('MORALES', 0, 9);")

cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('BOLSONARO', 1, 10);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('TRUMP', 0, 10);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('DUQUE', 0, 10);")

cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('AMLO', 1, 11);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('LULA', 1, 11);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('NORIEGA', 1, 11);")

cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('MATTARELLA', 1, 12);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('MERKEL', 0, 12);")
cursor.execute("INSERT INTO answers (answertext, iscorrect, question_id) VALUES ('KIM', 0, 12);")

conn.commit() #Commit changes to DB

conn.close() #Close connection with DB

