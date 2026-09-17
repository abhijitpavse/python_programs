import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost", 
        user = "root",
        password = "123456",
        database = "demoapp"
    )

    print("Connected to MySQL successfully")

except Exception as e:
    print("Connection failed:", e)


cursor = conn.cursor()

query = "INSERT INTO students (name, course) VALUES (%s, %s)"
values = [("abhi", "python"),
          ("pratik", "python"),
          ("pratik", "sql")]

cursor.executemany(query, values) # many for multiple values
conn.commit()

print("Record inserted successfully!")

cursor.execute("SELECT * FROM students")

for row in cursor:
    print(row)

# crate table student_sprk (student_id in t primary key auto_increment, fname vatchar (50), lname)
# course_id int, status varchar(20) default 'active');

