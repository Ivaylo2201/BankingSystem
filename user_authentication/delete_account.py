import psycopg2
from colorama import Fore

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def delete_account() -> tuple[bool, str]:
    terminated = True
    Query = connection.cursor()

    try:
        user_id = int(input("\nEnter your User ID: "))
    except ValueError:
        return Fore.RED + "\nInvalid User ID!\n" + Fore.RESET

    Query.execute("""SELECT id FROM account""")
    for _id in Query.fetchall():
        if user_id == _id[0]:
            break
    else:
        return Fore.RED + "\nAn account with that User ID does not exist!\n" + Fore.RESET

    confirmation = input(
        Fore.RED + "DANGER ZONE: Are you sure you want to delete your account? Type 'Confirm' to continue: "
        + Fore.RESET)

    if confirmation != "Confirm":
        return terminated, Fore.RED + "\nConfirmation failed. Process terminated.\n" + Fore.RESET

    Query.execute("""DELETE FROM account WHERE id = %s""", [user_id])

    connection.commit()
    Query.close()

    terminated = False
    return terminated, Fore.GREEN + "\nAccount deleted successfully!\n" + Fore.RESET
