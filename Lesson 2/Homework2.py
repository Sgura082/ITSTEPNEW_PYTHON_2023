
#-----------FUNCTIONS----------------

def Task1(): #For task 1
    print("\nTask 1: Even or Odd number checking\n")
    NumberA = int(input("Enter integer number to check for Even/Odd:"))
    if (NumberA % 2) == 0:
        print(" \nThe number you have entered is Even")
    else:
        print(" \nThe number you have entered is Odd")

def Task2(): #For task 2
    print("\nTask 2: Text search and checking\n")
    User_Text = input("Enter your text:")
    if "small" in User_Text:
        print(" \n Your text contains word :  'small'")
    elif "tall" in User_Text:
        print(" \n Your text contains word :  'tall'")
    elif "middle" in User_Text:
        print(" \n Your text contains word :  'middle'")
    else:
        print(" \n Your text doesn't contain words 'small' , 'tall' and 'middle'")

def Task3(): #For task 3
    print("\nTask 3: Calculator\n")
    Number1 = input("Enter number 1: ")
    Math_function = input("Enter math function: ")
    Number2 = input("Enter number 2: ")
    Math_Text = Number1 +" " + Math_function +" "+ Number2
    print (Math_Text, "=" ,eval(Math_Text))


#-------------MAIN CODE-------------
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