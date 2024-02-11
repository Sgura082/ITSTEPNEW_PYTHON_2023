
import re
import random

# -----------FUNCTIONS----------------
def anagram_Check(a,b):
    lista = [ i for i in a]
    listb = [ i for i in b]
    lista.sort()
    listb.sort()
    print(lista)
    print(listb)
    if lista == listb:
        return print("These two strings are anagrams")
    else:
        return print("These two strings are NOT anagrams")
def symbol_count(texta,symbol):
    symb_count = str(texta).count(symbol)
    return f"The '{symbol}' count in your text is {symb_count}"
def fibonacci_generator(a):
    FibList = [0,1]
    for i in range(1,a):
        FibList.append(FibList[i] + FibList[i-1])
    return FibList[:a]



def Task1():  # For task 1
    print("\nTask 1: Checking if two strings entered by user are anagrams. "
          "\nაქ დავალებაში მგონი გამორჩენილი იყო რომ ორი სტრინგის შეყვანა არის საჭირო იმისათვის რომ"
          "\nერთი მხოლოდ ერთი სტრინგი შემოწმდეს მაშინ სიტყვების ბაზა უნდა გვქონდეს რომლებსაც"
          "\nშეადარებს პროგრამა\n")
    Looper = "y"
    while Looper == "y":
        User_text1 = input("Enter text 1: ")
        User_text2 = input("Enter text 2: ")
        anagram_Check(User_text1 , User_text2)
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay

def Task2():  # For task 2
    print("\nTask 2: Counting how many times the symbol is repeated within string")
    Looper = "y"
    while Looper == "y":
        UserText = input("\nEnter any text: ")
        UserSymbol =""
        while len(UserSymbol) != 1:
            UserSymbol = input("\nEnter any character/symbol to count how many times it is used in your text: ")
            if len(UserSymbol) != 1:
                print("\nWrong input!!!. Enter ONLY 1 character")
        print(symbol_count(UserText,UserSymbol))
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay
def Task3():  # For task 3
    print("\nTask 3: Generate fibonacci sequence with length entered by user")
    Looper = "y"
    while Looper == "y":
        ValidInput = False
        while ValidInput != True:
            UserNumber = input("\nEnter the whole number to display that amount elements of fibonacci sequence: ")
            ValidInput = bool(re.match(r"^\d+$",UserNumber))
            if ValidInput !=True:
                print("\nInvalid Input!!! Enter only positive whole numbers")
        print(fibonacci_generator(int(UserNumber)))
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


print("\n ---THE END---")
list = []