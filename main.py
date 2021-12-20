# Employee registration

import mysql.connector
from pprint import pprint

# user : root
# password : 0000000000
usr = input("username : ")
pwd = input("password : ")

mydb = mysql.connector.connect(
    host="localhost",
    user=usr,
    password=pwd
)

print(mydb)
mycursor = mydb.cursor()

mycursor.execute("create database if not exists main;")
mycursor.execute("use main;")
mycursor.execute("create table if not exists employees(id int, name varchar(30), salary int, position varchar(30), phoneNumber varchar(20), primary key (id, phoneNumber) );")


def newStaff(m):
    a = int(input("id(int) : "))
    b = str(input("name : "))
    c = int(input("salary(int) : "))
    d = str(input("position : "))
    e = str(input("phone number : "))
    # other columns can also be added

    try:
        m.execute(f"insert into employees values ({a}, '{b}', {c}, '{d}', {e});")
        myresult = m.fetchall()
        for x in myresult:
            print(x)
    except mysql.connector.errors.IntegrityError:
        pprint("integrity error")


def TABLE(m):
    m.execute(f"select * from employees;")
    myresult = m.fetchall()
    print("[id | name | salary | position | phoneNumber]")
    for x in myresult:
        print(str(list(x)).replace(",", " |", 4))


def find_staff(m):
    a = str(input("name : "))
    m.execute(f"select * from employees where name = '{a}';")
    myresult = m.fetchall()
    for x in myresult:
        print(f"\nid :{x[0]}\nname : {x[1]}\nsalary : {x[2]}\nposition : {x[3]}\nphoneNumber : {x[4]}")


while True:
    p = int(input("\n1 : List of employees\n2 : register new employee\n3 : find employee with name\n4 : exit\n>>>"))
    if p == 1:
        TABLE(mycursor)
    elif p == 2:
        newStaff(mycursor)
    elif p == 3:
        find_staff(mycursor)
    elif p == 4:
        print("committing changes")
        mydb.commit()
        print("terminating...")
        mydb.close()
        print("terminated")
        break
