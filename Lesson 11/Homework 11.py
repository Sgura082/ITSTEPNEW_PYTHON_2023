import re
import random

# -----------GLOBAL Variables----------------
global TaskNames
TaskNames = ["Task 1: Creating tuple of numbers raised to power 2",
             "Task 2: Working with tuples"]


# -----------FUNCTIONS----------------
def rand_int_tuple_generator(tuple_length):
    element = (lambda: random.randint(0, 10))
    tuplea = tuple(element() for i in range(0,tuple_length))
    return tuplea


# -----------TASK FUNCTIONS----------------

def Task1():  # For task 1
    print(f"\n{TaskNames[0]}")
    Looper = "y"
    while Looper == "y":
        while True:
            length = input("Please enter the desired length (n) of the "
                           "list(1, 2, 3, .....,n). Elements of which will be raised to power 2 :\n")
            if re.match(r'^([\s\d]+)$', length):
                break
            else:
                print("ERROR Wrong input. Please enter only INT number.")
        squared_numbers = [i ** 2 for i in range(1, int(length) + 1)]
        print(f"List of numbers raised to power 2: {squared_numbers}")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task2():  # For task 2
    print(f"\n{TaskNames[1]}")
    Looper = "y"
    while Looper == "y":
        while True:
            length = input("Please enter the desired length of the tuple :\n")
            if re.match(r'^([\s\d]+)$', length):
                break
            else:
                print("ERROR Wrong input. Please enter only INT number.")
        tuple1 = sorted(rand_int_tuple_generator(int(length)))
        tuple2 = sorted(rand_int_tuple_generator(int(length)))
        print(f"Generated tuple1: {tuple1}")
        print(f"Generated tuple2: {tuple2}")
        combined_tuple = tuple(set(tuple1 + tuple2))
        duplicated_values = sorted(list(set(tuple1).intersection(set(tuple2))))

        print(f"\nCombination of 2 tuples without duplicates: {combined_tuple}")
        print(f"List of elements present in both tuples: {duplicated_values}")
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

print("\n ---THE END---")
