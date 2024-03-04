import json
import copy

# --------------------TASK DESCRIPTIONS-------------------------------
# ------Task1: Serialization and Deserialization using modules
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
Task01 = Task("Serialization and Deserialization using modules")
def task1_body():
    pass

    # ----------------Task Variables----------------------------------

    # ----------------Task Classes------------------------------------
    class Movie():
        def __init__(self, dict):
            for key, value in dict.items():
                self.__dict__[key] = value
        def __str__(self):
            return f"{vars(self)}"

    # ----------------Task Functions----------------------------------
    def cus_encoder(obj):
        """
        Translates Movie class objects in data into dictionaries
        :param obj:
        :return:
        """
        for i in obj:
            for movie in i['results']:
                if isinstance(movie, Movie):
                    index = i['results'].index(movie)
                    i['results'][index] = vars(movie)
        return obj


    def seek_create_modify(json_data):
        """
        Checks if a movie complies with predefined conditions, if yes then new instance (deepcopy) of it
        is created with the genres modified and  the list of movies is appended by this new instance
        :param json_data:
        :return:
        """
        new_data = copy.deepcopy(json_data)
        for page in new_data:
            lst_additional_movies = []
            for movie in page['results']:
                movie = Movie(movie)
                new_movie_element = copy.deepcopy(movie)
                if int(movie.release_date[:4]) > 2000 and "Crime" in movie.genres:
                    index = new_movie_element.genres.index("Crime")
                    new_movie_element.genres[index] = "New_Crime"
                    lst_additional_movies.append(new_movie_element)
                elif int(movie.release_date[:4]) < 2000 and "Drama" in movie.genres:
                    index = new_movie_element.genres.index("Drama")
                    new_movie_element.genres[index] = "Old_Drama"
                    lst_additional_movies.append(new_movie_element)
                elif int(movie.release_date[:4]) == 2000:
                    new_movie_element.genres.append("New_Century")
                    lst_additional_movies.append(new_movie_element)
            page['results'].extend(lst_additional_movies)
        return new_data
    # ----------------Task BODY---------------------------------------
    with open("movies.json", "r") as json_data:
        data = json.load(json_data)

    new_data = seek_create_modify(data) # Creates new data file by adding new movies as Movie class objects to 'result'
    writable_json_data = cus_encoder(new_data) # Translates newly added Movie class objects into dictionaries
    with open("movies.json", "w") as json_file:
        json.dump(writable_json_data,json_file,indent=2)
Task01.write_function(task1_body)

# -------------MAIN CODE---------------------------------------------------------------------

for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
