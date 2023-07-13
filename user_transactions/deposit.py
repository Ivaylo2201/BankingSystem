import psycopg2
from colorama import Fore
connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def deposit(user_id: int) -> str:
    Query = connection.cursor()

    try:
        amount = float(input("Enter deposit amount: "))
    except ValueError:
        return Fore.RED + "\nAn error has occurred!\n" + Fore.RESET

    Query.execute("""UPDATE account SET balance = balance + %s WHERE id = %s""", [amount, user_id])
    connection.commit()
    Query.close()

    return Fore.GREEN + f"\nYou have successfully deposited ${amount:,.2f}\n" + Fore.RESET
