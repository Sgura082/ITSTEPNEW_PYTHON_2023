import psycopg2
HOST = 'localhost'
PORT = 5432
DATABASE = 'Lesson33'
USER = 'postgres'
PASSWORD = 'XX132Files'

conn = psycopg2.connect(host=HOST,port=PORT,database=DATABASE,user=USER,password=PASSWORD)
cursor = conn.cursor()

Query_Send_list =[]
Query_Fetch_list = []
#----Query for Department table creation---------------------------------------------------------------
create_Department_table_query = """
create table Department(DepartmentID varchar(10) unique, DepartmentName varchar(30))
"""
Query_Send_list.append(create_Department_table_query)


#----Query for Employee table creation---------------------------------------------------------------
create_Employee_table_query = """
create table Employee(EmployeeID varchar(10), Fullname varchar(30),HireDate Timestamp, DepartmentID varchar(10))
"""
Query_Send_list.append(create_Employee_table_query)

#----Query for altering DepartmentID in Employee table so that it becomes a foreign key---------------------------------
alter_Employee_table_query = """
alter table Employee add constraint DepartmentIDconst foreign key (DepartmentID) references Department (DepartmentID)
"""
Query_Send_list.append(alter_Employee_table_query)

#----Query for Data input into Department table---------------------------------------------------------------
insert_Departments_query = """
    insert into Department (DepartmentID, DepartmentName) values ('10001','Management'),('10002','IT'),('10003','Sales')
    """
Query_Send_list.append(insert_Departments_query)

#----Query for Data input into Employee table---------------------------------------------------------------
insert_Employee_query = """
    insert into Employee(EmployeeID, Fullname ,HireDate , DepartmentID) values ('30001','Saba Gurashvili','16/12/2023','10002'),
    ('30002','George Gergianson','01/01/2021','10001'),('30003','Makhatma Ghlonti','01/04/1991','10001'),
    ('30004','Karl Marx','10/10/1851','10003')
    """
Query_Send_list.append(insert_Employee_query)

#----Query for Fetching all data---------------------------------------------------------------
Fetch_joined_data_query = """
    select * from employee
    left join department on department.departmentID = Employee.Departmentid
    """
Query_Fetch_list.append(Fetch_joined_data_query)

#----Query Sender---------------------------------------------------------------
for query in Query_Send_list:
    cursor.execute(query)
    conn.commit()
cursor.close()
conn.close()

#----Query Fetcher--------------------------------------------------------------
for query in Query_Fetch_list:
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i)
cursor.close()