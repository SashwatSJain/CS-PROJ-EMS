import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000000000"
)

mycursor = mydb.cursor()

mycursor.execute(f"use main;")
mydb.commit()

while True:

    id, name, salary, position, phoneNumber = int(input("id(int) : ")), str(input("name : ")), int(input("salary(int) : ")), str(input("position : ")), str(input("phone number : "))

    try:
        mycursor.execute(f"insert into employees values ({id}, '{name}', {salary}, '{position}', '{phoneNumber}');")
        mydb.commit()
        mycursor.execute("select * from employees;")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    except mysql.connector.errors.IntegrityError:
            print("integrity error")
