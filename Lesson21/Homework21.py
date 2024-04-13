import json

# --------------------TASK DESCRIPTIONS-------------------------------
# ------Task1: Serialisation


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
Task01 = Task("Serialisation")
Task02 = Task("x")
Task03 = Task("x")


def task1_body():
    pass
    # ----------------Task Variables----------------------------------
    product_lst = []

    # ----------------Task Classes------------------------------------
    class Product():
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def __str__(self):
            return (f"Product name: {self.name} \n"
                    f"Price: {self.price} \n"
                    f"Quantity: {self.quantity}")

    # ----------------Task Functions----------------------------------
    def cus_encoder(obj):
        if isinstance(obj, Product):
            return {
                "name": obj.name,
                "price": obj.price,
                "quantity": obj.quantity
            }
        return obj

    def cus_decoder(json_data):
        return Product(json_data['name'], json_data['price'], json_data['quantity'])

    # ----------------Task BODY---------------------------------------
    product1 = Product("Orange", 5.95, 30)
    product2 = Product("Apple", 30.50, 100)
    product3 = Product("Milk", 10.95, 10)
    product_lst.append(product1)
    product_lst.append(product2)
    product_lst.append(product3)
    with open("Json_data.json", "w") as json_fileW:
        json.dump(product_lst, json_fileW, default=cus_encoder, indent=2)

    with open("Json_data.json", "r") as json_fileR:
        data = json.load(json_fileR, object_hook=cus_decoder)
    print(data)
    for i in data:
        print(f"-----------------------------------------------\n   {i}")


Task01.write_function(task1_body)


def task2_body():
    pass
    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------


Task02.write_function(task2_body)


def task3_body():
    pass
    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------


Task03.write_function(task3_body)

# -------------MAIN CODE---------------------------------------------------------------------

for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
