import streamlit as st
import pandas as pd
import mysql.connector
import datetime
st.title("employee management system")
choice=st.sidebar.selectbox("My menu",("Home", "Employee","Admin",))
if(choice=="Home"):
  st.image("https://p7.hiclipart.com/preview/373/160/931/human-resource-management-system-time-and-attendance-service-employees-international-union.jpg")
elif(choice=="Employee"):
  btn2=st.button("Temporary")
  if 'login' not in st.session_state:
      st.session_state['login']=False
  uid=st.text_input("Enter User ID")
  upwd=st.text_input("Enter password")
  btn=st.button("Login")
  if btn:
      mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
      c=mydb.cursor()
      c.execute("select * from emplogin")
      for r in c:
          if(r[0]==uid and r[1]==upwd):
              st.session_state['login']=True
              break
      if(not st.session_state['login']):
          st.write("Incorrect ID or Password")
  if(st.session_state['login']):
      st.write("Login successfull")
      choice2=st.selectbox("Features",("none","view all employees","view a specific employee","view a total count of employees"))
      if(choice2=="view all employees"):
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
        df=pd.read_sql("select * from employees",mydb)
        st.dataframe(df)
      elif(choice2=="view a specific employee"):
       emp_id = st.text_input("Enter Employee ID")
       if st.button("View Employee"):
         mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="employee")
         c = mydb.cursor()
         query = "SELECT * FROM employees WHERE e_id = %s"
         c.execute(query, (emp_id,))
         result=c.fetchone()

         if result:
           employee_info={"Employee ID": result[0],"FirstName":result[1], "Last Name": result[2],"Email": result[3],"Phone Number": result[4],"Hire Date": result[5],
                          "Address": result[6],"Department ID": result[7],}
           st.write(employee_info)
         else:
           st.write("No employee found with the given ID.")
      elif(choice2=="view a total count of employees"):
         mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
         cursor = mydb.cursor()
         cursor.execute("SELECT COUNT(*) FROM employees")
         employee_count = cursor.fetchone()[0]
         st.write(f"Total number of employees: {employee_count}")
         cursor.close()
         mydb.close()
      
         
  st.write(st.session_state['login'])

           
elif(choice=="Admin"):
   if 'alogin' not in st.session_state:
      st.session_state['alogin']=False
   aid=st.text_input("Enter Admin ID")
   apwd=st.text_input("Enter password")
   btn=st.button("Login")
   if btn:
      mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
      c=mydb.cursor()
      c.execute("select * from admins")
      for r in c:
          if(r[0]==aid and r[1]==apwd):
              st.session_state['alogin']=True
              break
      if(not st.session_state['alogin']):
          st.write("Incorrect ID or Password")
   if(st.session_state['alogin']):
      st.write("Login successfull")
      choice2=st.selectbox("Features",("none","view all employees","add employee", "delete employees","payroll","Attendance","Employee performance"))
      if(choice2=="view all employees"):
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
        df=pd.read_sql("select * from employees",mydb)
        st.dataframe(df)
      elif(choice2=="add employee"):
       e_id = st.text_input("Enter Employee ID")
       first_name=st.text_input("enter first name")
       last_name=st.text_input("enter last name")
       email=st.text_input("enter email id")
       phone_no=st.text_input("enter a phone number")
       hiredate=st.text_input("enter a hiredate")or None
       address=st.text_input("enter address")or None
       department_id=st.text_input("enter a department id")
       if st.button("add and View Employee"):
         mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="employee")
         c = mydb.cursor()
         query = "Insert into employees (e_id,first_name,last_name,email,phone_no,hiredate,address,department_id)values (%s, %s, %s ,%s ,%s, %s ,%s, %s)"
         c.execute(query, (e_id,first_name,last_name,email,phone_no,hiredate,address,department_id))
         mydb.commit()
         st.header("Employee added succesfully")
         c.execute("select * from employees where e_id=%s",(e_id),)
         result=c.fetchone()
         st.write(result)
         c.close()
         mydb.close()

      elif(choice2 == "delete employees"):
       e_id = (st.text_input("Enter Employee ID to delete"))
       if st.button("Delete Employee"):
        mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="employee")
        c = mydb.cursor()
        c.execute("SELECT * FROM employees WHERE e_id = %s", (e_id,))
        result = c.fetchone() 
        if result:
            query = "DELETE FROM employees WHERE e_id = %s"
            c.execute(query, (e_id,))
            mydb.commit()
            st.header("Employee deleted successfully!")
        else:
            st.write("Error: Employee with ID {} does not exist.".format(e_id))



      elif(choice2 == "payroll"):
       
       if st.button("check the payroll"):
        mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="employee")
        df=pd.read_sql("SELECT Payroll_id AS 'Payroll ID', e_id AS 'Employee ID', MonthYEAR AS 'Month & Year', Salary AS 'Salary ($)',Bonus AS 'Bonus ($)', Deductions AS 'Deductions ($)' FROM payroll",mydb)
        st.dataframe(df)

      elif(choice2=="Attendance"):
         if st.button("check the attendance"):
          mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="employee")
          df=pd.read_sql("SELECT attendance_id AS 'ATTENDANCE ID', e_id AS 'Employee ID', MonthYEAR AS 'Month & Year', remark AS 'REMARK'from attendance",mydb)
          st.dataframe(df)  

      elif(choice2=="Employee performance"):
         if st.button("check the performance"):
          mydb = mysql.connector.connect(host="localhost", user="root", password="12345678", database="employee")
          df=pd.read_sql("SELECT Performance_id AS 'PERFORMANCE ID', e_id AS 'Employee ID',  Review_date AS 'REVIEW DATE', rating AS 'RATING',comments AS 'COMMENTS'from employeeperformance",mydb)
          st.dataframe(df) 
   st.write(st.session_state['alogin'])


  
  
