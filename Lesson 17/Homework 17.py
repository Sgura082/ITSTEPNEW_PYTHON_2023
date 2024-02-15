
# -----------GLOBAL Variables----------------

global TaskNames
TaskNames = {"Task 1": {"Name": "Task 1: Selling and buying houses",
                        "FunctionId": 0},
             "Task 2": {"Name": "Task 2: x",
                        "FunctionId": 1},
             "Task 3": {"Name": "Task 3: x",
                        "FunctionId": 2},
             "Task 4": {"Name": "Task 4: x",
                        "FunctionId": 3},
             "Task 5": {"Name": "Task 5: x",
                        "FunctionId": 4},
             "Task 6": {"Name": "Task 6: x",
                        "FunctionId": 5},
             "Task 7": {"Name": "Task 7: x",
                        "FunctionId": 6},
             "Task 8": {"Name": "Task 8: x",
                        "FunctionId": 7},
             "Task 9": {"Name": "Task 9: x",
                        "FunctionId": 8},
             "Task 10": {"Name": "Task 10: x",
                        "FunctionId": 9}, }
global Task_function_list
Task_function_list = []

# -----------CUSTOM FUNCTIONS----------------

# -----------TASK FUNCTIONS----------------
def Task1():  # For task 1
    Looper = "y"
    while Looper == "y":
        # ----------------Task Variables----------------------------------
        # ----------------Task Classes----------------------------------
        class Person():
            def __init__(self,name):
                assert isinstance(name, str), "'name' must be a string!!!"
                self.name = name
                self.deposit = 1000.0
                self.loan = 0.0
                self.property = []
            def acquire_new_property(self,property,aqcuisition_type = "Inherited"):
                assert isinstance(property, House), "'property' must be a House (class)!!!"
                if property.get_status() == "Sold":
                    property_buying_type = "Bought"
                elif property.get_status() == "Sold with a loan":
                    property_buying_type = "Bought with a loan"
                else:
                    property_buying_type = aqcuisition_type
                self.property.append(f"{len(self.property)+1})   {property}, Acquired: {property_buying_type}")

            def give_up_old_property(self,ID):
                for i in self.property:
                    if ID in i:
                        self.property.pop(self.property.index(i))
            def __str__(self):
                return (f"--------------------\n"
                        f"Name: {self.name},\n"
                        f"Deposit Amount: {self.deposit},\n"
                        f"Loan amount:{self.loan}\n"
                        f"Property: \n"
                        f"{"\n".join(self.property)}\n"
                        f"--------------------")
            def increase_deposit(self,amount_d):
                assert isinstance(amount_d, float), "'amount_d' must be a float number!!!"
                if amount_d < 0.0:
                    print("amount can't be a negative number")
                else:
                    self.deposit += amount_d
            def increase_loan(self,amount_l):
                assert isinstance(amount_l, float), "'amount_l' must be a float number!!!"
                if amount_l < 0.0:
                    print("amount can't be a negative number")
                else:
                    self.loan += amount_l
            def get_name(self):
                return self.name
            def get_property(self):
                return self.property
        class House():
            def __init__(self,ID,price,owner=object):
                assert isinstance(ID, str), "'ID' must be a string!!!"
                assert isinstance(price, float), "'price' must be a float number!!!"
                assert isinstance(owner, Person), "'owner' must be a Person (class)!!!"
                self.ID = ID
                self.price = price
                self.owner = owner
                self.status = "For Sale"
            def get_status(self):
                return self.status
            def get_ID(self):
                return self.ID
            def __str__(self):
                return (f"ID: {self.ID},   "
                        f"Price: {self.price}")
            def change_ownership(self,new_owner, loan_amount = 0.0):
                assert isinstance(new_owner, Person), "'new_owner' must be a Person (class)!!!"
                if loan_amount == 0.0:
                    self.owner.increase_deposit(self.price)
                    self.owner.give_up_old_property(self.ID)
                    self.owner = new_owner
                    self.status = "Sold"
                    new_owner.acquire_new_property(self)
                    print(f"-------------------------------------------------------------------"
                          f"\nProperty with ID: {self.ID} was sold to {new_owner.get_name()} for {self.price}.\n"
                          f"-------------------------------------------------------------------")
                elif loan_amount > 0.0:
                    self.owner.increase_deposit(self.price)
                    self.owner.give_up_old_property(self.ID)
                    self.owner = new_owner
                    self.status = "Sold with a loan"
                    new_owner.acquire_new_property(self)
                    self.owner.increase_loan(loan_amount)
                    print(f"-------------------------------------------------------------------"
                          f"\nProperty with ID: {self.ID} was sold to {new_owner.get_name()} for {self.price} "
                          f"using a loan of {loan_amount}.\n"
                          f"-------------------------------------------------------------------")

        # ----------------Task Functions----------------------------------

        # ----------------Task BODY----------------------------------
        buyer = Person("Saba Gurashvili")
        seller = Person("Giorgi Giorgobiani")


        house1 = House("62.06.59.396",90000.99,seller)
        house2 = House("63.06.54.396", 85000.50, seller)
        seller.acquire_new_property(house1)
        seller.acquire_new_property(house2,"Won in a Casino")
        print(f"{buyer}\n"
              f"{seller}")
        pause = input("Press enter to continue")
        house2.change_ownership(buyer)
        pause = input("Press enter to continue")
        print(f"{buyer}\n"
              f"{seller}")
        pause = input("Press enter to continue")
        house1.change_ownership(buyer,40000.25)
        print(f"{buyer}\n"
              f"{seller}")
        Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
        if Replay == "y":
            continue
        else:
            Looper = Replay
Task_function_list.append(Task1)

# -------------MAIN CODE---------------------------------------------------------------------
for key, value in TaskNames.items():
    if len(Task_function_list) <= value.get('FunctionId'):
         continue
    else:
        Task_status = input(f"\nDo you want to do - {value.get('Name')}? \n(Enter 'y' for YES or any key for NO) ")
        if Task_status == "y":
            Task_function_list[value.get('FunctionId')]()
        else:
            print(f" \n{value.get('Name')} - Skipped")

print("\n ---THE END---")