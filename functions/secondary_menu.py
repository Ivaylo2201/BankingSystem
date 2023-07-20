from colorama import Fore


def show_secondary_menu() -> str:
    return "1. Check balance\n2. Deposit\n3. Withdraw\n4. Get User ID\n5. Log Out\n" + Fore.RED + "6. Delete Account\n" + Fore.RESET
