import functools
import random
import string

# -----------GLOBAL Variables----------------
global TaskNames
TaskNames = ["Task 1: Combining lists wit ZIP",
             "Task 2: Getting only odd numbers from list of numbers",
             "Task 3: Getting only positive numbers from list of numbers ",
             "Task 4: Checking for palindrome with Lambda",
             "Task 5: Multiplying numbers from list",
             "Task 6: Text filtering from list",]


# -----------FUNCTIONS----------------
def combine(a,b):
    lst = list(zip(a,b))
    return lst

# -----------TASK FUNCTIONS----------------
def Task1():  # For task 1
    print(f"\n{TaskNames[0]}")
    Looper = "y"
    while Looper == "y":
        lst1 = [1,2,3]
        lst2 = ["a","b","c"]
        print(lst1)
        print(lst2)
        print(combine(lst1,lst2))
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task2():  # For task 2
    print(f"\n{TaskNames[1]}")
    Looper = "y"
    while Looper == "y":
        Numbers = [random.randint(0,100) for i in range(0,10)]
        print(f"The number list to filter positive numbers from is:\n"
              f"{Numbers} \n")
        oddnumbers = list(filter(lambda a: a if a%2 != 0 else "" , Numbers))
        print(f"Odd number are: {oddnumbers}")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task3():  # For task 3
    print(f"\n{TaskNames[2]}")
    Looper = "y"
    while Looper == "y":
        numbers = [random.randint(-100,100) for i in range(0,5)]
        print(f"The number list to filter positive numbers from is:\n"
              f"{numbers} \n")
        positiveNums = list(filter(lambda x: x if x > 0 else "",numbers))
        print(f"positive numbers are :{positiveNums}")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task4():  # For task 4
    print(f"\n{TaskNames[3]}")
    Looper = "y"
    while Looper == "y":
        txtlst = ["civic","ABBa","raDar","raceCAR", "Apple", "MOM"]
        print(f"List of texts being checked for palindrome: {txtlst}\n")
        palindromes = list(filter(lambda x: x if x=="".join(reversed(x)) else "",txtlst))
        print(f"Palindromes are: {palindromes}")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task5():  # For task 5
    print(f"\n{TaskNames[4]}")
    Looper = "y"
    while Looper == "y":
        numbers = [random.randint(1,10) for i in range(0,3)]
        #numbers =[1,"g",3] #For testing error
        print(f"The number list to multiply numbers from is:\n"
              f"{numbers} \n")
        try:
            sum = functools.reduce(lambda a, b: a * b +0, numbers)
            print(sum)
        except TypeError:
            print("Incorrect value in list. Can't multiply by string.")

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task6():  # For task 6
    print(f"\n{TaskNames[5]}")
    Looper = "y"
    while Looper == "y":
        lst_txt = ["Ended", "boxing", "kickeD", "saw","painted"]
        #lst_txt = ["Ended",1,2, "boxing", "kickeD", "saw", "painted"] #for chekcing
        ending_txt = "ed"
        try:
            check2 = list(filter(lambda a, b=ending_txt: a if a[len(a)-len(b):]==b else "",lst_txt))
            print (check2)
        except TypeError:
            print("Incorrect type of data in list. Make sure there are only strings!!")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay
 # -------------MAIN CODE-------------
Task1_status = input(f"\nDo you want to do {TaskNames[0]}? \n(Enter 'y' for YES or any key for NO) ")
if Task1_status == "y":
    Task1()
else:
    print(" \nTask 1 Skipped")
Task2_status = input(f"\nDo you want to do {TaskNames[1]}? \n(Enter 'y' for YES or any key for NO) ")
if Task2_status == "y":
    Task2()
else:
    print(" \nTask 2 Skipped")

Task3_status = input(f"\nDo you want to do {TaskNames[2]}? \n(Enter 'y' for YES or any key for NO) ")
if Task3_status == "y":
    Task3()
else:
    print(" \nTask 3 Skipped")

Task4_status = input(f"\nDo you want to do {TaskNames[3]}? \n(Enter 'y' for YES or any key for NO) ")
if Task4_status == "y":
    Task4()
else:
    print(" \nTask 4 Skipped")

Task5_status = input(f"\nDo you want to do {TaskNames[4]}? \n(Enter 'y' for YES or any key for NO) ")
if Task5_status == "y":
    Task5()

else:
    print(" \nTask 5 Skipped")

Task6_status = input(f"\nDo you want to do {TaskNames[5]}? \n(Enter 'y' for YES or any key for NO) ")
if Task6_status == "y":
    Task6()

else:
    print(" \nTask 6 Skipped")

print("\n ---THE END---")