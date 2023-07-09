from typing import Self


class Account:
    def __init__(self, user_id: str, username: str, password: str, balance: float = 0) -> None:
        self.user_id = user_id
        self.username = username
        self.password = password
        self.balance = balance

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        self.__password = value

    @classmethod
    def create_account(cls, user_id: str, username: str, password: str, balance: float = 0) -> Self:
        return cls(user_id, username, password, balance)
