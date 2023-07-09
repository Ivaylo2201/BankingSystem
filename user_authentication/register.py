from user_authentication.account import Account
from user_authentication.validate_input import validate_input
from user_authentication.generate_id import generate_unique_id


def register(database: dict) -> None:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if validate_input(username, password, database):
        account = Account.create_account(generate_unique_id(database), username, password, balance=0)
        database[account.user_id] = account

        print("Registration successful!")
