from typing import List, Union
from user_authentication.account import Account


def split_data() -> List[List[Union[str, float]]]:
    with open('user_authentication/data.txt', 'r') as input_data:
        data: List[str] = [x.strip('\n') for x in input_data.readlines()]

        # A single account consists of exactly 4 parameters
        accounts: List[List[Union[str, float]]] = []
        ACCOUNT_RANGE: int = 4

        # Splitting the data into separate lists and adding them to the list that will be returned
        for i in range(0, len(data), ACCOUNT_RANGE):
            accounts.append([data[i], data[i+1], data[i+2], float(data[i+3])])

    return accounts


def load_data(database: dict) -> None:
    USER_ID_INDEX: int = 0

    # Instantiating the account class using its @classmethod
    for account in split_data():
        database[account[USER_ID_INDEX]] = Account.create_account(*account)
