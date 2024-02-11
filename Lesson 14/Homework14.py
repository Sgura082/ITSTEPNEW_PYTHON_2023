import csv
import pandas as pd

# -----------GLOBAL Variables----------------
global TaskNames
TaskNames = {"Task 1": "Task 1: List of Titanic survivors",
             "Task 2": "Task 2: Filtering Companies with HTTPS",
             "Task 3": "Task 3: Sorting CSV file data and storing it in another file",
             }


# -----------GLOBAL FUNCTIONS----------------

# -----------TASK FUNCTIONS----------------

def Task1():  # For task 1
    print(f"\n{TaskNames.get('Task 1')}")
    Looper = "y"
    while Looper == "y":
        with open("titanic.csv", "r") as titanic_passengers:
            passenger_dict = csv.DictReader(titanic_passengers)
            Survivors_data_list = []
            for passenger in passenger_dict:
                if int(passenger['Survived']) == 1:
                    Survivors_data_list.append(passenger)
        with open("survived.csv", "w", newline="") as survived:
            header_lst = list(Survivors_data_list[0].keys())
            writing = csv.DictWriter(survived, fieldnames=header_lst)
            writing.writeheader()
            for i in Survivors_data_list:
                writing.writerow(i)
        print("\nFile 'survived.csv' was created in project folder!!!! Which contains list of Titanic survivors.")

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task2():  # For task 2
    print(f"\n{TaskNames.get('Task 2')}")
    Looper = "y"
    while Looper == "y":
        header_lst_ssl_comp = ['Organization Id', 'Name', 'Website', 'Industry', 'Number of employees']
        ssl_companies_data_list = []
        with open("organizations-100.csv", "r") as organizations:
            reader = csv.DictReader(organizations)
            for company in reader:
                if "https" in company['Website']:
                    for i in list(company.keys()):
                        if i not in header_lst_ssl_comp:
                            company.pop(i)
                    ssl_companies_data_list.append(company)
        with open("ssl_companies.csv", "w", newline="") as ssl_comp:
            writer = csv.DictWriter(ssl_comp, fieldnames=header_lst_ssl_comp)
            writer.writeheader()
            for company in ssl_companies_data_list:
                writer.writerow(company)
        print(
            "\nFile 'ssl_companies.csv' was created in project folder!!!! which contains list of companies with HTTPS websites")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay

a = 1233

def Task3():  # For task 3
    print(f"\n{TaskNames.get('Task 3')}")
    Looper = "y"
    while Looper == "y":
        dataframe = pd.read_csv("organizations-100.csv")
        sorted = dataframe.sort_values(by = ['Number of employees'])
        sorted.to_csv('sorted_csv.csv',index = False)
        print("\nFile 'sorted_csv.csv' was created in project folder!!!! which contains list of companies sorted by their 'Nubmer of employees'.")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay

        # -------------MAIN CODE-------------


Task1_status = input(f"\nDo you want to do {TaskNames.get('Task 1')}? \n(Enter 'y' for YES or any key for NO) ")
if Task1_status == "y":
    Task1()
else:
    print(" \nTask 1 Skipped")
Task2_status = input(f"\nDo you want to do {TaskNames.get('Task 2')}? \n(Enter 'y' for YES or any key for NO) ")
if Task2_status == "y":
    Task2()
else:
    print(" \nTask 2 Skipped")

Task3_status = input(f"\nDo you want to do {TaskNames.get('Task 3')}? \n(Enter 'y' for YES or any key for NO) ")
if Task3_status == "y":
    Task3()
else:
    print(" \nTask 3 Skipped")

print("\n ---THE END---")