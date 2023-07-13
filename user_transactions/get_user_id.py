import psycopg2
from colorama import Fore
connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def get_user_id(user_id: int) -> str:
    Query = connection.cursor()
    Query.execute("""SELECT id FROM account WHERE id = %s""", [user_id])

    return Fore.YELLOW + f"\nYour User ID is: {Query.fetchone()[0]}\n" + Fore.RESET
