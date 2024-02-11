import string
import random

# -----------GLOBAL Variables----------------
global TaskNames
TaskNames = ["Task 1: Sorting random list by existing methods and functions",
             "Task 2: Sorting random list by custom written function."]


# -----------FUNCTIONS----------------
def rand_list_generator(list_length, Element_Type):
    lst = []
    element = ""
    if Element_Type == "str":
        element = (lambda: random.choice(string.ascii_letters))
    elif Element_Type == "int":
        element = (lambda: random.choice(string.digits))
    else:
        print("Type of element not recognized. Enter only 'str' or 'int'.")
    for i in range(list_length):
        lst.append(element())
    return lst

def QUICKsorter_DES(list1): #QUICK sort
    if len(list1)>1:
        pivot_index = len(list1) // 2
        pivot_value = list1[pivot_index]
        lst_left = [i for i in list1 if i > pivot_value]
        lst_middle = [i for i in list1 if i == pivot_value]
        lst_right = [i for i in list1 if i < pivot_value]
        result = QUICKsorter_DES(lst_left) + lst_middle + QUICKsorter_DES(lst_right)
        return result
    else:
        return list1


def BUBBLEsorter_ASC(list1): #BUBBLE sort
    was_sorted = False
    for a in range(0,len(list1)-1):
        for b in range(0,len(list1)-1-a):
            if list1[b] > list1[b+1]:
                was_sorted = True
                list1[b] , list1[b+1] = list1[b+1] , list1[b]
        if was_sorted == False:
            return


# -----------TASK FUNCTIONS----------------

def Task1():  # For task 1
    print(f"\n{TaskNames[0]}")
    Looper = "y"
    while Looper == "y":
        while True:
            type_of_list = input("Please enter either 'int' or 'str' to generate a random list "
                             "consisting of either digits or strings:\n")
            if type_of_list == "int" or type_of_list == "str":
                break
            else:
                print("Wrong type entered. Enter only 'str' or 'int'.\n")
        rand_lst = rand_list_generator(100,type_of_list)
        print(f"Generated list: {rand_lst}")
        print("\nUsing 'sorted' function: ")
        print(f"\nList sorted (Ascending): {sorted(rand_lst)}")
        print(f"\nList sorted (Descending): {sorted(rand_lst,reverse = True)}")
        print("---------------------------------------------------------------------------")
        print("\nUsing 'sort' method: ")
        rand_lst.sort()
        print(f"\nList sorted (Ascending): {rand_lst}")
        rand_lst.sort(reverse=True)
        print(f"\nList sorted (Descending): {rand_lst}")
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
            type_of_list = input("Please enter either 'int' or 'str' to generate a random list "
                             "consisting of either digits or strings:\n")
            if type_of_list == "int" or type_of_list == "str":
                break
            else:
                print("Wrong type entered. Enter only 'str' or 'int'.\n")
        rand_lst = rand_list_generator(100, type_of_list)
        print(f"Generated list: {rand_lst}")
        BUBBLEsorter_ASC(rand_lst)
        print(f"\nList sorted (Ascending): {rand_lst}")
        sorted_lst = QUICKsorter_DES(rand_lst)
        print(f"\nList sorted (Descending): {sorted_lst}")
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