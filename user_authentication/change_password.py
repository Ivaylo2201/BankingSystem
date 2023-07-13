import psycopg2
from colorama import Fore
connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def change_password() -> str:
    Query = connection.cursor()

    try:
        user_id = int(input("Enter your User ID: "))
    except ValueError:
        return Fore.RED + "Invalid User ID!" + Fore.RESET

    Query.execute("""SELECT id FROM account""")
    for _id in Query.fetchall():
        if user_id == _id[0]:
            break
    else:
        return Fore.RED + "An account with that User ID does not exist!" + Fore.RESET

    new_password = input("Enter your new password: ")
    if len(new_password) < 5:
        return Fore.RED + "\nPassword must be at least 5 characters long!\n" + Fore.RESET

    Query.execute("""UPDATE account SET password = %s WHERE id = %s""", [new_password, user_id])
    connection.commit()
    Query.close()

    return Fore.GREEN + "\nPassword successfully changed!\n" + Fore.RESET
