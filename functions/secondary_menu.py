from colorama import Fore


def show_secondary_menu() -> str:
    return "1. Check balance\n2. Deposit\n3. Withdraw\n4. Get User ID\n" + Fore.RED + "5. Log Out" + Fore.RESET
