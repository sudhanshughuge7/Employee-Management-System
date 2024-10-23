import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="employee"
)
print(mydb)

e_id = input("Enter employee ID: ")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
email = input("Enter email id: ")
phone_no = input("Enter phone number: ")
hiredate = input("Enter hire date (YYYY-MM-DD): ")
address = input("Enter address: ")
department_id = input("Enter department id: ")

c = mydb.cursor()
c.execute("INSERT INTO employees (e_id, first_name, last_name, email, phone_no, hiredate, address, department_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
          (e_id, first_name, last_name, email, phone_no, hiredate, address, department_id))
mydb.commit()
print("Employee added successfully")
c2 = mydb.cursor()
c2.execute("select * from employees")
