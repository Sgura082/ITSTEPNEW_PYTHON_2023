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
    # ----------------Task Classes----------------------------------
    class Node:
        """
        Class for creation of Node objects, the elements of LinkedLists
        """

        def __init__(self, data):
            """
            Initiates the object of Node Class by saving given argument in 'data'. It also keeps information about
            the Node that comes after current one in the LinkedList in 'next'
            """
            self.data = data
            self.next = None

    class LinkedList:
        """
        Class for creation of Linked Lists
        """

        def __init__(self):
            """
            Initiates the object of LinkedList Class, setting 'head' as none.
            """
            self.head = None

        def append(self, data):
            """
            Adds given argument 'data' to the LinkedList by storing it in a newly created Node class object (new_node)
            and then adds it as a last element in the list. For details see comments in code.
            :param data: data to be added to the LinkedList
            :return:
            """
            new_node = Node(data)  # Creates a new Node class object which stores argument ('data')

            if self.head is None:  # Checks whether the list is empty or not by checking the 'head'
                                    # variable (which equals None by default). If its empty then the new_node
                                    # object is stored as the 'head' (first element of LinkedList)
                self.head = new_node
                return

            last_node = self.head #In order to add the new_node as the last element/node system needs to identify
            # the current last Node within the LinkedList. To do so every Node will be checked whether it is last or not.
            # So system starts with the first node of list.

            while last_node.next: #In order for the Node within the LinkedList to be the last one
                # the Node.next == None must be true, since this variable stores data about the node after
                # it in the linked list. This while loop works while the 'next' is filled, constantly appointing
                # the Node after the current one until there is no next Node. As a result of loop the current las node is
                # written in 'last_node'
                last_node = last_node.next

            last_node.next = new_node #The new_node is appointed as a next for the current last element

        def insert(self, data, index):
            """
            Adds given argument 'data' to the LinkedList by storing it in a specific index in form of newly created Node class object
            (new_node)
            For details see comments in code.
            :param data: data to be added to the LinkedList
            :param index: index where the 'data' needs to be added
            :return:
            """
            new_node = Node(data) # Creates a new Node class object which stores argument ('data')

            if index == 0: #If the desired index is 0 then current head of the Linked list is appointed as 'next' for
                # new_node since it becomes the head(first node) of the LinkedList
                new_node.next = self.head
                self.head = new_node
                return

            current_node = self.head
            current_index = 0

            while current_node.next and current_index < index - 1: #In order to find the Node in list that comes
                # before the desired index system checks every Node from the very start. While the checked(current) Node
                # has 'next' filled and its index is below the index of a Node that comes before the insertion
                # index is incremented and next nodes are set as current ones
                current_node = current_node.next
                current_index += 1

            new_node.next = current_node.next #Sets the Node that came after the current node as the 'next' for new_node
            # since the new node now comes after the current node but before the Node that came after it.

            current_node.next = new_node #Sets new_node as the next for the current_node since now it comes after
            # it in the order.

        def remove(self, data):
            """
            Removes the data from the LinkedList
            :param data: data to be removed from the LinkedList
            :return:
            """
            if self.head is None: #If list is empty returns None
                return

            if self.head.data == data: #Checks if the first node contains the 'removable data' if True sets
                # the Node that came after the first one as the head(first one) of List.
                self.head = self.head.next
                return

            current_node = self.head
            while current_node.next and current_node.next.data != data: #In order to find the Node which come before
                # the Node that contains the 'data' system checks every Node in list. Loop stops when it finds the node
                # with desired data or when it reaches the last node (for which 'next'==None)
                current_node = current_node.next

            if current_node.next: #Since the Node that needs to be removed comes after the current node.
                # The value of 'next' for current node is set as the removable nodes next Node(node that came after the removable node)
                current_node.next = current_node.next.next

        def display_info(self): # prints the contents of the Linked list
            current_node = self.head

            while current_node is not None:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print()

    a = LinkedList()
    a.insert()
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
