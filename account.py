class Account:
    '''

    A class representing the account of a person
    '''
    def __init__(self, name: str) -> None:
        '''

        Constructor to create initial state of a person's account balance with a name and zero balance
        :param name: Person's first name
        '''

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''

        Method to increase amount balance after checking that the amount deposited is greater than zero
        :param amount: Amount to be deposited
        :return: returns true or false based on checking the amount to be deposited
        '''

        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:

        '''

        Method to withdraw a specified amount of money from a person's account after checking that the amount is not less than zero or does not exceed account balance
        :param amount: Amount to be withdrawn
        :return: returns True or False based on the check
        '''

        if amount > self.__account_balance or amount <= 0:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''

        Method to access a person's balance
        :return: Returns the balance
        '''

        return self.__account_balance

    def get_name(self) -> str:
        '''

        Method to access the name of the account
        :return: Returns the account name
        '''

        return self.__account_name


