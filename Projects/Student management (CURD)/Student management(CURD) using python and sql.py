import mysql.connector
from tabulate import tabulate 
con = mysql.connector.connect(host = "localhost", user = "root", password = "2002", database = "student_db")

def insert(Name, Class, Mark):
    cur = con.cursor()
    quary = "INSERT INTO PRIMARY_DATA(NAME, CLASS, MARK) VALUES (%s,%s,%s)"
    values = (Name, Class, Mark)
    cur.execute(quary, values)
    con.commit()
    
def update(Name, Class, Mark, Id):
    cur = con.cursor()
    quary = "UPDATE PRIMARY_DATA SET NAME = %s, CLASS = %s, MARK = %s WHERE ID = %s"
    values = (Name, Class, Mark, Id)
    cur.execute(quary, values)
    con.commit()

def select():
    cur = con.cursor()
    quary = "SELECT ID, NAME, CLASS, MARK FROM PRIMARY_DATA"
    cur.execute(quary)
    result = cur.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "CLASS", "MARK"]))
 
def delete(id):
    cur = con.cursor()
    quary = "DELETE FROM PRIMARY_DATA WHERE ID = %s"
    values = (id,)
    cur.execute(quary, values)
    con.commit()

while True:
    print("1. Insert data")
    print("2. Update data")
    print("3. Select data")
    print("4. Delete data")
    print("5. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        Name = input("\nEnter the Name : ")
        Class = input ("Enter the Class : ")
        Mark = input("Enter the Mark : ")
        insert(Name, Class, Mark)
        print("\nData Inserted Successfully")
    elif choice == 2:
        Id = int(input("\nEnter the ID number you want to update :"))
        Name = input("Enter the Name : ")
        Class = input ("Enter the Class : ")
        Mark = input("Enter the Mark : ")
        update(Name, Class, Mark, Id)
        print("\nData updated Successfully")
    elif choice == 3:
        select()
        print("\nData selected Succesfully")
    elif choice == 4:
        Id = int(input("\nEnter the ID : "))
        delete(Id)
        print("\nData Deleted Succesfully")
    elif choice == 5:
        break
    else :
        print("\nInvalid option. Enter Valid option : ")

