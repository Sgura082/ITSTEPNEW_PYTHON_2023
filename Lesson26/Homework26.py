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
#---------------------------------------------------------------------------------------------------START TASK 1--------
Task01 = Task("Using sockets, Client-Server")
def task1_body():
    #----SERVER SIDE-------------------------------------------------
    # ----------------Task Variables----------------------------------
    server_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 45678
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
    print("Server socket created")
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen()
    print(f"Server socket started listening to {PORT}")
    while True:
        conn, addr = server_socket.accept()
        print(f"Connected host {addr}")
        message = "Server Accepted Connection"
        conn.sendall(message.encode())
        conn.close()
Task01.write_function(task1_body)
#-----------------------------------------------------------------------------------------------------END TASK 1--------
#---------------------------------------------------------------------------------------------------START TASK 2--------
Task02 = Task("Chat Prototype")
def task2_body():
    pass
    # ----SERVER SIDE-------------------------------------------------
    # ----------------Task Variables----------------------------------
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1"
    PORT = 45678
    clients = []
    nicknames = []
    transcript = []
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    def broadcast(message):
        for client in clients:
            transcript.append(str(message))
            save_transcript(transcript)
            client.send(message)
    def save_transcript(transcript):
        with open("Transcript.txt", "w") as file:
            for line in transcript:
                file.writelines(line)
                file.writelines("\n")
    def handle_chatter(client):
        while True:
            try:
                message = client.recv(1024)
                broadcast(message)
            except:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                nicknames.remove(nickname)
                print("ERROR USER KICKED")
                break


    def receive():
        while True:
            client, addres = server_socket.accept()
            print(f"Connected with {addres}")

            client.send("Nickname".encode())
            nickname = client.recv(1024).decode()
            nicknames.append(nickname)
            clients.append(client)

            print(f"{nickname} connected")
            broadcast(f"{nickname} joined the chatbox".encode())

            thread = threading.Thread(target=handle_chatter, args=(client,))
            thread.start()
    # ----------------Task BODY---------------------------------------
    print("Socket created")
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server socket started listening")
    receive()

Task02.write_function(task2_body)
#-----------------------------------------------------------------------------------------------------END TASK 2--------

# -------------MAIN CODE---------------------------------------------------------------------

for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
