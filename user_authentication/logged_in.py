from functions.secondary_menu import show_secondary_menu
from user_transactions.deposit import deposit
from user_transactions.withdraw import withdraw


def logged_in(database: dict, user_id: str) -> None:
    while True:
        show_secondary_menu()

        try:
            operation = int(input("Select operation: "))
        except ValueError:
            print("Invalid operation!")
            continue

        match operation:
            case 1: print(f"Your current balance is: {database[user_id].balance:,.2f}$")
            case 2: deposit(database, user_id)
            case 3: withdraw(database, user_id)
            case 4: print(f"Your User ID is: {database[user_id].user_id}")
            case 5: break
            case _: print("Invalid operation!")
