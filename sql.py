import sqlite3
import os

db_path = "student.db"

if os.path.exists(db_path):
    os.remove(db_path)

# Connect to sqlite
connection = sqlite3.connect(db_path)

# Creating a cursor to do sql operations
cursor = connection.cursor()

# Create table
table_info = """Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);"""
print(table_info)
cursor.execute(table_info)

# Insert records
cursor.executescript('''
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Alice', 'Physics', 'Section A', 88);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Bob', 'Mathematics', 'Section B', 92);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Charlie', 'Chemistry', 'Section A', 75);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Diana', 'Biology', 'Section C', 84);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Ethan', 'Computer Science', 'Section B', 91);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Fiona', 'Physics', 'Section A', 78);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('George', 'Mathematics', 'Section C', 85);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Hannah', 'Chemistry', 'Section B', 90);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Ian', 'Biology', 'Section A', 83);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Jack', 'Computer Science', 'Section C', 89);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Katherine', 'Physics', 'Section B', 76);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Liam', 'Mathematics', 'Section A', 95);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Mia', 'Chemistry', 'Section C', 82);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Noah', 'Biology', 'Section B', 88);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Olivia', 'Computer Science', 'Section A', 93);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Paul', 'Physics', 'Section C', 79);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Quinn', 'Mathematics', 'Section B', 87);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Riley', 'Chemistry', 'Section A', 91);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Sophia', 'Biology', 'Section C', 85);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Tyler', 'Computer Science', 'Section B', 80);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Ursula', 'Physics', 'Section A', 93);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Victor', 'Mathematics', 'Section C', 89);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Wendy', 'Chemistry', 'Section B', 77);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Xander', 'Biology', 'Section A', 91);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Yara', 'Computer Science', 'Section C', 94);
    INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Zane', 'Physics', 'Section B', 80);
''')

print("Inserted records are: ")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

# Close connection
connection.commit()
connection.close()
