# -----------FUNCTIONS----------------

def Task1():  # For task 1
    print("\nTask 1: Cheking for palindrome\n")
    Looper = "y"
    while Looper == "y":
        UserText = input("\nEnter to check whether it is a palindrome or not: ")
        ReversedText =""
        for i in range(len(UserText)-1,-1,-1):
            ReversedText += UserText[i]
        if UserText == ReversedText:
            print("\nYour word is a PALINDROME")
        else:
            print("\nWord is NOT a palindrome")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay
    



def Task2():  # For task 2
    print("\nTask 2: ASCII conversion of users text")
    Looper = "y"
    while Looper == "y":
        UserText = input("\nEnter text: \n")
        for i in UserText:
            print(ord(i), end=" ")
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

print("\n ---THE END---")