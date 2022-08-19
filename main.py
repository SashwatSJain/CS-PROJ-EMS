import mysql.connector


def start():
    # print(a)
    print("*" * 89)
    for x in range(2):
        print("*", " " * 85, "*")

    print("*                              EMPLOYEE MANAGEMENT SYSTEM                               *")
    print("*                       Sashwat Jain, Bhavya Bajaj and Dhvij Shah                       *")
    for x in range(2):
        print("*", " " * 85, "*")
    print("*" * 89)


usr = input("SQL username : ")
pwd = input("SQL password : ")

mydb = mysql.connector.connect(
    host="localhost",
    user=usr,
    password=pwd
)

print(mydb)
mycursor = mydb.cursor()
# creating database and table
mycursor.execute("create database if not exists main;")
mycursor.execute("use main;")
mycursor.execute(
    "create table if not exists employees(id int(8), name char(20), salary int, position varchar(10), phoneNumber varc"
    "har(20), startyear varchar(11) NOT NULL,department VARCHAR(30) NOT NULL, primary key (id, phoneNumber) );")


def new_staff(m):
    # function to register new staff
    a = int(input("id(int) : "))
    b = str(input("name : "))
    c = int(input("salary(int) : "))
    d = str(input("position : "))
    e = str(input("phone number : "))
    f = str(input("start year : "))
    g = str(input("department : "))

    try:
        m.execute(
            f"insert into employees values ({a}, '{b}', {c}, '{d}', {e} , '{f}' , '{g}' );")
        mydb.commit()
    except mysql.connector.errors.IntegrityError:
        print("integrity error - employee not registered")


def edit_details(m):
    # function to edit employee details
    a = int(input("id(int) : "))
    m.execute(f"select * from employees where id = {a}")
    myresult = m.fetchall()
    if myresult:
        for x in myresult:
            print(f"\nid :{x[0]}\nname : {x[1]}\nsalary : {x[2]}\nposition : {x[3]}\nphoneNumber : {x[4]}\nstartyear : {x[5]}"
                  f"\ndepartment : {x[6]}")

        b = str(input("name : "))
        c = int(input("salary(int) : "))
        d = str(input("position : "))
        e = str(input("phone number : "))
        f = str(input("start year : "))
        g = str(input("department : "))

        m.execute(
            f"update employees set name='{b}', salary={c}, position='{d}', phoneNumber={e}, startYear='{f}', department='{g}' where id={a};")
        mydb.commit()
        print("Employee Details Updated")
    else:
        print("Employee not found")


def full_table(m):
    # function to display full table
    m.execute(f"select * from employees;")
    myresult = m.fetchall()
    tbl = "[   id |       name       |      salary     |  position  |phoneNumber |  startYear |   department  ]"
    print("\n \nDisplaying Employee Menu...")
    print(tbl)
    for x in myresult:
        print("%6s" % str(x[0])[0:4], "|", "%16s" % x[1][0:13], "|", "%15s" % str(x[2])[0:11], "|", "%10s" % x[3],
              "|", "%10s" % x[4], "|", "%10s" % x[5], "|", "%10s" % x[6])


def filteredtable(m):
    # function to display filtered table based on salary, start year, and department
    print("""
* * * * * * * * * * * * * * * 
*  1. full table            *
*  2. filter by salary      *
*  3. filter by start year  *
*  4. filter by department  *
* * * * * * * * * * * * * * * 
""")
    o = int(input(">>>"))
    if o == 1:
        m.execute(f"select * from employees;")
        myresult = m.fetchall()
    elif o == 2:
        j = str(input("Greater than, Less than or Equal [>,<,=] : "))
        i = int(input("Enter Salary : "))
        m.execute(f"select * from employees where Salary {j} {i};")
        myresult = m.fetchall()
    elif o == 3:
        j = str(input("Greater than, Less than or Equal [>,<,=] : "))
        i = str(input("Enter StartYear <YYYY>: "))
        m.execute(f"select * from employees where StartYear {j} '{i}';")
        myresult = m.fetchall()
    elif o == 4:
        i = str(input("Enter Department : "))
        m.execute(f"select * from employees where Department='{i}';")
        myresult = m.fetchall()
    else:
        print("invalid option")
        pass

    tbl = "[   id |       name      |      salary     |  position  |phoneNumber |  startYear |   department  ]"
    print("\n \nDisplaying Employee Menu...")
    print(tbl)
    try:
        for x in myresult:
            print("%6s" % str(x[0])[0:4], "|", "%15s" % x[1][0:12], "|", "%15s" % str(x[2])[0:11], "|", "%10s" % x[3],
                  "|", "%10s" % x[4], "|", "%10s" % x[5], "|", "%10s" % x[6])
    except UnboundLocalError:
        pass


def find_staff(m):
    # function to find employee based on name or id
    opt = int(input("Search by : \n1.Name \n2.ID \nEnter Choice :"))

    if opt == 2:
        a = int(input("enter ID : "))
        m.execute(f"select * from employees where ID= {a};")
        myresult = m.fetchall()
    elif opt == 1:
        a = str(input("name : "))
        m.execute(f"select * from employees where name = '{a}';")
        myresult = m.fetchall()
    print("\n \nSearching employee database...")

    for x in myresult:
        print(
            f"\nid :{x[0]}\nname : {x[1]}\nsalary : {x[2]}\nposition : {x[3]}\nphoneNumber : {x[4]}\nstartyear : {x[5]}"
            f"\ndepartment : {x[6]}")


def employee_exists(m, a):
    # function to check if employee exists
    m.execute(f"select * from employees where id = {a}")
    myresult = m.fetchall()
    if myresult:
        return True
    else:
        return False


def remove_staff(m):
    # function to remove employee from database
    a = int(input("id(int) : "))
    if employee_exists(m, a):
        m.execute(f"select * from employees where id = {a}")
        myresult = m.fetchall()
        for x in myresult:
            print(f"\nid :{x[0]}\nname : {x[1]}\nsalary : {x[2]}\nposition : {x[3]}\nphoneNumber : {x[4]}\nstartyear : {x[5]}"
                  f"\ndepartment : {x[6]}")
        b = str(input("Are you sure you want to remove this employee? (y/n) : "))
        if b == "y":
            m.execute(f"delete from employees where id = {a}")
            mydb.commit()
            print("Employee FIRED")
        else:
            print("Employee not removed")
    else:
        print("Employee not found")


start()

while True:
    p = int(input("\n1 : List Of employees\n2 : Register new employee\n3 : Find Employee\n4 : FIRE Employee\n"
                  "5 : Update Details\n6 : Exit\n>>>"))
    if p == 1:
        filteredtable(mycursor)
    elif p == 2:
        new_staff(mycursor)
    elif p == 3:
        find_staff(mycursor)
    elif p == 4:
        remove_staff(mycursor)
        full_table(mycursor)
    elif p == 5:
        edit_details(mycursor)
    elif p == 6:
        print("committing changes")
        mydb.commit()
        print("terminating...")
        mydb.close()
        print("terminated")
        break
    else:
        print("invalid option selected")
