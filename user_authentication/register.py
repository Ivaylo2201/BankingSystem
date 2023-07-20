import psycopg2
from colorama import Fore
from user_authentication.generate_id import generate_unique_id
from user_authentication.validate_input import validate_input

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def register() -> None:
    Query = connection.cursor()

    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    if validate_input(username, password):
        Query.execute("""INSERT INTO account(id, username, password, balance) VALUES (%s, %s, %s, %s)""",
                      (generate_unique_id(), username, password, 0))

        print(Fore.GREEN + "\nRegistration successful!\n" + Fore.RESET)

    connection.commit()
    Query.close()
