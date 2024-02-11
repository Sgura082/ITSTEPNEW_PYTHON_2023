import random


# -----------FUNCTIONS----------------

def Task1():  # For task 1
    print("\nTask 1: Printing reverse sequence (towards 0) for a number\n")
    UserNumber = int(input("Enter integer number (Do not enter 0): "))
    while UserNumber != 0:
        print(UserNumber, end=", ")
        if UserNumber > 0:
            UserNumber -= 1
        else:
            UserNumber += 1


def Task2():  # For task 2
    print("\nTask 2: Summing user numbers")
    TotalSum = 0
    TotalCount = 0
    EnteredNumbers = ""

    while True:
        print(f"Numbers entered thus far ({EnteredNumbers})")
        User_input = input("\nEnter Number to add to the summing data  \nor enter word 'sum' to calculate the Sum: ")
        if User_input == "sum":
            print(f"\nYou have entered {TotalCount} numbers in total. Numbers entered ({EnteredNumbers})")
            print("\nThe sum of all numbers entered is: ", TotalSum)
            break
        elif int(User_input) > 0:
            TotalSum += int(User_input)
            TotalCount += 1
            EnteredNumbers += User_input + " ,"
        elif int(User_input) <= 0:
            print("\nNegative numbers can't be summed. Enter the positive number")
        else:
            print("\nErorr!! Command not found!")


def Task3():  # For task 3
    print("\nTask 3: Guessing Game\n")
    while True:
        Difficulty = int(input("Choose level of difficulty:"
                               "\n1=easy (number between 1-10, 5 lives)"
                               "\n2=medium (number between 1-10, 3 lives)"
                               "\n3=insane (number between 1-100, 5 lives)"
                               "\n4=god (number between 1-100, 3 lives)\nCHOOSE:  "
                               ))

        if Difficulty == 1:
            NumberLength = 10
            Life = 5
            print("\n-----------EASY-----------")
            break
        elif Difficulty == 2:
            NumberLength = 10
            Life = 3
            print("\n-----------MEDIUM-----------")
            break
        elif Difficulty == 3:
            NumberLength = 100
            Life = 5
            print("\n-----------INSANE-----------")
            break
        elif Difficulty == 4:
            NumberLength = 100
            Life = 3
            print("\n-----------GOD-----------")
            break
        else:
            print("\nEnter Correct difficulty 1 or 2 or 3 or 4\n")
    Number_to_guess = random.randint(1, NumberLength)
    message = ""
    while Life != 0:

        print("-----------------------LIVES LEFT-----------------------")
        print("   0 0 " * Life)
        print("  00000" * Life)
        print("   000 " * Life)
        print("    0  " * Life)
        print("---------------------------------------------------------")
        print(message)
        User_guess = int(input(f"Guess the number between 0-{NumberLength} : "))
        if User_guess == Number_to_guess:
            print ( "\n CONGRATS!! YOU WON!!!")
            break
        elif User_guess < Number_to_guess:
            message = "\nWRONG GUESS. Go HIGHER"
            Life -= 1
        elif User_guess > Number_to_guess:
            message =  "\nWRONG GUESS. Go LOWER"
            Life -= 1
    else:
            print("\nYOU LOOSE!!!")
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
Task3_status = input("\nDo you want to do Task 3? (Enter 'y' for YES or any key for NO) ")
if Task3_status == "y":
    Task3()
else:
    print(" \nTask 3 Skipped")

print("\n ---THE END---")
