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
Task01 = Task("Describing code")
Task02 = Task("x")
Task03 = Task("x")


def task1_body():
    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                return

            last_node = self.head

            while last_node.next:
                last_node = last_node.next

            last_node.next = new_node

        def insert(self, data, index):
            new_node = Node(data)

            if index == 0:
                new_node.next = self.head
                self.head = new_node
                return

            current_node = self.head
            current_index = 0

            while current_node.next and current_index < index - 1:
                current_node = current_node.next
                current_index += 1

            new_node.next = current_node.next
            current_node.next = new_node

        def remove(self, data):

            if self.head is None:
                return

            if self.head.data == data:
                self.head = self.head.next
                return

            current_node = self.head

            while current_node.next and current_node.next.data != data:
                current_node = current_node.next

            if current_node.next:
                current_node.next = current_node.next.next

        def display_info(self):
            current_node = self.head

            while current_node is not None:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print()
    print(help(Node))
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(2)
    linked_list.append(5)
    linked_list.append(4)
    linked_list.append(4)
    linked_list.append(4)
    linked_list.append(11)
    linked_list.append(25)
    linked_list.display_info()
    linked_list.insert("Irakli", 3)
    linked_list.insert(10.1, 5)
    linked_list.display_info()
    linked_list.remove("Irakli")
    linked_list.remove(4)
    linked_list.display_info()


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
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
