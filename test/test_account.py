import unittest
from unittest.mock import patch, MagicMock

from banking.account import Account


class AccountTest(unittest.TestCase):

    def test_generated_format(self):
        card_number = Account.generate_card_number()
        self.is_valid_card_number(card_number)

    def test_generated_account(self):
        account = Account([])
        self.is_valid_card_number(account.number)
        self.assertEqual(4, len(account.pin))
        self.assertTrue(account.pin.isdigit())
        self.assertEqual(0, account.balance)

    def is_valid_card_number(self, card_number):
        self.assertEqual(16, len(card_number))
        self.assertTrue(card_number.isdigit())
        self.assertEqual('400000', card_number[:6])
        self.assertEqual('5', card_number[-1])

    @staticmethod
    def mock_generate_four_ids_only():
        return Account.random_id(4)

    @patch.object(Account, 'generate_card_number')
    def test_card_numbers_unique(self, mock_gen: MagicMock):
        mock_gen.side_effect = self.mock_generate_four_ids_only
        account_keys = set()
        for i in range(4):
            acc = Account(account_keys)
            account_keys.add(acc.number)
        self.assertSetEqual(set(map(str, range(4))), account_keys)


