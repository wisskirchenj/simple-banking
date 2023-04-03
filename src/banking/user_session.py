from banking.account import Account
from banking.input_utils import menu, SHOULD_EXIT

MENU_MSG = '''
1. Balance
2. Log out
0. Exit
'''
BALANCE = 1
LOGOUT = 2


class UserSession:
    def __init__(self, account: Account):
        self.account = account

    def run(self):
        return menu(MENU_MSG, {BALANCE: self.balance, LOGOUT: self.logout})

    def balance(self):
        print(f'\nBalance: {self.account.balance}')

    @staticmethod
    def logout():
        print('\nYou have successfully logged out!')
        return SHOULD_EXIT
