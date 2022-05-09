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

    