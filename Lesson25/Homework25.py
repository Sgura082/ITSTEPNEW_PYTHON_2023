import threading
import time
import queue
import random
import logging

# --------------------TASK DESCRIPTIONS-------------------------------
# ------Task1: JSON file parsing using threading
# ------Task2: Checking if numbers are even Using Queue



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
Task01 = Task("JSON file parsing using threading")

def task1_body():
    pass
    # ----------------Task Variables----------------------------------


    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
Task01.write_function(task1_body)

Task02 = Task("Checking if numbers are even Using Queue")

def task2_body():
    pass
    # ----------------Task Variables----------------------------------
    number_Queue = queue.Queue()
    num_workers = 3
    mthreads =[]

    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    def worker(queue1):
        worker.threadname =""
        assert isinstance(queue1, queue.Queue)
        while True:
            number =queue1.get()
            if number == None:
                break
            if number % 2 == 0:
                print(f"{threading.current_thread().name}: Number {number} is EVEN!!")
            else:
                print(f"{threading.current_thread().name}: Number {number} is ODD!!")
    # ----------------Task BODY---------------------------------------
    for _ in range(num_workers):
        thread = threading.Thread(target = worker, args=(number_Queue,))
        thread.start()
        mthreads.append(thread)
    for i in range(100):
        number_Queue.put(random.randint(1,1000))
    for _ in range(num_workers):
        number_Queue.put(None)
    for i in mthreads:
        i.join()
    print("----------------------ALL Tasks finished--------------------")
Task02.write_function(task2_body)


# -------------MAIN CODE---------------------------------------------------------------------

for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
