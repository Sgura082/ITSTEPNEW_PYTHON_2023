
# -----------GLOBAL Variables----------------
global TaskNames
TaskNames = {"Task 1": "Task 1: x",
             "Task 2": "Task 2: x",
             "Task 3": "Task 3: x",
             "Task 4": "Task 4: x",
             "Task 5": "Task 5: x",
             "Task 6": "Task 6: x",
             "Task 7": "Task 7: x",
             "Task 8": "Task 8: x",
             "Task 9": "Task 9: x",
             "Task 10": "Task 10: x",
             }


# -----------GLOBAL FUNCTIONS----------------

# -----------TASK FUNCTIONS----------------

def Task1():  # For task 1
    print(f"\n{TaskNames.get('Task 1')}")
    Looper = "y"
    while Looper == "y":

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task2():  # For task 2
    print(f"\n{TaskNames.get('Task 2')}")
    Looper = "y"
    while Looper == "y":

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task3():  # For task 3
    print(f"\n{TaskNames.get('Task 3')}")
    Looper = "y"
    while Looper == "y":

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay
def Task4():  # For task 4
    print(f"\n{TaskNames.get('Task 4')}")
    Looper = "y"
    while Looper == "y":

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task5():  # For task 5
    print(f"\n{TaskNames.get('Task 5')}")
    Looper = "y"
    while Looper == "y":

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task6():  # For task 6
    print(f"\n{TaskNames.get('Task 6')}")
    Looper = "y"
    while Looper == "y":

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task7():  # For task 7
    print(f"\n{TaskNames.get('Task 7')}")
    Looper = "y"
    while Looper == "y":

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task8():  # For task 8
    print(f"\n{TaskNames.get('Task 8')}")
    Looper = "y"
    while Looper == "y":

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task9():  # For task 9
    print(f"\n{TaskNames.get('Task 9')}")
    Looper = "y"
    while Looper == "y":

        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task10():  # For task 10
    print(f"\n{TaskNames.get('Task 10')}")
    Looper = "y"
    while Looper == "y":

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

Task4_status = input(f"\nDo you want to do {TaskNames.get('Task 4')}? \n(Enter 'y' for YES or any key for NO) ")
if Task4_status == "y":
    Task4()
else:
    print(" \nTask 4 Skipped")

Task5_status = input(f"\nDo you want to do {TaskNames.get('Task 5')}? \n(Enter 'y' for YES or any key for NO) ")
if Task5_status == "y":
    Task5()

else:
    print(" \nTask 5 Skipped")

Task6_status = input(f"\nDo you want to do {TaskNames.get('Task 6')}? \n(Enter 'y' for YES or any key for NO) ")
if Task6_status == "y":
    Task6()

else:
    print(" \nTask 6 Skipped")

Task7_status = input(f"\nDo you want to do {TaskNames.get('Task 7')}? \n(Enter 'y' for YES or any key for NO) ")
if Task7_status == "y":
    Task7()

else:
    print(" \nTask 7 Skipped")

Task8_status = input(f"\nDo you want to do {TaskNames.get('Task 8')}? \n(Enter 'y' for YES or any key for NO) ")
if Task8_status == "y":
    Task8()

else:
    print(" \nTask 8 Skipped")

Task9_status = input(f"\nDo you want to do {TaskNames.get('Task 9')}? \n(Enter 'y' for YES or any key for NO) ")
if Task9_status == "y":
    Task9()

else:
    print(" \nTask 9 Skipped")

Task10_status = input(f"\nDo you want to do {TaskNames.get('Task 10')}? \n(Enter 'y' for YES or any key for NO) ")
if Task10_status == "y":
    Task10()

else:
    print(" \nTask 10 Skipped")
print("\n ---THE END---")