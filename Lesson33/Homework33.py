import psycopg2

HOST = 'localhost'
PORT = 5432
DATABASE = 'Lesson33'
USER = 'postgres'
PASSWORD = 'XX132Files'

conn = psycopg2.connect(host=HOST,port=PORT,database=DATABASE,user=USER,password=PASSWORD)
cursor = conn.cursor()

Query_list =[]
#----Query for Department table creation---------------------------------------------------------------
create_Department_table_query = """
create table Department(DepartmentID varchar(10), DepartmentName varchar(30))
"""
Query_list.append(create_Department_table_query)


#----Query for Employee table creation---------------------------------------------------------------
create_Employee_table_query = """
create table Employee(EmployeeID varchar(10), Fullname varchar(30),HireDate timestamp, DepartmentID varchar(10)
"""
Query_list.append(create_Employee_table_query)

#----Query for altering DepartmentID in Employee table so that it becomes a foreign key---------------------------------
alter_Employee_table_query = """
alter table Employee add constraint DepartmentIDconst foreign key (DepartmentID) references Departments (DepartmentID)
"""
Query_list.append(alter_Employee_table_query)

#----Query for Data input into Department table---------------------------------------------------------------
# insert_query = """
#     insert into customers(customerid, surname, firstname, city) values (
#         '10000011','Frank', 'Sinatra','ny')"""
# cursor.execute(insert_query )
# conn.commit()
# cursor.close()
# conn.close()

#----Query Sender---------------------------------------------------------------
for query in Query_list:
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()