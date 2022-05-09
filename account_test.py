import unittest # imports the unittest module
from account import Accounts # imports the Accounts class from the account.py file

class TestAccounts(unittest.TestCase):
    '''
    Test class that defines the test cases for the behaviour of the Accounts class
    Args:
        unittest.Testcase: Test case class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Setup method to run before each test case.
        '''
        self.new_account = Accounts("Kevson", 0)

    def tearDown(self):
        '''
        Method that cleans up after every testcase:
        '''
        Accounts.account_list = []

    def test_init(self):
        '''
        Test to check if the Accounts object is initialized properly
        '''
        self.assertEqual(self.new_account.accountname, "Kevson")
        self.assertEqual(self.new_account.accountbalance, 0)

    def test_save_account(self):
        '''
        Test case for testing if the account object is saved in the account list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Accounts.account_list), 1)

    def test_save_multiple_accounts(self):
        '''
        Test case for checking if multiple users can be saved
        '''
        self.new_account.save_account()
        test_account = Accounts('Joy', 0)
        test_account.save_account()
        self.assertEqual(len(Accounts.account_list),2)

if __name__=='__main__':
    unittest.main()