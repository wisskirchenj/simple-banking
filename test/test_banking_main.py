import os
import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from sqlalchemy.orm import Session

from banking.account import Account
from banking.banking_main import Banking
from banking.database_manager import init_database, DatabaseManager


class TestBanking(unittest.TestCase):

    path = 'card.s3db'

    @classmethod
    def setUpClass(cls):
        if os.path.exists(cls.path):
            os.remove(cls.path)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    @patch.object(Account, 'random_id')
    def test_stage4_example1(self, mock_random: MagicMock, mock_stdout: StringIO, mock_input: MagicMock):
        mock_random.side_effect = ['945529612', '1961', '330516003', '5639']
        mock_args = ['1', '1', '2', '4000009455296122', '1961', '2', '10000', '1', '3',
                     '4000003305160035', '3', '4000003305061034', '3', '4000003305160034',
                     '15000', '3', '4000003305160034', '5000', '3', '4000009455296122', '1', '5', '0']
        mock_input.side_effect = mock_args
        Banking().run()
        self.assertEqual(2, mock_stdout.getvalue().count('Your card has been created'))
        self.assertEqual(1, mock_stdout.getvalue().count('You have successfully logged in!'))
        self.assertEqual(1, mock_stdout.getvalue().count('Income was added!'))
        self.assertEqual(1, mock_stdout.getvalue().count('Balance: 10000'))
        self.assertEqual(1, mock_stdout.getvalue().count('Balance: 5000'))
        self.assertEqual(1, mock_stdout.getvalue()
                         .count('Probably you made a mistake in the card number. Please try again!'))
        self.assertEqual(1, mock_stdout.getvalue().count('Such a card does not exist.'))
        self.assertEqual(1, mock_stdout.getvalue().count("You can't transfer money to the same account!"))
        self.assertEqual(1, mock_stdout.getvalue().count('Not enough money!'))
        self.assertEqual(1, mock_stdout.getvalue().count('Success!'))
        self.assertEqual(1, mock_stdout.getvalue().count('You have successfully logged out!'))
        self.assertEqual(1, mock_stdout.getvalue().count('Bye!'))
        self.check_database_example1()

    def check_database_example1(self):
        db = self.open_db()
        account = db.find_account('4000009455296122')
        self.assertIsNotNone(account)
        self.assertEqual('1961', account.pin)
        self.assertEqual(5000, account.balance)
        account = db.find_account('4000003305160034')
        self.assertIsNotNone(account)
        self.assertEqual('5639', account.pin)
        self.assertEqual(5000, account.balance)
        db.session.close()

    def open_db(self) -> DatabaseManager:
        engine = init_database(self.path)
        session = Session(engine)
        db = DatabaseManager(session)
        return db

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    @patch.object(Account, 'random_id')
    def test_stage4_example2(self, mock_random: MagicMock, mock_stdout: StringIO, mock_input: MagicMock):
        mock_random.side_effect = ['791605370', '6263']
        mock_args = ['1', '2', '4000007916053702', '6263', '4', '2', '4000007916053702', '6263', '0']
        mock_input.side_effect = mock_args
        Banking().run()
        self.assertEqual(1, mock_stdout.getvalue().count('Your card has been created'))
        self.assertEqual(1, mock_stdout.getvalue().count('You have successfully logged in!'))
        self.assertEqual(1, mock_stdout.getvalue().count('The account has been closed!'))
        self.assertEqual(1, mock_stdout.getvalue().count('Wrong card number or PIN!'))
        self.assertEqual(1, mock_stdout.getvalue().count('Bye!'))
        self.check_database_example2()

    def check_database_example2(self):
        db = self.open_db()
        self.assertIsNone(db.find_account('4000007916053702'))
        db.session.close()
