
# --------------------TASK DESCRIPTIONS-------------------------------
# ------Task1: Using DECORATORS
# ------Task2: Using DECORATORS with functors
# ------Task3: Financial Transactions with commissions



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

# -----------TASK OBJECTS & CODE----------------
Task01 = Task("Using DECORATORS")
def task1_body():
    def decorator(func):
        def wrapper(userinput):
            if userinput < 0:
                raise ValueError("Number can't be negative. Try again!!!")
            else:
                return f"Number is {func(userinput)}!!!"
        return wrapper
    @decorator
    def func(number):
        return float(number)
    user_input = float(input("\nEnter any positive number: "))
    print(func(user_input))
Task01.write_function(task1_body)


Task02 = Task("Using DECORATORS with functors")
def task2_body():
    class decoratorCLASS:
        def __init__(self,func):
            self.func = func
        def __call__(self,userinput):
            if userinput < 0:
                raise ValueError("Number can't be negative. Try again!!!")
            else:
                return f"Number is {self.func(userinput)}!!!"
    @decoratorCLASS
    def func2(number):
        return float(number)
    user_input = float(input("\nEnter any positive number: "))
    print(func2(user_input))
Task02.write_function(task2_body)


Task03 = Task("Financial Transactions with commissions")
def task3_body():
    def Commission(func):
        def wrapper(balancew, sumw):
            if (balancew - sumw) >=1:
                balancew -= 1
                return f"\n{func(balancew,sumw)}\nCommission of 1 GEL was deducted from your balance\n"
            else:
                return f"Not enough money on balance to cover the commission of 1 GEL !!!"
        return wrapper

    @Commission
    def transaction(balance, sum):
        if sum <= balance:
            balance -= sum
            return f"Your transaction of {sum} was successful. Remaining balance: {balance} "
        else:
            return f"Not enough money on balance!!! You require additional {sum - balance}."
    user_input_balance = float(input("\nEnter your current balance: "))
    user_input_sum = float(input("\nEnter the sum you wish to transfer from your balance: "))
    print(transaction(user_input_balance,user_input_sum))
Task03.write_function(task3_body)

# -------------MAIN CODE---------------------------------------------------------------------

for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        print(f"\n{task}\n---------------------------------------------------------")
        task.RunMainCode()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
