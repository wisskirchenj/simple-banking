import random

IIN = "400000"


class Account:

    def __init__(self, keys):
        self.number = self.get_new_card_number(keys)
        self.pin = self.random_id(10_000)
        self.balance = 0

    def __repr__(self):
        return "{ number: " + self.number + ", pin: " + self.pin + " }"

    @staticmethod
    def get_new_card_number(keys: set[str]):
        card_number = Account.generate_card_number()
        while card_number in keys:
            card_number = Account.generate_card_number()
        return card_number

    @staticmethod
    def generate_card_number() -> str:
        number_without_checksum = IIN + Account.random_id(1_000_000_000)
        return number_without_checksum + Account.get_luhn_checksum(number_without_checksum)

    @staticmethod
    def random_id(upper_limit: int):
        return str(random.randrange(0, upper_limit)).zfill(len(str(upper_limit)) - 1)

    @staticmethod
    def get_luhn_checksum(number_without_checksum: str) -> str:
        digits = list(map(int, number_without_checksum))
        digits = [d if i % 2 else d * 2 for i, d in enumerate(digits)]
        sum_of_digits = sum([d - 9 if d > 9 else d for d in digits])
        return str((10 - sum_of_digits % 10) % 10)
