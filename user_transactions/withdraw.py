import psycopg2
from colorama import Fore

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def withdraw(user_id: int) -> str:
    Query = connection.cursor()
    print()

    try:
        amount = float(input("Enter withdraw amount: "))
    except ValueError:
        return Fore.RED + "\nAn error has occurred!\n" + Fore.RESET

    Query.execute("""SELECT balance FROM ACCOUNT WHERE id = %s""", [user_id])
    if Query.fetchone()[0] < amount:
        return Fore.RED + "\nInsufficient funds!\n" + Fore.RESET

    Query.execute("""UPDATE account SET balance = balance - %s WHERE id = %s""", [amount, user_id])
    connection.commit()
    Query.close()

    return Fore.GREEN + f"\nYou have successfully withdrawn ${amount:,.2f}\n" + Fore.RESET
