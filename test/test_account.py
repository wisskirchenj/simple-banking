import unittest
from unittest.mock import patch, MagicMock

from parameterized import parameterized

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
        self.assertEqual(Account.get_luhn_checksum(card_number[:-1]), card_number[-1])

    @patch.object(Account, 'generate_card_number')
    def test_card_numbers_unique(self, mock_gen: MagicMock):
        mock_gen.side_effect = self.mock_generate_four_ids_only
        account_keys = set()
        for i in range(4):
            acc = Account(account_keys)
            account_keys.add(acc.number)
        self.assertSetEqual(set(map(str, range(4))), account_keys)

    @parameterized.expand([
        ['3', '400000844943340'],
        ['2', '400000000000000'],
        ['1', '400000999999999']
    ])
    def test_luhn_algorithm(self, expected_digit: str, number_without_checksum: str):
        self.assertEqual(expected_digit, Account.get_luhn_checksum(number_without_checksum))
        self.assertEqual(expected_digit, Account.get_luhn_checksum(number_without_checksum))
        self.assertEqual(expected_digit, Account.get_luhn_checksum(number_without_checksum))

    @staticmethod
    def mock_generate_four_ids_only():
        return Account.random_id(4)
