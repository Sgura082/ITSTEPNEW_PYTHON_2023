import re

# -----------GLOBAL Variables----------------
global TaskNames
TaskNames = {"Task 1": "Task 1: Counting occurrences of words within users text. (Using dictionary)",
             "Task 2": "Task 2: Making calculator using dictionary"}


# -----------FUNCTIONS----------------

def dictifier(a):
    dict = {}
    lst = a.split()
    for i in lst:
        dict[i] = lst.count(i)
    return dict


def numInput_with_validation(a, opera =""):
    Control_for_zero_division = ["/", "//", "%"]
    while True:
        userNum = input(f"Enter number {a}: ")
        if (opera in Control_for_zero_division) and float(userNum) == 0:
            print("You can't divide by 0. Enter other number!!!")
            continue
        elif re.match(r'^([\.\d]+)$', userNum):
            break
        else:
            print("ERROR Wrong input. Please enter only INT number.")
    return userNum


# -----------TASK FUNCTIONS----------------

def Task1():  # For task 1
    print(f"\n{TaskNames.get("Task 1")}")
    Looper = "y"
    while Looper == "y":
        usertxt = input("Enter a sentence: ")
        print(dictifier(usertxt))
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task2():  # For task 2
    print(f"\n{TaskNames.get("Task 2")}")
    Looper = "y"
    while Looper == "y":
        Calculator = {'+': {"Name": "   Addition", "Formula": lambda x, y: x + y},
                      '-': {"Name": "   Subtraction", "Formula": lambda x, y: x - y},
                      '/': {"Name": "   Division", "Formula": lambda x, y: x / y},
                      '*': {"Name": "   Multiplication", "Formula": lambda x, y: x * y},
                      '//': {"Name": "  Floor division", "Formula": lambda x, y: x // y},
                      '%': {"Name": "   Modulus", "Formula": lambda x, y: x % y},
                      '**': {"Name": "  Exponentiation", "Formula": lambda x, y: x ** y},
                      'root': {"Name": "Getting root", "Formula": lambda x, y: x ** (1 / y)},
                      }
        OperationList = list(Calculator.keys())
        prompt = [" " + i + " " + Calculator.get(i).get("Name") for i in OperationList]
        print("\n------PROMPT LIST------", *prompt, sep="\n")
        while True:
            userOper = input("\nEnter an operation you want to conduct (use prompt above): ")
            if userOper in OperationList:
                break
            else:
                print("No such operation found!!! Check prompt list at the start of program!!")
        userNum1 = float(numInput_with_validation(1))
        userNum2 = float(numInput_with_validation(2, userOper))
        result = Calculator.get(userOper).get("Formula")(userNum1, userNum2)
        print(f"\nResult of calculation: \n{userNum1} {userOper} {userNum2} = {result}")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay

        # -------------MAIN CODE-------------


Task1_status = input(f"\nDo you want to do - {TaskNames.get("Task 1")}? \n(Enter 'y' for YES or any key for NO) ")
if Task1_status == "y":
    Task1()
else:
    print(" \nTask 1 Skipped")
Task2_status = input(f"\nDo you want to do - {TaskNames.get("Task 2")}? \n(Enter 'y' for YES or any key for NO) ")
if Task2_status == "y":
    Task2()
else:
    print(" \nTask 2 Skipped")
print("\n ---THE END---")
