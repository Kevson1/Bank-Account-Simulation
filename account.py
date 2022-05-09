class Accounts:
    '''
    class that generates a new instance of an account
    '''
    account_list=[]
    def __init__(self, accountname, accountbalance):
        '''
        __init__ method that helps us define properties for the user object.
        Args:
            accountname: Name of the account holder
            accountbalance: The balance of the account
        '''
        self.accountname = accountname
        self.accountbalance = accountbalance

    def save_account(self):
        '''
        Save account method for saving the account object in the account_list
        '''
        Accounts.account_list.append(self)

    @classmethod
    def account_exist(cls, accountname):
        '''
        Method for checking if an account exists from the account list
        Args:
            accountname: The name of the account holder
        Return:
            Boolean: True of False depending on whether the account name has been found or not.
        '''
        for account in cls.account_list:
            if account.accountname == accountname:
                return True
        return False