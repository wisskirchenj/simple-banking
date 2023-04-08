import random

from sqlalchemy.orm import Mapped, mapped_column

from banking.alchemy_base import Base, int_pk, text

IIN = "400000"
ACCOUNT_TABLE = 'card'


class Account(Base):

    __tablename__ = ACCOUNT_TABLE

    id: Mapped[int_pk] = mapped_column(init=False)
    number: Mapped[text]
    pin: Mapped[text]
    balance: Mapped[int] = mapped_column(default=0)

    def __repr__(self):
        return "{ number: " + self.number + ", pin: " + self.pin + " }"

    @staticmethod
    def generate_card_number() -> str:
        number_without_checksum = IIN + Account.random_id(1_000_000_000)
        return number_without_checksum + Account.get_luhn_checksum(number_without_checksum)

    @staticmethod
    def random_id(upper_limit: int) -> str:
        return str(random.randrange(0, upper_limit)).zfill(len(str(upper_limit)) - 1)

    @staticmethod
    def get_luhn_checksum(number_without_checksum: str) -> str:
        digits = list(map(int, number_without_checksum))
        digits = [d if i % 2 else d * 2 for i, d in enumerate(digits)]
        sum_of_digits = sum([d - 9 if d > 9 else d for d in digits])
        return str((10 - sum_of_digits % 10) % 10)

    @staticmethod
    def get_random_pin() -> str:
        return Account.random_id(10_000)


def create_account() -> Account:
    return Account(number=Account.generate_card_number(), pin=Account.get_random_pin())
