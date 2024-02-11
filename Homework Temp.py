
# -----------GLOBAL Variables----------------

global TaskNames
TaskNames = {"Task 1": {"Name": "Task 1: x",
                        "FunctionId": 0},
             "Task 2": {"Name": "Task 2: x",
                        "FunctionId": 1},
             "Task 3": {"Name": "Task 3: x",
                        "FunctionId": 2},
             "Task 4": {"Name": "Task 4: x",
                        "FunctionId": 3},
             "Task 5": {"Name": "Task 5: x",
                        "FunctionId": 4},
             "Task 6": {"Name": "Task 6: x",
                        "FunctionId": 5},
             "Task 7": {"Name": "Task 7: x",
                        "FunctionId": 6},
             "Task 8": {"Name": "Task 8: x",
                        "FunctionId": 7},
             "Task 9": {"Name": "Task 9: x",
                        "FunctionId": 8},
             "Task 10": {"Name": "Task 10: x",
                        "FunctionId": 9}, }
global Task_function_list
Task_function_list = []

# -----------CUSTOM FUNCTIONS----------------

# -----------TASK FUNCTIONS----------------
def Task1():  # For task 1
    Looper = "y"
    while Looper == "y":
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay
Task_function_list.append(Task1)

def Task2():  # For task 2
    Looper = "y"
    while Looper == "y":
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay
Task_function_list.append(Task2)

# -------------MAIN CODE---------------------------------------------------------------------
for key, value in TaskNames.items():
    if len(Task_function_list) <= value.get('FunctionId'):
         continue
    else:
        Task_status = input(f"\nDo you want to do - {value.get('Name')}? \n(Enter 'y' for YES or any key for NO) ")
        if Task_status == "y":
            Task_function_list[value.get('FunctionId')]()
        else:
            print(f" \n{value.get('Name')} - Skipped")

print("\n ---THE END---")