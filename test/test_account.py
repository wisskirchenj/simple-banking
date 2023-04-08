import unittest

from parameterized import parameterized

from banking.account import Account, create_account


class AccountTest(unittest.TestCase):

    def test_generated_format(self):
        card_number = Account.generate_card_number()
        self.is_valid_card_number(card_number)

    def test_generated_account(self):
        account = create_account()
        self.is_valid_card_number(account.number)
        self.assertEqual(4, len(account.pin))
        self.assertTrue(account.pin.isdigit())
        self.assertEqual(0, account.balance)

    def is_valid_card_number(self, card_number):
        self.assertEqual(16, len(card_number))
        self.assertTrue(card_number.isdigit())
        self.assertEqual('400000', card_number[:6])
        self.assertEqual(Account.get_luhn_checksum(card_number[:-1]), card_number[-1])

    @parameterized.expand([
        ['3', '400000844943340'],
        ['2', '400000000000000'],
        ['1', '400000999999999']
    ])
    def test_luhn_algorithm(self, expected_digit: str, number_without_checksum: str):
        self.assertEqual(expected_digit, Account.get_luhn_checksum(number_without_checksum))
        self.assertEqual(expected_digit, Account.get_luhn_checksum(number_without_checksum))
        self.assertEqual(expected_digit, Account.get_luhn_checksum(number_without_checksum))
