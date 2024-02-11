import re
from datetime import datetime
import string
import math
from typing import List
import random
# -----------GLOBAL Variables----------------
global TaskNames 
TaskNames = ["Task 1: Calculating greatest divisor",
             "Task 2: Math wizz. Number powerups",
             "Task 3: Printing current time",
             "Task 4: Caesar cipher",
             "Task 5: Checking for prime numbers and printing divisors",
             "Task 6: Remove duplicates from list",
             "Task 7: Checking lists for monotone type",
             "Task 8: Reversing case of strings in a list",
             "Task 9: Rock, Paper, Scissors GAME",
             "Task 10: Tic-Tac-Toe GAME"]
# -----------FUNCTIONS----------------
def calc_greatestDivisor(Num):
    b = Num -1
    while True:
        a = Num % b
        if a == 0:
            return b
        else:
            b -= 1
def mathWizz(Num):
    lst = []
    for i in range (1, Num+1):
        lstLine =[]
        power2 = i**2
        power10 = i**10
        poweri = i**i
        lstLine.append(f"{i}^2 = ")
        lstLine.append(f"{i}^10 = ")
        lstLine.append(f"{i}^{i} = ")
        print('{:<10}'.format(f"{lstLine[0]}"),end="")
        print('{:<20}'.format(power2),end="")
        print('{:<10}'.format(f"| {lstLine[1]}"),end="")
        print('{:<20}'.format(power10),end="")
        print('{:<10}'.format(f"| {lstLine[2]}"),end="")
        print('{:<20}'.format(poweri))

def CaesarCipher(txt):
    ABC = string.ascii_uppercase
    abc = string.ascii_lowercase
    user_text_list =list(txt)
    coded_text_list= []
    for i in user_text_list:
        if i.isupper():
            coded_text_list.append(ABC[ABC.index(i)-3])
        elif i.islower():
            coded_text_list.append(abc[abc.index(i)-3])
        else:
            coded_text_list.append(i)
        codedText ="".join(coded_text_list)
    return codedText

def primecheck(Num):
    if calc_greatestDivisor(int(Num)) == 1:
        return f"Your number {Num} is a Prime number"
    else:
        b = Num
        divisors =[]
        while True:
            if b == 0:
                break
            elif Num % b ==0:
                divisors.append(b)
            b -= 1
        return f"Your number {Num} is not a prime number its divisors are: {divisors}"

def removeDuplicates(lst):
    lst.sort()
    lst = set(lst)
    return lst

def check_monotone(lst):
    checker = 0
    for i in range(1,len(lst)):
        if lst[i-1] < lst[i]:
            checker += 1
        elif lst[i-1] > lst[i]:
            checker -= 1
        else:
            checker = 0
    if checker == (len(lst)-1):
        return "List is Monotone and the values are ascending"
    elif checker == (-len(lst)+1):
        return "List is Monotone and the values are descending"
    else:
        return "List isn't Monotone"

def reverse_string_case(lst):
    for i in lst:
        lst[lst.index(i)] = i.swapcase()
    return lst

def RPS_Game(user_input):
    list = ["p","r","s"]
    listdetailed = ["Paper","Rock","Scissors"]
    ai_input= list[random.randrange(0,3)]
    RPS_Game.win_count_AI =0
    RPS_Game.win_count_User =0
    strength_Check = list.index(user_input) - list.index(ai_input)
    if user_input == ai_input:
        return "DRAW"
    elif strength_Check == -1 or strength_Check == 2:
        RPS_Game.win_count_User += 1
        return f"You WON this round. Your {listdetailed[list.index(user_input)]} beat AI's {listdetailed[list.index(ai_input)]}"
    elif strength_Check == 1 or strength_Check == -2:
        RPS_Game.win_count_AI += 1
        return f"You LOST this round. AI's {listdetailed[list.index(ai_input)]} beat Your {listdetailed[list.index(user_input)]}"
def PrintBoard(lst):
    print("    a    b    c")
    print(f"1 {lst[0]}")
    print(f"2 {lst[1]}")
    print(f"3 {lst[2]}")
def CheckWin(board):
    for a in board:
        if  a == ['X','X','X']:
            return "\nPlayer 1 WON!!!"
        elif a == ['O','O','O']:
            return "\nPlayer 2 WON!!!"
    for i in range(0,3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] == "X":
            return "\nPlayer 1 WON!!!"
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] == "O":
            return "\nPlayer 2 WON!!!"
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == "X":
        return "\nPlayer 1 WON!!!"
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == "O":
        return "\nPlayer 2 WON!!!"
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == "X":
        return "\nPlayer 1 WON!!!"
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == "O":
        return "\nPlayer 2 WON!!!"    
    return 1   
