def validate_input(username: str, password: str, database: dict) -> bool:
    taken_usernames = [a.username for a in database.values()]

    if username in taken_usernames:
        print("Sorry, this username is already taken!")
        return False

    if not (5 <= len(password) <= 10):
        print("Invalid password length -> Password must be between 5 and 10 characters long [inc.]")
        return False

    return True
