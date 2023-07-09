import random


def generate_unique_id(database: dict) -> str:
    taken_ids = [a.user_id for a in database.values()]

    # Generating an int->str. If it already exists generate a new one, else return it
    while True:
        current_id = str(random.randint(100000, 999999))

        if current_id in taken_ids:
            continue

        return current_id
