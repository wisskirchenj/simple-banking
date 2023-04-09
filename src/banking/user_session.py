from banking.account import Account
from banking.database_manager import DatabaseManager
from banking.input_utils import menu, SHOULD_EXIT, prompt_for_number

TRANSFER_PROMPT = "\nTransfer\nEnter card number:\n"
MENU_MSG = '''
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
'''
BALANCE = 1
ADD_INCOME = 2
TRANSFER = 3
CLOSE_ACCOUNT = 4
LOGOUT = 5


class UserSession:
    def __init__(self, db_manager: DatabaseManager, account: Account):
        self.account = account
        self.db_manager = db_manager

    def run(self):
        return menu(MENU_MSG, {BALANCE: self.balance, ADD_INCOME: self.add_income,
                               TRANSFER: self.transfer, CLOSE_ACCOUNT: self.close_account, LOGOUT: self.logout})

    def balance(self):
        print(f'\nBalance: {self.account.balance}')

    def add_income(self):
        income = prompt_for_number('\nEnter income:\n')
        self.account.balance += income
        self.db_manager.commit()
        print('Income was added!')

    def transfer(self):
        receiver_number = input(TRANSFER_PROMPT)
        if not (receiver := self.find_receiver(receiver_number)):
            return
        transfer_amount = prompt_for_number('Enter how much money you want to transfer:\n')
        if transfer_amount > self.account.balance:
            print('Not enough money!')
        else:
            receiver.balance += transfer_amount
            self.account.balance -= transfer_amount
            self.db_manager.commit()
            print('Success!')

    def close_account(self):
        self.db_manager.delete(self.account)
        print('\nThe account has been closed!')
        return SHOULD_EXIT

    @staticmethod
    def logout():
        print('\nYou have successfully logged out!')
        return SHOULD_EXIT

    def find_receiver(self, receiver_number: str) -> Account | None:
        if self.account.number == receiver_number:
            print("You can't transfer money to the same account!")
            return None
        if Account.get_luhn_checksum(receiver_number[:-1]) != receiver_number[-1]:
            print("Probably you made a mistake in the card number. Please try again!")
            return None
        receiver = self.db_manager.find_account(receiver_number)
        if receiver is None:
            print('Such a card does not exist.')
        return receiver
