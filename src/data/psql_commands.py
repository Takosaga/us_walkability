import db_connection as db


def commands():
    try:
        with db.connection() as conn:
            with conn.cursor() as curs:
                curs.execute(open("test.sql", "r").read())
        keep = input("Do you wish to commit? (y/yes): ")
        if keep == "y" or keep == "yes":
            conn.commit()

    finally:
        conn.close()


if __name__ == "__main__":
    commands
