from user_authentication.login import login
from user_authentication.register import register
from user_authentication.change_password import change_password
from functions.view_database import view_database
from functions.primary_menu import show_primary_menu
from functions.save_data import save_data
from functions.load_data import load_data

accounts_database = {}
load_data(accounts_database)

while True:
    show_primary_menu()

    try:
        operation = int(input("Select operation: "))
    except ValueError:
        print("Invalid operation!")
        continue

    match operation:
        case 1: register(accounts_database)
        case 2: login(accounts_database)
        case 3: change_password(accounts_database)
        case 4: print(view_database(accounts_database))
        case 5: save_data(accounts_database)
        case _: print("Invalid operation!")
