def save_data(database: dict) -> None:
    with open('user_authentication/data.txt', 'w') as output_data:
        for account in database.values():
            output_data.write(f"{account.user_id}\n{account.username}\n{account.password}\n{account.balance}\n")
    exit()
