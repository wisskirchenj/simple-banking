from sqlalchemy import Text
from sqlalchemy.orm import DeclarativeBase, mapped_column, MappedAsDataclass
from typing_extensions import Annotated


class Base(MappedAsDataclass, DeclarativeBase):
    pass


int_pk = Annotated[int, mapped_column(primary_key=True)]
text = Annotated[str, mapped_column(Text)]
