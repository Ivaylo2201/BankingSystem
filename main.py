from colorama import Fore
from user_authentication.login import login
from user_authentication.register import register
from user_authentication.change_password import change_password
from functions.primary_menu import show_primary_menu
from functions.create_database import create_database

create_database()

while True:
    print(show_primary_menu())

    try:
        operation = int(input("Select operation: "))
    except ValueError:
        print(Fore.RED + "Invalid operation!" + Fore.RESET)
        continue

    match operation:
        case 1: register()
        case 2: login()
        case 3: print(change_password())
        case 4: exit(0)
        case _: print(Fore.RED + "Invalid operation!" + Fore.RESET)
