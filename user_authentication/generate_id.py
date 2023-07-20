import random
import psycopg2

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def generate_unique_id() -> int:
    Query = connection.cursor()
    Query.execute("""SELECT id FROM account""")
    taken_ids = [_id[0] for _id in Query.fetchall()]

    while True:
        unique_id = random.randint(100_000, 999_999)

        if unique_id in taken_ids:
            continue

        return unique_id
