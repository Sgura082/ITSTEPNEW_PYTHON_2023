from abc import ABC, abstractmethod

# ------------------------------------------------------------------------------TASK DESCRIPTIONS-----------------------
# ------Task1: Creating Media Player using SOLID principles
# ------Task2:
# ------Task3:
# ------Task4:


# ------------------------------------------------------------------------------GLOBAL Variables------------------------
global Task_list
Task_list = []

# ------------------------------------------------------------------------------MAIN CLASSES----------------------------
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


# ------------------------------------------------------------------------------CUSTOM FUNCTIONS------------------------

# ------------------------------------------------------------------------------TASK OBJECTS----------------------------
# --------------------------------------------------------------------------------------------------START TASK 1--------
Task01 = Task("Creating Media Player using SOLID principles")
def task1_body():
    pass
    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    class Iplayer(ABC):
        def play(self,file):
            print(f"playing - {file}")
    class Ipauser(ABC):
        def pause(self,file):
            print(f"paused - {file}")
    class Istopper(ABC):
        def stop(self,file):
            print(f"Stopped - {file}")
    class Irewinder(ABC):
        def rewind(self,file):
            print(f"rewinding - {file}")
    class Iforwarder(ABC):
        def forward(self,file):
            print(f"forwarding - {file}")
    class Ifast_forwarder(ABC):
        def fast_forward(self,file):
            print(f"fast forwarding - {file}")
    class Video_player(Iplayer,Ipauser,Istopper,Irewinder,Iforwarder,Ifast_forwarder):
        def __init__(self):
            print("Movie Player open\n------------------------")
    class Audio_player(Iplayer,Ipauser,Istopper,Irewinder,Iforwarder,Ifast_forwarder):
        def __init__(self):
            print("Audio Player open\n------------------------")
    class Stream_player(Iplayer,Ipauser,Istopper):
        def __init__(self):
            print("Stream Player open\n------------------------")

    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
    VP = Video_player()
    VP.play("movie.avi")
    VP.pause("movie.avi")
    VP.stop("movie.avi")
    VP.play("movie.avi")
    VP.rewind("movie.avi")
    VP.fast_forward("movie.avi")
    print("------------------------------------\n")
    AP = Audio_player()
    AP.play("music.flac")
    AP.pause("music.flac")
    AP.stop("music.flac")
    AP.play("music.flac")
    AP.rewind("music.flac")
    AP.fast_forward("music.flac")
    print("------------------------------------\n")
    SP = Stream_player()
    SP.play("youtube stream")
    SP.pause("youtube stream")
    SP.stop("youtube stream")



Task01.write_function(task1_body)
# ----------------------------------------------------------------------------------------------------END TASK 1--------
# --------------------------------------------------------------------------------------------------START TASK 2--------
Task02 = Task("x")
def task2_body():
    pass
    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
Task02.write_function(task2_body)
#-----------------------------------------------------------------------------------------------------END TASK 2--------
#---------------------------------------------------------------------------------------------------START TASK 3--------
Task03 = Task("x")
def task3_body():
    pass
    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
Task03.write_function(task3_body)
#-----------------------------------------------------------------------------------------------------END TASK 3--------
# ------------------------------------------------------------------------------MAIN CODE-------------------------------
for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
