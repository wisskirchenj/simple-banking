from sqlalchemy import Engine, create_engine, inspect, select
from sqlalchemy.orm import Session

from banking.account import Account, create_account, ACCOUNT_TABLE
from banking.alchemy_base import Base


class DatabaseManager:

    def __init__(self, session: Session):
        self.session = session

    def find_account(self, number: str) -> Account | None:
        query = select(Account).where(Account.number == number)
        return self.session.scalars(query).first()

    def create_new_account(self) -> Account:
        account = create_account()
        while self.find_account(account.number) is not None:
            account = create_account()
        self.session.add(account)
        self.session.commit()
        return account


def init_database(filename: str) -> Engine:
    engine = create_engine('sqlite+pysqlite:///' + filename, echo=True)
    if ACCOUNT_TABLE not in inspect(engine).get_table_names():
        Base.metadata.create_all(engine)
    return engine
