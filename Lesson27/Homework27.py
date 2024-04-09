import asyncio
import multiprocessing
import time
import random
# --------------------TASK DESCRIPTIONS-------------------------------
# ------Task1: Launching two Async functions
# ------Task2: Async function, number printer
# ------Task3: Async function: math operations
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

    def __call__(self):
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
# ---------------------------------------------------------------------------------------------------START TASK 1--------
Task01 = Task("Launching two Async functions")


def task1_body():
    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    async def func1():
        startt = time.localtime()
        print(f"Function 1 started at {time.strftime('%H:%M:%S', startt)}")
        await asyncio.sleep(2)
        endt = time.localtime()
        print(f"Function 1 ended at {time.strftime('%H:%M:%S', endt)}")
    async def func2():
        startt = time.localtime()
        print(f"Function 2 started at {time.strftime('%H:%M:%S', startt)}")
        await asyncio.sleep(5)
        endt = time.localtime()
        print(f"Function 2 ended at {time.strftime('%H:%M:%S', endt)}")
    # ----------------Task BODY---------------------------------------
    async def main():
        task1 = asyncio.create_task(func1())
        task2 = asyncio.create_task(func2())
        await task1
        await task2
    if __name__ == '__main__':
        asyncio.run(main())

Task01.write_function(task1_body)
# -----------------------------------------------------------------------------------------------------END TASK 1--------
# ---------------------------------------------------------------------------------------------------START TASK 2--------
Task02 = Task("Async function, number printer")
def task2_body():
    pass
    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    async def printer():
        for i in range(10):
            await asyncio.sleep(random.randint(1,6))
            print(f"Number {i} printed at {time.strftime('%H:%M:%S', time.localtime())}")
    # ----------------Task BODY---------------------------------------
    async def main():
        task1 = asyncio.create_task(printer())
        await task1
    if __name__ == '__main__':
        asyncio.run(main())

Task02.write_function(task2_body)
# -----------------------------------------------------------------------------------------------------END TASK 2--------
# ---------------------------------------------------------------------------------------------------START TASK 3--------
Task03 = Task("Async function: math operations")


def task3_body():
    pass
    # ----------------Task Variables----------------------------------
    User_input = input("Enter any number: ")
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    async def math_power(x):
        if await even_checker(x):
            print(x**2)
    async def even_checker(x):
        if x % 2 == 0.0:
            return x
        else:
            print("Number isn't EVEN")
            return

    # ----------------Task BODY---------------------------------------
    async def main():
        task1 = asyncio.gather(math_power(float(User_input)))
        task2 = asyncio.gather(even_checker(float(User_input)))
        await task1
        await task2
    if __name__ == '__main__':
        asyncio.run(main())


Task03.write_function(task3_body)
# -----------------------------------------------------------------------------------------------------END TASK 3--------
# -------------MAIN CODE---------------------------------------------------------------------

for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
