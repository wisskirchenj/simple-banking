from banking.account import Account
from banking.input_utils import menu
from banking.user_session import UserSession

MENU_MSG = '''
1. Create an account
2. Log into account
0. Exit
'''
CREATE_ACCOUNT = 1
LOGIN = 2


class Banking:

    def __init__(self):
        self.accounts: dict[str, Account] = dict()

    def create_account(self):
        account = Account(self.accounts.keys())
        print(f'Your card has been created\nYour card number:\n{account.number}\nYour card PIN:\n{account.pin}')
        self.accounts[account.number] = account

    def login(self):
        card_number = input('Enter your card number:\n')
        pin = input('Enter your pin:\n')
        account = self.accounts.get(card_number)
        if account and account.pin == pin:
            print('\nYou have successfully logged in!')
            return UserSession(account).run()
        else:
            print('\nWrong card number or PIN!')

    def run(self):
        menu(MENU_MSG, {CREATE_ACCOUNT: self.create_account, LOGIN: self.login})
        print('\nBye!')


if __name__ == '__main__':
    Banking().run()
