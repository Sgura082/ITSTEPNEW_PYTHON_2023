


# -----------GLOBAL Variables----------------
global TaskNames
TaskNames = {"Task 1": "Task 1: Creating text file and counting lines in it",
             "Task 2": "Task 2: Creating text file and writing on specific lines",
             "Task 3": "Task 3: Combining two text files (USES FILES FROM PREVIOUS TASKS)",
             }


# -----------FUNCTIONS----------------

# -----------TASK FUNCTIONS----------------

def Task1():  # For task 1
    print(f"\n{TaskNames.get('Task 1')}")
    Looper = "y"
    while Looper == "y":
        with open("text_file_task1.txt", "w") as txt_file:
            txt = "ALL POWERFUL PYTHON\n"
            for i in range(1, 1001):
                txt_file.write(str(i) + ": " + txt)
        with open("text_file_task1.txt", "r") as txt_file:
            Count_of_lines= len(txt_file.readlines())
        print(f'Count of lines in the text file is: {Count_of_lines}')
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task2():  # For task 2
    print(f"\n{TaskNames.get('Task 2')}")
    Looper = "y"
    while Looper == "y":
        chosen_line_data = {2: "TWO",
                            8: "EIGHT",
                            10: "TEN",
                            13: "THIRTEEN",
                            17: "SEVENTEEN"}
        number_keys = list(chosen_line_data.keys())
        number_names_VALUES = list(chosen_line_data.values())
        with open("text_file_task2.txt", "w") as txt_file:
            txt = "--------------------\n"
            for i in range(1, 31):
                txt_file.write(str(i) + ": " + txt)
        with open("text_file_task2.txt", "r") as txt_file:
            file_line_list = txt_file.readlines()
        with open("text_fi  le_task2.txt", "w") as txt_file:
            for i in number_keys:
                file_line_list[i-1] = str(i)+": "+number_names_VALUES[number_keys.index(i)]+"\n"
            txt_file.writelines(file_line_list)
        with open("text_file_task2.txt", "r") as txt_file:
            print(txt_file.read())
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay


def Task3():  # For task 3
    print(f"\n{TaskNames.get('Task 3')}")
    Looper = "y"
    while Looper == "y":
        with open("text_file_task1.txt", "r") as txt_file1:
            file1_content = txt_file1.readlines()
        with open("text_file_task2.txt", "r") as txt_file2:
            file2_content = txt_file2.readlines()
        with open("text_file_task3.txt", "w") as txt_file3:
            txt_file3.writelines(file1_content+file2_content)
        with open("text_file_task3.txt", "r") as txt_file3:
            print(txt_file3.read())
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

print("\n ---THE END---")