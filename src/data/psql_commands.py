import db_connection as db


def commands(psql_file):
    try:
        with db.connection() as conn:
            with conn.cursor() as curs:
                curs.execute(open(psql_file, "r").read())
        keep = input("Do you wish to commit? (y/yes): ")
        if keep == "y" or keep == "yes":
            conn.commit()

    finally:
        conn.close()


if __name__ == "__main__":
    file = input("Which file do you want to pass thru to database? ")
    commands(file)
