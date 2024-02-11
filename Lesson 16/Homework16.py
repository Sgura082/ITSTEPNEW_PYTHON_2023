import os
import random
import re

# -----------GLOBAL Variables----------------

global TaskNames
TaskNames = {"Task 1": {"Name": "Task 1: OOP- Banking operations",
                        "FunctionId": 0},
             "Task 2": {"Name": "Task 2: x",
                        "FunctionId": 1},
             "Task 3": {"Name": "Task 3: x",
                        "FunctionId": 2},
             "Task 4": {"Name": "Task 4: x",
                        "FunctionId": 3},
             "Task 5": {"Name": "Task 5: x",
                        "FunctionId": 4},
             "Task 6": {"Name": "Task 6: x",
                        "FunctionId": 5},
             "Task 7": {"Name": "Task 7: x",
                        "FunctionId": 6},
             "Task 8": {"Name": "Task 8: x",
                        "FunctionId": 7},
             "Task 9": {"Name": "Task 9: x",
                        "FunctionId": 8},
             "Task 10": {"Name": "Task 10: x",
                         "FunctionId": 9}, }
global Task_function_list
Task_function_list = []


# -----------CUSTOM CLASSES----------------

# -----------CUSTOM FUNCTIONS----------------
def clear_screen():
    os.system("cls")


def user_input_controlled_by_dict(dicta):
    def print_dict():
        lst = []
        for key, value in dicta.items():
            lst.append(f"{key} = {value.get('name')}")
        for i in lst:
            print(i)

    print_dict()
    while True:
        user_input = input("\nChoose the operation from above (type corresponding letter): ")
        if user_input in list(dicta.keys()):
            return user_input
        else:
            print("\nOperation not recognized!! Please Choose from list below")
            print_dict()

def numInput_with_validation():
        while True:
            userNum = input(f"Enter Sum: ")
            if re.match(r'^([\.\d]+)$', userNum):
                if float(userNum) < 0:
                    print("Please enter positive number")
                    continue
                else:
                    break
            else:
                print("ERROR Wrong input. Please enter only INT number.")
        return userNum


# -----------TASK FUNCTIONS----------------
def Task1():  # For task 1
    # ----------------Task Variables----------------------------------
    bank_account_repository = []

    # ----------------Task Classes----------------------------------
    class BankAccount():
        def __init__(self, account_number, account_holder, balance, client_ID):
            assert isinstance(account_number, str), "Account number must be a string!!!"
            assert isinstance(account_holder, str), "Account holder must be a string!!!"
            assert isinstance(balance, float), "The balance must be a float number!!!"
            assert isinstance(client_ID, str), "Account holder must be a string!!!"
            self.account_number = account_number
            self.account_holder = account_holder
            self.balance = balance
            self.client_ID = client_ID

        def get_info(self, inf):
            if inf == "account_number":
                return self.account_number
            elif inf == "account_holder":
                return self.account_holder
            elif inf == "balance":
                return self.balance
            elif inf == "client_ID":
                return self.client_ID
            else:
                return "NO SUCH DATA EXISTS"

        def withdrawing_money(self, money_sum1):
            assert isinstance(money_sum1, float), "The amount of money must be a float number!!!"
            self.balance -= money_sum1
            return (f"\nDear Mr. {self.account_holder} \n"
                    f"${money_sum1} was withdrawn from your account #{self.account_number}.\n"
                    f"Remaining Balance on the account is: ${self.balance}")

        def depositing_money(self, money_sum2):
            assert isinstance(money_sum2, float), "The amount of money must be a float number!!!"
            self.balance += money_sum2
            return (f"\nDear Mr. {self.account_holder} \n"
                    f"${money_sum2} was deposited to your account #{self.account_number}.\n"
                    f"Current Balance on the account is: ${self.balance}")

    # ----------------Task Functions----------------------------------
    def create_account():
        print("-------------\nCreating new Account:")

        user_name = input('Please enter your first name: ')
        user_lastname = input('Please enter your first name: ')
        user_id = input('Please enter your ID number: ')
        client_name = user_name + " " + user_lastname
        client_new_account_number = "GE" + str(random.randint(100000000000000, 999999999999999))
        account = BankAccount(client_new_account_number, client_name, 0.0, user_id)
        bank_account_repository.append(account)
        return (f"\nDear Mr. {client_name} \n "
                f"CONGRADULATIONS!! your new account #{client_new_account_number} has been approved and activated.")

    def open_personal_page():
        client_accounts_lst = []
        client = ""
        client_id = input("Please enter your ID number: ")
        for i in bank_account_repository:
            if i.get_info("client_ID") == client_id:
                client = i.get_info('account_holder')
                client_accounts_lst.append(f"{i.get_info("account_number")} - Balance = {i.get_info("balance")}")
        if client_accounts_lst == []:
            print("Sorry! No accounts have been found for that ID!")
        else:
            print(f"--------------------------------\n"
                  f"Mr. {client}, your accounts:")
            for i in client_accounts_lst:
                print(i)
        print("--------------------------------")

    def deposit():
        while True:
            user_account = input("Enter the account number to which you want to deposit money:\n")
            for i in bank_account_repository:
                if i.get_info("account_number") == user_account:
                    money_sum = numInput_with_validation()
                    return i.depositing_money(float(money_sum))
            print("No such account was found!!")
    def withdraw():
        while True:
            user_account = input("Enter the account number to which you want to deposit money:\n")
            for i in bank_account_repository:
                if i.get_info("account_number") == user_account:
                    money_sum = numInput_with_validation()
                    if i.get_info("balance") >= float(money_sum):
                        return i.withdrawing_money(float(money_sum))
                    else:
                        return "Not enough money on balance"
            print("No such account was found!!")
            user_choice = input("Try again? YES (y) / NO (any other key)")
            if user_choice != 'y':
                break


    # ----------------Task BODY----------------------------------
    acc1 = BankAccount("GE219282766639660","Saba Gurashvili",2500.0,"1234")
    acc2 = BankAccount("GE612389737643965","Saba Gurashvili",256.8,"1234")
    acc3 = BankAccount("GE612384736583961","Giorgi Jgenti",100000.8,"4321")
    bank_account_repository.append(acc1)
    bank_account_repository.append(acc2)
    bank_account_repository.append(acc3)
    Looper = "y"
    while Looper == "y":

        print("---------WELCOME TO TRUSTY BANK!!!----------\n\n")
        operations = {"n": {'name': "Create New account", 'function': create_account},
                      "w": {'name': "Withdraw sum from existing account", 'function': withdraw},
                      "d": {'name': "Deposit money to your account", 'function': deposit},
                      "x": {'name': "EXIT"}}
        while True:
            print("---For Example type: '1234'----")
            open_personal_page()
            user_operation = user_input_controlled_by_dict(operations)
            if user_operation == "x":
                print("-------------Goodbye. HAVE A NICE DAY!!!!!------------")
                break
            print(operations.get(user_operation).get("function")())
            user_input = input("\nContinue? (y) / Exit (any key): \n")
            if user_input != 'y':
                print("-------------Goodbye. HAVE A NICE DAY!!!!!------------")
                break


        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


