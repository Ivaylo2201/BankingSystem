import psycopg2
from colorama import Fore
connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def validate_input(username: str, password: str) -> bool:
    Query = connection.cursor()

    Query.execute("""SELECT username FROM account""")
    taken_usernames = [current_username[0] for current_username in Query.fetchall()]

    if username in taken_usernames:
        print(Fore.RED + "\nSorry, this username is already taken!\n" + Fore.RESET)
        return False

    if len(password) < 5:
        print(Fore.RED + "\nPassword must be at least 5 characters long!\n" + Fore.RESET)
        return False

    return True
