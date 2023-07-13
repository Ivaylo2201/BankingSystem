from colorama import Fore


def show_primary_menu() -> str:
    return "1. Register\n2. Login\n3. Change password\n" + Fore.RED + "4. Exit" + Fore.RESET
