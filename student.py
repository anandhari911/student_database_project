import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="student_db",
    user="postgres",
    password="anand",
    port="5432"
)
cur=conn.cursor()
while True:
    print("\n Student Management")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Exit")
    choice=input("Enter choice:")
    if choice=="1":
        id=int(input("Enter id:"))
        name=input("Enter name:")
        course=input("Enter course:")
        marks=int(input("Enter marks:"))
        cur.execute("INSERT INTO student(student_id,name,course,marks) values(%s,%s,%s,%s)",(id,name,course,marks))
        conn.commit()
        print("Student Added Successfully")
    elif choice=="2":
        cur.execute("SElECT * FROM student")
        students=cur.fetchall()
        for student in students:
            print(student)
    elif choice=="3":
          name = input("Enter Student Name: ")
          cur.execute(
            "SELECT * FROM student WHERE name ILIKE %s",
            ('%' + name + '%',)
        )
          result = cur.fetchall()
          for row in result:
            print(row)
    elif choice=="4":
        break
    else:
        print("Invalid choice")
cur.close()
conn.close()
    
