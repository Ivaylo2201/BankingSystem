def change_password(database: dict) -> None | str:
    user_id = input("Enter your user ID: ")

    if user_id not in database:
        print("An account with that user ID does not exist!")
        return None

    new_password = input("Enter your new password: ")
    database[user_id].password = new_password
    print("Password successfully changed!")
