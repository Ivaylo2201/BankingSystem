def deposit(database: dict, user_id: str) -> None | str:
    try:
        amount = float(input("Enter deposit amount: "))
    except ValueError:
        print("An error has occurred!")
        return None

    database[user_id].balance += amount
    print(f"You have successfully deposited {amount:,.2f}$")
