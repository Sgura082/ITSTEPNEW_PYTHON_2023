import bank_account1
import contact_manager1
import unittest


class Test_BankAccount(unittest.TestCase):
    def test_deposit(self):
        bank_account_A = bank_account1.BankAccount("GE1216519819120031", "Sam Fisher", 729)
        deposit_amount = -500
        self.assertEqual(bank_account_A.deposit(deposit_amount),
                          f"Deposited ${deposit_amount}. New balance: ${bank_account_A.balance}")