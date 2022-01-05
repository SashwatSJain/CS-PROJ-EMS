import mysql.connector

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

    try:
        m.execute(f"insert into employees values ({a}, '{b}', {c}, '{d}', {e});")
        mydb.commit()
    except mysql.connector.errors.IntegrityError:
        print("integrity ertror")


def TABLE(m):
    tbl = str("list of employees : \n")
    m.execute(f"select * from employees;")
    myresult = m.fetchall()
    tbl += str("[id | name | salary | position | phoneNumber]\n")
    for x in myresult:
        tbl += str(list(x)).replace(",", " |", 4)
        tbl += str("\n")
    return tbl


def find_staff(m):
    a = str(input("name : "))
    m.execute(f"select * from employees where name = '{a}';")
    myresult = m.fetchall()
    for x in myresult:
        print(f"\nid :{x[0]}\nname : {x[1]}\nsalary : {x[2]}\nposition : {x[3]}\nphoneNumber : {x[4]}")

def remove_staff(m):
    a = int(input("id(int) : "))
    m.execute(f"delete from employees where id = {a}")
    mydb.commit()

def start():
    print("*"*89)
    for x in range(5):    
        print("*"," "*85,"*")

    print("*                              EMPLOYEE MANAGEMENT SYSTEM                               *")
    for x in range(5):    
        print("*"," "*85,"*")
    print("*"*89, "\n")


start()

while True:
    p = int(input("\n1 : List of employees\n2 : register new employee\n3 : find employee with name\n4 : remove\n5 : exit\n>>>"))
    if p == 1:
        print(TABLE(mycursor))
    elif p == 2:
        newStaff(mycursor)
    elif p == 3:
        find_staff(mycursor)
    elif p == 4:
        remove_staff(mycursor)
        print(TABLE(mycursor))
    elif p == 5:
        print("committing changes")
        mydb.commit()
        print("terminating...")
        mydb.close()
        print("terminated")
        break
    else:
        print("invalid input")