def Tic_Tac_Toe():
    #drawing the board
    board =[['0','0','0'],['0','0','0'],['0','0','0']]
    PrintBoard(board)
    CoordinatesX = ["a","b","c"]
    CoordinatesY = ["1","2","3"]
    while True:
        while True:
            player1_Input = input("Player 1 enter coordinates for your tic (Example b2): ")
            check = list(player1_Input)
            check[0] = CoordinatesX.index(check[0])
            check[1] = CoordinatesY.index(check[1])
            if board[check[1]][check[0]] == '0':
                board[check[1]][check[0]] = "X"
                break
            else:
                print("This spot is taken. Try another")
        print("\r")
        PrintBoard(board)
        if CheckWin(board) != 1:
            return CheckWin(board)
        while True:
            player2_Input = input("Player 2 enter coordinates for your tic (Example b2): ")
            check = list(player2_Input)
            check[0] = CoordinatesX.index(check[0])
            check[1] = CoordinatesY.index(check[1])
            if board[check[1]][check[0]] == '0':
                board[check[1]][check[0]] = "O"
                break
            else:
                print("This spot is taken. Try another")
        print("\r")
        PrintBoard(board)
        if CheckWin(board) != 1:
            return CheckWin(board)
# -----------TASK FUNCTIONS----------------

def Task1():  # For task 1
    print(f"\n{TaskNames[0]}")
    Looper = "y"
    while Looper == "y":
        while True:
            UserNumber = input("Enter whole number to calculate the greatest divisor for it: ")
            if re.match(r'^\d+$', UserNumber):
                print (f"\nThe greatest divisor for '{UserNumber}' is {calc_greatestDivisor(int(UserNumber))}")
                break
            else:
                print("Wrong input. Enter WHOLE NUMBERS ONLY!! Try again:\n")
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
            UserNumber = input("Enter whole number to calculate the greatest divisor for it: ")
            if re.match(r'^\d+$', UserNumber):
                mathWizz(int(UserNumber))
                break
            else:
                print("Wrong input. Enter WHOLE NUMBERS ONLY!! Try again:\n")
        
        
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay
def Task3():  # For task 3
    print(f"\n{TaskNames[2]}")
    Looper = "y"
    while Looper == "y":
        while True:
            currentTime = datetime.now()
            print(currentTime, end="\r")


def Task4():  # For task 4
    print(f"\n{TaskNames[3]}")
    Looper = "y"

    while Looper == "y":
        userText = input("Enter text in order to code it with Caesar cipher: \n")    
        print(CaesarCipher(userText))
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay
def Task5():  # For task 5
    print(f"\n{TaskNames[4]}")
    Looper = "y"
    while Looper == "y":
        while True:
            UserNumber = input("Enter whole number to calculate the greatest divisor for it: ")
            if re.match(r'^\d+$', UserNumber):
                break
            else:
                print("Wrong input. Enter WHOLE NUMBERS ONLY!! Try again:\n")
        print(primecheck(int(UserNumber)))
        
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay    
def Task6():  # For task 6
    print(f"\n{TaskNames[5]}")
    Looper = "y"
    while Looper == "y":
        print(removeDuplicates([1,2,445,85,42,3,6,1,2,1,1,1,1,1,2,2,358,85,445]))
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay         
def Task7():  # For task 7
    print(f"\n{TaskNames[6]}")
    Looper = "y"
    while Looper == "y":
        print(check_monotone([452,124,12,10,5,4,2]))
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay     

def Task8():  # For task 8
    print(f"\n{TaskNames[7]}")
    Looper = "y"
    while Looper == "y":
        list = ["Green","Blue","oRanGe"]
        print(list)
        print(reverse_string_case(list))
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay     

def Task9():  # For task 9
    print(f"\n{TaskNames[8]}")
    Looper = "y"
    winCount_user =0
    winCount_AI =0
    while Looper == "y":
        while True:
            while True:
                userInput = input("To play Rock,Paper,Scissors enter 'r' for rock, 'p' for paper or 's' for scissors:")
                if userInput =='p' or userInput =='r' or userInput =='s':
                    break
                else:
                    print("\nEnter ONLY one of the following 'r' for rock, 'p' for paper or 's' for scissors.\n")
            print(f"\n {RPS_Game(userInput)}")
            winCount_user += RPS_Game.win_count_User
            winCount_AI += RPS_Game.win_count_AI
            if winCount_AI > 2 and winCount_AI > winCount_user:
                print(f"\nYou LOST!!! the game by {winCount_AI} to {winCount_user}")
                break
            elif winCount_user > 2 and winCount_user > winCount_AI:
                print(f"\nYou WON!!! the game by {winCount_user} to {winCount_AI}")
                break
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay     

def Task10():  # For task 10
    print(f"\n{TaskNames[9]}")
    Looper = "y"
    while Looper == "y":
        print(Tic_Tac_Toe())
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

Task7_status = input(f"\nDo you want to do {TaskNames[6]}? \n(Enter 'y' for YES or any key for NO) ")
if Task7_status == "y":
    Task7()

else:
    print(" \nTask 7 Skipped")

Task8_status = input(f"\nDo you want to do {TaskNames[7]}? \n(Enter 'y' for YES or any key for NO) ")
if Task8_status == "y":
    Task8()

else:
    print(" \nTask 8 Skipped")

Task9_status = input(f"\nDo you want to do {TaskNames[8]}? \n(Enter 'y' for YES or any key for NO) ")
if Task9_status == "y":
    Task9()

else:
    print(" \nTask 9 Skipped")

Task10_status = input(f"\nDo you want to do {TaskNames[9]}? \n(Enter 'y' for YES or any key for NO) ")
if Task10_status == "y":
    Task10()

else:
    print(" \nTask 10 Skipped")
print("\n ---THE END---")