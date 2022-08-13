import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000000000"
)

c = db.cursor()
c.execute(f"create database if not exists ems;")
c.execute(f"use ems;")
c.execute("create table if not exists employees(id int, name varchar(30), salary int(50), position varchar(30), phoneNumber varchar(14), department varchar(30) primary key (id, phoneNumber) );")
db.commit()


def addEmployes(cc):
    id = int(input("id(int) : "))
    name = str(input("name : "))
    salary = int(input("salary(int) : "))
    position = str(input("position : "))
    phoneNumber = str(input("phone number : "))
    department = str(input("Department : "))

    try:
        cc.execute(f"insert into employees values ({id}, '{name}', {salary}, '{position}', {phoneNumber});")
        myresult = cc.fetchall()
        for x in myresult:
            print(x)

    except mysql.connector.errors.IntegrityError:
        print("integrity error")


def tableprint(cc):
    cc.execute(f"select * from employees;")
    myresult = cc.fetchall()
    print("[id|      name      |   salary   | position |  phoneNumber  ]")
    for x in myresult:
        print(str(list(x)).replace(",", " |", 4))


def find_staff(cc):
    name = str(input("name : "))
    cc.execute(f"select * from employees where name = '{name}';")
    myresult = cc.fetchall()
    for x in myresult:
        print(f"\nid :{x[0]}\nname : {x[1]}\nsalary : {x[2]}\nposition : {x[3]}\nphoneNumber : {x[4]}")


def remove_staff(c,d):
    tableprint(c)
    a = int(input("id(int) : "))
    c.execute(f"delete from employees where id = {a}")
    d.commit()


def start():
    print("*"*89)
    for x in range(5):
        print("*"," "*85,"*")
    
    print(f"*{' '*30}EMPLOYEE MANAGEMENT SYSTEM{' '*31}*")

    for x in range(5):
        print("*"*89)


while True:
    print("1: add new employee")
    print("2: list of employees")
    print("3: find employee")
    print("4: remove employee")
    print("5: exit")
    p = int(input(">>>"))
    if p == 1:
        addEmployes(c)
    elif p == 2:
        tableprint(c)
    elif p == 3:
        find_staff(c)
    elif p == 4:
        remove_staff(c,db)
    elif p == 5:
        db.commit()
        db.close()
        break
    else:
        print("wrong input")
        continue

print("Thank you for using EmployeeManagementSystem", "created by :", " - Sashwat Jain", " - Bhavya Bajaj", " - Dhvij Shah", sep="\n")
