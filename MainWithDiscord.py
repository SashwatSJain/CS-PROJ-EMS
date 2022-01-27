# Employee registration

import mysql.connector
from pprint import pprint
from discord.ext.commands import Bot


# usr = input("username : ")
# pwd = input("password : ")
usr = "root"
pwd = "0000000000"
bot = Bot(command_prefix='.')
TOKEN = "ODcwNTE0ODEyMDA0NzU3NTU2.YQN4GA.bxU1MSSDKmcbcUQ7psksGgv-tYY"

mydb = mysql.connector.connect(
    host="localhost",
    user=usr,
    password=pwd
)

print(mydb)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

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

while True:
    p = int(input("\n1 : List of employees\n2 : register new employee\n3 : find employee with name\n4 : remove\n5 : exit\n6 : DiscordBot\n>>>"))
    if p == 1:
        print(TABLE(mycursor))
    elif p == 2:
        newStaff(mycursor)
    elif p == 3:
        find_staff(mycursor)
    elif p == 4:
        remove_staff(mycursor)
        pprint(TABLE(mycursor))
    elif p == 5:
        print("committing changes")
        mydb.commit()
        print("terminating...")
        mydb.close()
        print("terminated")
        break
    elif p == 6:
        for x in range(1):
            @bot.event
            async def on_message(message):

                if message.content.startswith("help"):
                    await message.channel.send(f"possible commands are list and remove.")

                elif message.content == "list":
                    await message.channel.send(TABLE(mycursor))

                elif message.content.startswith("remove "):
                    mycursor.execute(f"delete from employees where id = {int(message.content[7:])};")
                    mydb.commit()


            bot.run(TOKEN)