from sqlalchemy.orm import Session

from banking.database_manager import DatabaseManager, init_database
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
        self.db_manager: DatabaseManager | None = None

    def create_account(self):
        account = self.db_manager.create_new_account()
        print(f'Your card has been created\nYour card number:\n{account.number}\nYour card PIN:\n{account.pin}')

    def login(self):
        card_number = input('Enter your card number:\n')
        pin = input('Enter your pin:\n')
        account = self.db_manager.find_account(card_number)
        if account and account.pin == pin:
            print('\nYou have successfully logged in!')
            return UserSession(self.db_manager, account).run()
        else:
            print('\nWrong card number or PIN!')

    def run(self):
        engine = init_database('card.s3db')
        with Session(engine) as session:
            self.db_manager = DatabaseManager(session)
            menu(MENU_MSG, {CREATE_ACCOUNT: self.create_account, LOGIN: self.login})
        print('\nBye!')


if __name__ == '__main__':
    Banking().run()
