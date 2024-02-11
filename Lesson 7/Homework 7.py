
import re
import random


# -----------FUNCTIONS----------------
def sumList(*args):
    totalSum = 0
    problems = []
    for i in args:
        totalSum += i
    return f"Sum of numbers in list {args} is: {totalSum}"
def sumChar(Num):
    if int(Num) == 0:
        return 0
    return int(Num%10) + sumChar(int(Num/10))

def stringReverser(txt):

    if len(txt) !=0:
        b = txt.split(txt[0],1)[1]
        return stringReverser(b) + txt[0]
    else:
        return ""

def factorial(Number):
    if Number == 1:
        return Number
    else:
        return Number*factorial(Number -1)



# -----------TASK FUNCTIONS----------------
def Task1():  # For task 1
    print("\nTask 1: Summing numbers in a list \n")
    Looper = "y"
    while Looper == "y":

        print(sumList(100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10))

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay

def Task2():  # For task 2
    print("\nTask 2: Summing digits of entered Number: Using Recursion ")
    Looper = "y"
    while Looper == "y":
        inputloop = True
        while inputloop == True:
            userNumber = input("Enter only whole number in order to sum it's digits: ")
            if re.match(r'^\d+$', userNumber):
                print (f"\nSum of digits in {userNumber} is: {sumChar(int(userNumber))}")
                break
            else:
                print("Wrong input. Enter WHOLE NUMBERS ONLY!! Try again:\n")

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task3():  # For task 3
    print("\nTask 3: Reversing entered text: Using Recursion ")
    Looper = "y"
    while Looper == "y":
        usertxt = input("Enter text to reverse it: " )
        print(f"The reversed version of '{usertxt}' is: "
              f"\n'{stringReverser(usertxt)}'")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task4():  # For task 4
    print("\nTask 4: ")
    Looper = "y"

    while Looper == "y":
        inputloop = True
        while inputloop == True:
            userNumber = input("Enter whole positive number to calculate Factorial: ")
            if re.match(r'^\d+$', userNumber):
                print (f"\nFactorial for number '{userNumber}' is {factorial(int(userNumber))}")
                break
            else:
                print("Wrong input. Enter WHOLE NUMBERS ONLY!! Try again:\n")

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay



# -------------MAIN CODE-------------
Task1_status = input("\nDo you want to do Task 1? (Enter 'y' for YES or any key for NO) ")
if Task1_status == "y":
    Task1()
else:
    print(" \nTask 1 Skipped")
Task2_Status = input("\nDo you want to do Task 2? (Enter 'y' for YES or any key for NO) ")
if Task2_Status == "y":
    Task2()
else:
    print(" \nTask 2 Skipped")

Task3_Status = input("\nDo you want to do Task 3? (Enter 'y' for YES or any key for NO) ")
if Task3_Status == "y":
    Task3()
else:
    print(" \nTask 3 Skipped")

Task4_Status = input("\nDo you want to do Task 4? (Enter 'y' for YES or any key for NO) ")
if Task4_Status == "y":
    Task4()
else:
    print(" \nTask 4 Skipped")
print("\n ---THE END---")