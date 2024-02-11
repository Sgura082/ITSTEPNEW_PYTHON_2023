import string
import random

# -----------GLOBAL Variables----------------
global TaskNames
TaskNames = ["Task 1: Linear searching in random list",
             "Task 2: Sorting random list by custom written function."]


# -----------FUNCTIONS----------------
def rand_int_list_generator(list_length):
    lst = []
    element = (lambda: random.randint(0,100))
    for i in range(list_length):
        lst.append(int(element()))
    return lst


def Linear_Search(list, searched_element):  # Linear Search
    for i in list:
        if i == searched_element:
            return f"Index of searched element is: {list.index(i)}"
    return "Your input wasn't found in list"


def Binary_Search(list, searched_element):  # Binary Search
    low = 0
    high = len(list)-1
    while low<=high:
        middle = (high + low) //2
        if searched_element == list[middle]:
            return f"Index of searched element is: {middle}"
        if searched_element > list[middle]:
            low = middle + 1
        if searched_element < list[middle]:
            high = middle -1
    return "Your input wasn't found in list"



def Merge_Sort(list1):  # MERGE sort
    if len(list1) < 2:
        return list1
    index_mid = len(list1) // 2
    return merger(Left=Merge_Sort(list1[:index_mid]), Right=Merge_Sort(list1[index_mid:]))


def merger(Left, Right):  # For Merge sorting
    if len(Left) == 0:
        return Right
    if len(Right) == 0:
        return Left
    res = []
    index_left = index_right = 0
    while len(res) < len(Left) + len(Right):
        if Left[index_left] <= Right[index_right]:
            res.append(Left[index_left])
            index_left += 1
        else:
            res.append(Right[index_right])
            index_right += 1
        if index_left == len(Left):
            res += Right[index_right:]
            break
        if index_right == len(Right):
            res += Left[index_left:]
            break
    return res

def indexer(list, lamb):
    indx_lst = []
    for i in range(len(list)):
        if lamb(list[i]) != "X":
            indx_lst.append(i)
    return indx_lst

# -----------TASK FUNCTIONS----------------

def Task1():  # For task 1
    print(f"\n{TaskNames[0]}")
    Looper = "y"
    while Looper == "y":
        rand_lst = rand_int_list_generator(100)
        print(f"Generated list: {rand_lst}\n")
        print("LINEAR SEARCH\n_______________________________________________________________")
        searched_element = input("Enter int number to search in randomly generated list:\n")
        print(Linear_Search(rand_lst, int(searched_element)))
        print("Binary SEARCH\n_______________________________________________________________")
        sorted_lst = Merge_Sort(rand_lst)
        print(f"Sorted (merge sorting) list: {sorted_lst}\n")
        searched_element = input("Enter int number to search in randomly generated list:\n")
        print(Binary_Search(sorted_lst, int(searched_element)))
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task2():  # For task 2
    print(f"\n{TaskNames[1]}")
    Looper = "y"
    while Looper == "y":
        lamb = lambda a: a if a!=0 and (a % 3) == 0 else "X"
        lst = rand_int_list_generator(100)
        print(f"Randomly generated list:\n{lst}\n")
        print(f"Indexes of elements divisible by 3 in list above: \n{indexer(lst,lamb)}")
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
