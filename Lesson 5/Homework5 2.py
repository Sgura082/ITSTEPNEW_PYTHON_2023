# -----------FUNCTIONS----------------
import re
import random
def Task1():  # For task 1
    print("\nTask 1: Summing particular elements of an array\n")
    Looper = "y"

    mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]
    ArrayElement1_order = 2
    ArrayElement2_order = 8
    ArrayElement3_order = 13
    sumTotal = mylist[ArrayElement1_order] + mylist[ArrayElement2_order] + mylist[ArrayElement3_order]
    print(sumTotal)



def Task2():  # For task 2
    print("\nTask 2: Creation of new array and printing elements with Min-Max values")
    Looper = "y"
    while Looper == "y":

        validation = False  #For user input validation (only positive numbers)
        GeneratedList = []
        while validation == False :
            listLength = input("\nEnter the length of a list you wish to create. "
                                   "Enter only positive int number :") #For custom list generation
            if listLength.isdigit() and int(listLength) > 0:
                listLength = int(listLength)
                break
            else:
                print("\nPlease enter valid number (positive integer)")
        for i in range (0,listLength):
            GeneratedList.append(random.randint(1,100))
        print(f"\nYou generated list is {GeneratedList}")
        print(f"The highest number in your list is :{max(GeneratedList)}")
        print(f"The lowest number in your list is :{min(GeneratedList)}")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay
def Task3():  # For task 3
    print("\nTask 3: Working with lists ")
    Looper = "y"
    while Looper == "y":
        my_llist = [43,'22',12,66,210,["hi"]]
        print(f"210's index in the list is: {my_llist.index(210)}")
        my_llist.append("hello")
        my_llist.pop(2)
        print(f"After removing element with index 2 the list is: {my_llist}")
        my_llist2 = my_llist.copy()
        my_llist2 = []
        print(f"my_llist  is: {my_llist} \nmy_llist2 is: {my_llist2}")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task4():  # For task 4
    print("\nTask 4: Summing 2 Matrixes")
    Looper = "y"
    while Looper == "y":
        matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix2 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
        matrix3 = []
        for a in range(0, len(matrix1)):
            list_matrix3 = []
            for b in range(0, len(matrix1[a])):
                list_matrix3.append(matrix1[a][b] + matrix2[a][b])
            matrix3.append(list_matrix3)
        print(matrix3)
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task5():  # For task 5
    print("\nTask 5: ")
    Looper = "y"
    while Looper == "y":
        matrixRaw = [[1,2,3],[4,5,6],[7,8,9]]
        print(f"Original matrix:   {matrixRaw}")
        matrixTrans = []
        matrixTransList =[]
        for a in range(0, len(matrixRaw)):
            for b in range(0, len(matrixRaw[a])):
                matrixTransList.append(matrixRaw[b][a])
            matrixTrans.append(matrixTransList)
            matrixTransList = []

        print(f"Transposed matrix: {matrixTrans}")
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

Task5_Status = input("\nDo you want to do Task 5? (Enter 'y' for YES or any key for NO) ")
if Task5_Status == "y":
    Task5()
else:
    print(" \nTask 5 Skipped")
print("\n ---THE END---")