Task_function_list.append(Task1)


def Task2():  # For task 2
    # ----------------Task Classes----------------------------------
    class Student():
        def __init__(self, name, student_id, courses):
            assert isinstance(name, str), "name must be a string!!!"
            assert isinstance(student_id, str), "student_id must be a string!!!"
            assert isinstance(courses, list), "courses must be a list!!!"
            self.name = name
            self.student_id = student_id
            self.courses = courses
        def get_courses(self):
            return self.courses
        def add_new_course(self,ncourse):
            self.courses.append(ncourse)
        def get_name(self):
            return self.name
        def get_student_id(self):
            return self.student_id
        def print_student_total_info(self):
            print("------------------------------------")
            print(f"Student name is: {self.name}")
            print(f"Student ID is: {self.student_id}")
            print(f"Student is taking Following courses: {self.courses}")
            print("------------------------------------\n")
    # ----------------Task BODY----------------------------------
    Looper = "y"
    while Looper == "y":
        available_courses_lst = ["Python","C++","Juggling","Cooking","Advanced Math","Athletic nut cracking","Joking Professionally"]
        student1 = Student("Saba gurashili", "1234",["Python","Joking Professionally"])
        student2 = Student("George Mozzart", "4567",["C++"])
        Student_lst =[]
        Student_lst.append(student1)
        Student_lst.append(student2)
        User_Student = Student("1","EMPTY",[""])
        while True:
            print('All Student info')
            for i in Student_lst:
                i.print_student_total_info()
            print("---For Example type: '1234'----")
            user_input_id = input("Enter your user ID: ")
            for i in Student_lst:
                if i.get_student_id() == user_input_id:
                    User_Student = i
                    break
            if User_Student.get_student_id() != "EMPTY":
                User_Student.print_student_total_info()
                user_choice = input("Do you want to take another course? YES (y) / NO (any other key): ")
                if user_choice == 'y':
                    for i in range(len(available_courses_lst)):
                        print(f"{i}: {available_courses_lst[i]}")
                    while True:
                        user_course = input("Choose a course from above (pick a number): ")
                        if re.match(r'^([\.\d]+)$', user_course):
                            if int(user_course) <= len(available_courses_lst):
                                if available_courses_lst[int(user_course)] in User_Student.get_courses():
                                    print("You are already on this course!!!")
                                else:
                                    User_Student.add_new_course(available_courses_lst[int(user_course)])
                                    print(f"You have been added to course {available_courses_lst[int(user_course)]}")
                                    break
                            else:
                                print("No such number found!! Choose only from the list")
                exit = input("\nEXIT? YES (y) / NO (Any other key)")
                if exit == "y":
                    break
            else:
                print("No student was found with such ID. Try again")


        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


Task_function_list.append(Task2)

# -------------MAIN CODE---------------------------------------------------------------------
for key, value in TaskNames.items():
    if len(Task_function_list) <= value.get('FunctionId'):
        continue
    else:
        Task_status = input(f"\nDo you want to do - {value.get('Name')}? \n(Enter 'y' for YES or any key for NO) ")
        if Task_status == "y":
            Task_function_list[value.get('FunctionId')]()
        else:
            print(f" \n{value.get('Name')} - Skipped")

print("\n ---THE END---")
