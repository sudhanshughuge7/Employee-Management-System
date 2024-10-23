create database employee;
use  employee;
create table employees(e_id int,first_name varchar(100),last_name varchar(200),email varchar(255),phone_no int(10),hiredate date,address varchar(255),department_id int,primary key(e_id));

drop  table employees;
create table employees(e_id int,first_name varchar(100),last_name varchar(200),email varchar(255),phone_no int(10),hiredate date,address varchar(255),department_id int,primary key(e_id));
insert into employees values(102,'sushant','kale','kalesushant45@gmail.com', 1353546650 , '2023-02-12', 'nashik', 2);
INSERT INTO Employees VALUES (101,'John', 'Doe', 'john.doe@example.com', 1234567890, '2023-01-15',  '123 mumbai', 1);
select * from employees;
create table departments(dept_id int , dept_name varchar(200), primary key (dept_id));
insert into departments values(1, 'sales');
insert into departments values(2, 'finance');
select * from departments;
create table Role(role_id int , rolename varchar(200));

drop table role;
create table Role(role_id int , rolename varchar(200),primary key (role_id));
insert into role values(1000,'sales manager');
create table payroll( Payroll_id INT ,e_id INT, MonthYEAR date ,Salary float,Bonus float,Deductions float,primary key(payroll_id),FOREIGN KEY (e_id) REFERENCES employees(e_id));
update employees set address= 'pune' where e_id =102;
select * from employees;
select * from departments;
select * from role;
select * from payroll;
select * from payroll;