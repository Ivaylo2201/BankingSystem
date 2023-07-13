import psycopg2
from colorama import Fore
connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def check_balance(user_id: int) -> str:
    Query = connection.cursor()

    Query.execute("""SELECT balance FROM account WHERE id = %s""", [user_id])
    return Fore.YELLOW + f"\nYour current balance is: ${Query.fetchone()[0]:,.2f}\n" + Fore.RESET
