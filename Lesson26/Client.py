import socket
import threading

# --------------------TASK DESCRIPTIONS-------------------------------
# ------Task1: Using sockets, Client-Server
# ------Task2: Chat Prototype

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
Task01 = Task("Using sockets, Client-Server")


def task1_body():
    pass
    # ----------------Task Variables----------------------------------
    client_socket = socket.socket()
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 45678
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
    client_socket.connect((SERVER_IP, SERVER_PORT))
    received_message = client_socket.recv(1024).decode()
    print(received_message)
    client_socket.close()


Task01.write_function(task1_body)
# -----------------------------------------------------------------------------------------------------END TASK 1--------
# ---------------------------------------------------------------------------------------------------START TASK 2--------
Task02 = Task("Chat Prototype")


def task2_body():
    # ----------------Task Variables----------------------------------
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 45678

    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    def receiver():
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message == "Nickname":
                    client_socket.send(nickname.encode())
                else:
                    print(message)
            except:
                print("ERROR!!!")
                client_socket.close()
                break

    def writer():
        while True:
            message = f"{nickname} -> {input()}"
            client_socket.send(message.encode())

    # ----------------Task BODY---------------------------------------
    nickname = input("Enter your nickname: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    thread_receive = threading.Thread(target=receiver)
    thread_receive.start()
    thread_write = threading.Thread(target=writer)
    thread_write.start()


Task02.write_function(task2_body)
# -----------------------------------------------------------------------------------------------------END TASK 2--------

# -------------MAIN CODE---------------------------------------------------------------------

for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
