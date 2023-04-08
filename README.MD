# IDEA EDU Course

Project implemented in the track 'SQL with Python' of hyperskill.org JetBrains Academy. Purpose of doing this
project is to further practice and stay in touch with Python programming.

## Technology / External Libraries

- Python 3.11.3,
- with packages: SQLAlchemy ORM & Core 2.0.9, typing, typing_extensions, random, os, unittest, unittest.mock, parameterized

## Repository Contents

The sources of main project tasks (4 stages) and pytest testing.

## Installation

Install the wheel file using pip after clone/fork:

    > pip install dist/banking-3.11.3.post1-py3-none-any.whl

## Program description

Simple banking is mainly about credit card accounts and a CL-menu to add cards, do transactions, see balances and
stuff like that. Transactions as well as the credit card accounts are stored in an SQLite-database using database
transactions.

Have fun!

## Project completion

[//]: # (Project was completed on 26.02.23)

## Progress

01.04.23 Project started - gitHub repo and project structure setup.

03.04.23 Stage 1 completed - creation of credit cards, user session to login to account, used @patch.object of
unittest.mock to replace method with mock.

04.04.23 Stage 2 completed - implement luhn algorithm for checksum to yield valid credit card number. Parameterized
tests with package parameterized.

08.04.23 Stage 3 completed - bind SQLite database with SQLAlchemy 2.0.9 to the credit card accounts. Use new Declarative
ORM-mapping of SQLAlchemy with Dataclasses.
