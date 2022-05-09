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
        self.new_account = Accounts("Kevson", "0")

    
    if __name__=='__main__':
        unittest.main()