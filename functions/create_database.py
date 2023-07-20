import psycopg2

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="22012003", port="2201")


def create_database() -> None:
    Query = connection.cursor()
    Query.execute("""
    CREATE TABLE IF NOT EXISTS account (
        id SERIAL NOT NULL,
        username VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        balance FLOAT
    )
    """)

    connection.commit()
    Query.close()
