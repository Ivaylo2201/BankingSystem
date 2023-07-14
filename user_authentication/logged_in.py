from functions.secondary_menu import show_secondary_menu
from user_transactions.deposit import deposit
from user_transactions.get_user_id import get_user_id
from user_transactions.withdraw import withdraw
from user_transactions.check_balance import check_balance
from colorama import Fore


def logged_in(user_id: int) -> None:
    while True:
        print(show_secondary_menu())

        try:
            operation = int(input("Select operation: "))
        except ValueError:
            print(Fore.RED + "Invalid operation!" + Fore.RESET)
            continue

        match operation:
            case 1: print(check_balance(user_id))
            case 2: print(deposit(user_id))
            case 3: print(withdraw(user_id))
            case 4: print(get_user_id(user_id))
            case 5: break
            case _: print(Fore.RED + "Invalid operation!" + Fore.RESET)
