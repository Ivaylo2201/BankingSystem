import psycopg2
from colorama import Fore
from user_authentication.logged_in import logged_in

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def login() -> None:
    Query = connection.cursor()

    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    Query.execute("""SELECT id, username, password FROM account""")

    for account in Query.fetchall():
        user_id, user_username, user_password = account

        if (username, password) == (user_username, user_password):
            print(Fore.GREEN + "\nLogin successful!\n" + Fore.RESET)
            logged_in(user_id)
            return None

    print(Fore.RED + "\nIncorrect user credentials or account does not exist!\n" + Fore.RESET)
