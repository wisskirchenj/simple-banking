import os
import unittest
from unittest.mock import patch, MagicMock

from sqlalchemy.orm import Session

from banking.account import Account
from banking.database_manager import init_database, DatabaseManager


def get_database_session() -> Session:
    path = 'test.s3db'
    if os.path.exists(path):
        os.remove(path)
    engine = init_database(path)
    return Session(engine)


class DatabaseManagerTest(unittest.TestCase):

    _session: Session

    @classmethod
    def setUpClass(cls):
        cls._session = get_database_session()

    @classmethod
    def tearDownClass(cls):
        cls._session.close()

    @patch.object(Account, 'generate_card_number')
    def test_cards_created_unique_numbers(self, mock_gen: MagicMock):
        mock_gen.side_effect = ['4000001962433439', '4000001962433439', '4000001962433439', '4000000000000000']
        db_manager = DatabaseManager(self._session)
        db_manager.create_new_account()
        self.assertIsNotNone(db_manager.find_account('4000001962433439'))
        db_manager.create_new_account()
        self.assertIsNotNone(db_manager.find_account('4000000000000000'))
        self.assertIsNotNone(db_manager.find_account('4000001962433439'))

    def test_find_account_none_for_invalid(self):
        db_manager = DatabaseManager(self._session)
        self.assertIsNone(db_manager.find_account('4000001234567890'))
