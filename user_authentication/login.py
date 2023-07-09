from user_authentication.logged_in import logged_in


def login(database: dict) -> None | str:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for account in database.values():
        # If we have a match, bring up the secondary menu
        if account.username == username and account.password == password:
            print("Login successful!")
            logged_in(database, account.user_id)
            return None

    print("Incorrect user credentials or account does not exist!")
