import random

IIN = "400000"
CHECK_SUM = "5"


class Account:

    def __init__(self, keys):
        self.number = self.get_new_card_number(keys)
        self.pin = self.random_id(10_000)
        self.balance = 0

    def __repr__(self):
        return "{ number: " + self.number + ", pin: " + self.pin + " }"

    @staticmethod
    def generate_card_number() -> str:
        return IIN + Account.random_id(1_000_000_000) + CHECK_SUM

    @staticmethod
    def random_id(upper_limit: int):
        return str(random.randrange(0, upper_limit)).zfill(len(str(upper_limit)) - 1)

    @staticmethod
    def get_new_card_number(keys: set[str]):
        card_number = Account.generate_card_number()
        while card_number in keys:
            card_number = Account.generate_card_number()
        return card_number
