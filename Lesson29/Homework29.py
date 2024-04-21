import bank_account1
import contact_manager1
import unittest
import re

#------------TESTING BANK-----------------------------------------------------------------------------------------------
class Test_BankAccount(unittest.TestCase):
    def test_deposit(self):
        """Tests the 'deposit' method from bank_account1"""
        bank_account_A = bank_account1.BankAccount("GE1216519819120031", "Sam Fisher",
                                                   729)
        #----Testing positive numbers-----------------------------------------------------------------------------------
        deposit_amount = 500
        self.assertEqual(bank_account_A.deposit(deposit_amount),
                          f"Deposited ${deposit_amount}. New balance: ${bank_account_A.balance}")

        deposit_amount = 500.20
        self.assertEqual(bank_account_A.deposit(deposit_amount),
                          f"Deposited ${deposit_amount}. New balance: ${bank_account_A.balance}")

        # ----Testing 0 and negative numbers----------------------------------------------------------------------------
        deposit_amount = 0
        self.assertEqual(bank_account_A.deposit(deposit_amount),
                          f"Invalid amount for deposit.")
        deposit_amount = -299
        self.assertEqual(bank_account_A.deposit(deposit_amount),
                          f"Invalid amount for deposit.")
        deposit_amount = -150.30
        self.assertEqual(bank_account_A.deposit(deposit_amount),
                          f"Invalid amount for deposit.")

        # ----Testing strings-------------------------------------------------------------------------------------------
        with self.assertRaises(TypeError) as context:
            deposit_amount = "200"
            bank_account_A.deposit(deposit_amount)
        self.assertEqual(str(context.exception), "'>' not supported between instances of 'str' and 'int'")

    def test_withdraw(self):
        bank_account_B = bank_account1.BankAccount("GE121656498494", "Jorge Sanchez",
                                                   123)
        # ----Testing withdrawing allowed amount------------------------------------------------------------------------
        withdraw_amount = 25
        self.assertEqual(bank_account_B.withdraw(withdraw_amount),
                         f"Withdrew ${withdraw_amount}. New balance: ${bank_account_B.balance}")
        withdraw_amount = 10.36
        self.assertEqual(bank_account_B.withdraw(withdraw_amount),
                         f"Withdrew ${withdraw_amount}. New balance: ${bank_account_B.balance}")

        # ----Testing withdrawing more than on balance------------------------------------------------------------------
        withdraw_amount = 12000
        self.assertEqual(bank_account_B.withdraw(withdraw_amount),
                         "Insufficient funds or invalid amount for withdrawal.")
        withdraw_amount = 653.32
        self.assertEqual(bank_account_B.withdraw(withdraw_amount),
                         "Insufficient funds or invalid amount for withdrawal.")

        # ----Testing strings-------------------------------------------------------------------------------------------
        with self.assertRaises(TypeError) as context:
            withdraw_amount = "200"
            bank_account_B.withdraw(withdraw_amount)
        self.assertEqual(str(context.exception), "'<' not supported between instances of 'int' and 'str'")

    def test_display_balance(self):
        bank_account_C = bank_account1.BankAccount("DE47471561651191", "Heinrich Heinz",
                                                   52144521.02)
        self.assertEqual( bank_account_C.display_balance(),f"Current Balance: ${bank_account_C.balance}")