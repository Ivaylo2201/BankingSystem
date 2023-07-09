from typing import List


def view_database(database: dict) -> str:
    accounts_list: List[str] = []

    # Keeping track of the index and the account itself and adding
    # a string containing its data along with the index
    for index, account in enumerate(database.values()):
        accounts_list.append(
            f"#{index + 1} -> User ID: {account.user_id}, Username: {account.username}, "
            f"Password: {account.password}, Balance: {account.balance:,.2f}$"
        )

    # Returning the list of strings joined by a new line
    return '\n'.join(accounts_list)
