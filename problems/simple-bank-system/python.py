class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.accountIsInValid(account1):
            return False
        if self.accountIsInValid(account2):
            return False

        srcAccountIndex = account1 - 1
        destAccountIndex = account2 - 1
        if self.accounts[srcAccountIndex] - money < 0:
            return False
        
        self.accounts[srcAccountIndex] -= money
        self.accounts[destAccountIndex] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        accountIndex = account - 1
        if self.accountIsInValid(account):
            return False
        self.accounts[accountIndex] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if self.accountIsInValid(account):
            return False
        accountIndex = account - 1
        if self.accounts[accountIndex] - money < 0:
            return False
        self.accounts[accountIndex] -= money
        return True

    def accountIsInValid(self, account: int) -> bool:
        accountIndex = account - 1
        return accountIndex >= len(self.accounts)


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)