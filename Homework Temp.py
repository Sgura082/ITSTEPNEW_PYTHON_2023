import re

# --------------------TASK DESCRIPTIONS-------------------------------
# ------Task1: Using DECORATORS
# ------Task2:
# ------Task3:
# ------Task4:


# -----------GLOBAL Variables----------------
global Task_list
Task_list = []


# -----------MAIN CLASSES----------------
class Task():
    def __init__(self, name):
        assert isinstance(name, str), "'name' must be a string!!!"
        self.Function = object
        Task_list.append(self)
        self.name = f"Task{Task_list.index(self) + 1}: {name}"

    def __str__(self):
        return self.name

    def write_function(self, object101):
        self.Function = object101

    def RunMainCode(self):
        Looper = "y"
        while Looper == "y":
            self.Function()
            Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
            if Replay == "y":
                continue
            else:
                Looper = Replay


# -----------CUSTOM FUNCTIONS----------------

# -----------TASK OBJECTS----------------
Task01 = Task("Using DECORATORS")
Task02 = Task("Using DECORATORS with functors")
Task03 = Task("Financial Transactions with commissions")


def task1_body():
    pass
Task01.write_function(task1_body)


def task2_body():
    pass
Task02.write_function(task2_body)


def task3_body():
    pass
Task03.write_function(task3_body)

# -------------MAIN CODE---------------------------------------------------------------------

for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task.RunMainCode()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
