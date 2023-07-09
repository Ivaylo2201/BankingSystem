def withdraw(database: dict, user_id: str) -> None | str:
    try:
        amount = float(input("Enter withdraw amount: "))
    except ValueError:
        print("An error has occurred!")
        return None

    if database[user_id].balance - amount >= 0:
        database[user_id].balance -= amount
        print(f"You have successfully withdrawn {amount:,.2f}$")

    else:
        print("Insufficient funds!")
