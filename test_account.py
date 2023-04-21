import pytest
from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('Jane')
        self.p2 = Account('John')

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        assert self.p1.get_name() == 'Jane'
        assert self.p1.get_balance() == 0
        assert self.p2.get_name() == 'John'
        assert self.p2.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(20) == True
        assert self.p1.deposit(0) == False
        assert self.p1.deposit(-20) == False
        assert self.p2.deposit(20) == True
        assert self.p2.deposit(0) == False
        assert self.p2.deposit(-20) == False

    def test_withdraw(self):
        assert self.p1.withdraw(20) == False
        assert self.p1.withdraw(0) == False
        assert self.p1.withdraw(-20) == False
        assert self.p2.withdraw(20) == False
        assert self.p2.withdraw(0) == False
        assert self.p2.withdraw(-20) == False
