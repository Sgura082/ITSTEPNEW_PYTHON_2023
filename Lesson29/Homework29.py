import bank_account1
import contact_manager1
import unittest
import re

#------------TESTING BANK-----------------------------------------------------------------------------------------------
class Test_BankAccount(unittest.TestCase):
    def setUp(self):
        print("Setup Bank Account")
        self.bank_account_A = bank_account1.BankAccount("GE1216519819120031", "Sam Fisher",
                                                   729)
        self.bank_account_C = bank_account1.BankAccount("DE47471561651191", "Heinrich Heinz",
                                                        52144521.02)
        self.bank_account_B = bank_account1.BankAccount("GE121656498494", "Jorge Sanchez",
                                                   123)
    def tearDown(self):
        print("tearDown Bank Account\n")
    def test_deposit(self):
        """Tests the 'deposit' method from bank_account1"""
        print("Testing deposit")
        #----Testing positive numbers-----------------------------------------------------------------------------------
        deposit_amount = 500
        self.assertEqual(self.bank_account_A.deposit(deposit_amount),
                          f"Deposited ${deposit_amount}. New balance: ${self.bank_account_A.balance}")

        deposit_amount = 500.20
        self.assertEqual(self.bank_account_A.deposit(deposit_amount),
                          f"Deposited ${deposit_amount}. New balance: ${self.bank_account_A.balance}")

        # ----Testing 0 and negative numbers----------------------------------------------------------------------------
        deposit_amount = 0
        self.assertEqual(self.bank_account_A.deposit(deposit_amount),
                          f"Invalid amount for deposit.")
        deposit_amount = -299
        self.assertEqual(self.bank_account_A.deposit(deposit_amount),
                          f"Invalid amount for deposit.")
        deposit_amount = -150.30
        self.assertEqual(self.bank_account_A.deposit(deposit_amount),
                          f"Invalid amount for deposit.")

        # ----Testing strings-------------------------------------------------------------------------------------------
        with self.assertRaises(TypeError) as context:
            deposit_amount = "200"
            self.bank_account_A.deposit(deposit_amount)
        self.assertEqual(str(context.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_withdraw(self):
        print("Testing withdraw")
        # ----Testing withdrawing allowed amount------------------------------------------------------------------------
        withdraw_amount = 25
        self.assertEqual(self.bank_account_B.withdraw(withdraw_amount),
                         f"Withdrew ${withdraw_amount}. New balance: ${self.bank_account_B.balance}")
        withdraw_amount = 10.36
        self.assertEqual(self.bank_account_B.withdraw(withdraw_amount),
                         f"Withdrew ${withdraw_amount}. New balance: ${self.bank_account_B.balance}")

        # ----Testing withdrawing more than on balance------------------------------------------------------------------
        withdraw_amount = 12000
        self.assertEqual(self.bank_account_B.withdraw(withdraw_amount),
                         "Insufficient funds or invalid amount for withdrawal.")
        withdraw_amount = 653.32
        self.assertEqual(self.bank_account_B.withdraw(withdraw_amount),
                         "Insufficient funds or invalid amount for withdrawal.")

        # ----Testing strings-------------------------------------------------------------------------------------------
        with self.assertRaises(TypeError) as context:
            withdraw_amount = "200"
            self.bank_account_B.withdraw(withdraw_amount)
        self.assertEqual(str(context.exception), "'<' not supported between instances of 'int' and 'str'")

    def test_display_balance(self):
        print("Testing display_balance")
        self.assertEqual( self.bank_account_C.display_balance(),f"Current Balance: ${self.bank_account_C.balance}")

#------------TESTING Contact manager------------------------------------------------------------------------------------
class Test_ContactManager(unittest.TestCase):
    def setUp(self):
        print("Setup Contact Manager")
        self.ConMan1 = contact_manager1.ContactManager()
        self.contact1 ="Charlie Sheen"
        self.contact1_phone = 5963333333
        self.contact2 = "Giorgi Razmadze"
        self.contact2_phone = 5991111111
        self.contact3 = "Friedrick Nitellbottom"
        self.contact3_phone = 5771111444
        self.ConMan1.add_contact(self.contact3,self.contact3_phone)
    def tearDown(self):
        print("tearDown Contact Manager\n")

    def test_add_contact(self):
        print("Testing add_contact")
        # ----Testing Addition of new contacts--------------------------------------------------------------------------
        self.assertEqual( self.ConMan1.add_contact(self.contact1,self.contact1_phone),
                          f"Contact '{self.contact1}' added successfully.")
        self.assertEqual( self.ConMan1.add_contact(self.contact2,self.contact2_phone),
                          f"Contact '{self.contact2}' added successfully.")

        # ----Testing Addition of already added contacts again----------------------------------------------------------
        self.assertEqual( self.ConMan1.add_contact(self.contact1,self.contact1_phone),
                          f"Contact '{self.contact1}' already exists.")

    def test_remove_contact(self):
        print("Testing remove_contact")
        # ----Testing Removal of contacts present in ContactManager-----------------------------------------------------
        self.assertEqual(self.ConMan1.remove_contact(self.contact3),
                         f"Contact '{self.contact3}' removed successfully.")

        # ----Testing Removal of contacts not present ContactManager----------------------------------------------------
        self.assertEqual(self.ConMan1.remove_contact(self.contact2),
                         f"Contact '{self.contact2}' not found.")

    def test_search_contact(self):
        print("Testing search_contact")
        # ----Testing Search of contacts present in ContactManager------------------------------------------------------
        self.assertEqual(self.ConMan1.search_contact(self.contact3),
                         f"Name: {self.contact3}, Phone Number: {self.ConMan1.contacts[self.contact3]}")
        # ----Testing Search of contacts not present in ContactManager-------------------------------------------------
        self.assertEqual(self.ConMan1.search_contact(self.contact1),
                     f"Contact '{self.contact1}' not found.")

    def test_display_contacts(self):
        # ----CODE OF THIS METHOD IS FAULTY!!!! it will always print only first contact and stop!!
        print("Testing display_contacts")
        # ----Testing Display contacts when manager has contacts in it--------------------------------------------------
        self.assertEqual(self.ConMan1.display_contacts(),f"Name: {self.contact3}, "
                                                         f"Phone Number: {self.contact3_phone}")