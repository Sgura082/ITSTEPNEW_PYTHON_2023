import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ------------------------------------------------------------------------------TASK DESCRIPTIONS-----------------------
# ------Task1: Working with SQl using psycopg2
# ------Task2: Working with SQl - ORM
# ------Task3:
# ------Task4:
# ------------------------------------------------------------------------------GLOBAL Variables------------------------
global Task_list
Task_list = []


# ------------------------------------------------------------------------------MAIN CLASSES----------------------------
class Task():
    def __init__(self, name):
        assert isinstance(name, str), "'name' must be a string!!!"
        self.Function = object
        Task_list.append(self)
        self.name = f"Task{Task_list.index(self) + 1}: {name}"

    def __str__(self):
        return self.name

    def write_function(self, object101):
        self.Function = object101

    def __call__(self):
        Looper = "y"
        while Looper == "y":
            self.Function()
            Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
            if Replay == "y":
                continue
            else:
                Looper = Replay


# ------------------------------------------------------------------------------CUSTOM FUNCTIONS------------------------

# ------------------------------------------------------------------------------TASK OBJECTS----------------------------
# --------------------------------------------------------------------------------------------------START TASK 1--------
Task01 = Task("Working with SQl using psycopg2")


def task1_body():
    pass
    # ----------------Task Variables----------------------------------
    # ------Connection Setup---------------------------------------------------------------------
    HOST = 'localhost'
    PORT = 5432
    DATABASE = 'Lesson33'
    USER = 'postgres'
    PASSWORD = 'XX132Files'
    conn = psycopg2.connect(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)
    cursor = conn.cursor()

    Query_Send_list = []
    Query_Fetch_list = []

    # ----Query for Department table creation---------------------------------------------------------------
    create_Department_table_query = """
    create table Department(DepartmentID varchar(10) primary key unique, DepartmentName varchar(30))
    """
    Query_Send_list.append(create_Department_table_query)

    # ----Query for Employee table creation---------------------------------------------------------------
    create_Employee_table_query = """
    create table Employee(EmployeeID varchar(10) primary key, Fullname varchar(30),HireDate Timestamp, DepartmentID varchar(10))
    """
    Query_Send_list.append(create_Employee_table_query)

    # ----Query for altering DepartmentID in Employee table so that it becomes a foreign key---------------------------------
    alter_Employee_table_query = """
    alter table Employee add constraint DepartmentIDconst foreign key (DepartmentID) references Department (DepartmentID)
    """
    Query_Send_list.append(alter_Employee_table_query)

    # ----Query for Data input into Department table---------------------------------------------------------------
    insert_Departments_query = """
        insert into Department (DepartmentID, DepartmentName) values ('10001','Management'),('10002','IT'),('10003','Sales')
        """
    Query_Send_list.append(insert_Departments_query)

    # ----Query for Data input into Employee table---------------------------------------------------------------
    insert_Employee_query = """
        insert into Employee(EmployeeID, Fullname ,HireDate , DepartmentID) values ('30001','Saba Gurashvili','16/12/2023','10002'),
        ('30002','George Gergianson','01/01/2021','10001'),('30003','Makhatma Ghlonti','01/04/1991','10001'),
        ('30004','Karl Marx','10/10/1851','10003')
        """
    Query_Send_list.append(insert_Employee_query)

    # ----Query for Fetching all data---------------------------------------------------------------
    Fetch_joined_data_query = """
        select * from employee
        left join department on department.departmentID = Employee.Departmentid
        """
    Query_Fetch_list.append(Fetch_joined_data_query)

    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
    # ----Query Sender---------------------------------------------------------------
    for query in Query_Send_list:
        cursor.execute(query)
        conn.commit()
    # ----Query Fetcher--------------------------------------------------------------
    for query in Query_Fetch_list:
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            print(i)
    cursor.close()
    conn.close()


Task01.write_function(task1_body)
# ----------------------------------------------------------------------------------------------------END TASK 1--------
# --------------------------------------------------------------------------------------------------START TASK 2--------
Task02 = Task("Working with SQl - ORM")


def task2_body():
    pass
    # ----------------Task Variables----------------------------------
    HOST = 'localhost'
    PORT = 5432
    DATABASE = 'Lesson33'
    USER = 'postgres'
    PASSWORD = 'XX132Files'

    database_string = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    engine = create_engine(database_string)
    Base = declarative_base()

    # ----------------Task Classes------------------------------------
    class Department(Base):
        __tablename__ = 'department'
        departmentID = Column('departmentid', String(10), primary_key=True, unique=True)
        departmentName = Column('departmentname', String(30))
        def __str__(self):
            return f"DepartmentID: {self.departmentID} ; DepartmentName: {self.departmentName}"


    class Employee(Base):
        __tablename__ = 'employee'
        employeeID = Column('employeeid', String(10), primary_key=True)
        fullname = Column('fullname', String(30))
        hiredate = Column('hiredate', Date)
        departmentID = Column('departmentid', String(10), ForeignKey('department.departmentID'))
        def __str__(self):
            return f"EmployeeID: {self.employeeID}; Employee Fullname: {self.fullname}; HireDate: {self.hiredate}; DepartmentID: {self.departmentID}"

    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    joinedQ = session.query(
        Employee.employeeID,
        Employee.fullname,
        Employee.hiredate,
        Employee.departmentID,
        Department.departmentName).join(Department, Employee.departmentID==Department.departmentID).all()
    for i in joinedQ:
        print(f"{i}\n-------------------------------------------------------------")



Task02.write_function(task2_body)
# -----------------------------------------------------------------------------------------------------END TASK 2--------
# ------------------------------------------------------------------------------MAIN CODE-------------------------------
for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
