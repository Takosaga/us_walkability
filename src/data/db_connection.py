import psycopg2
from dotenv import load_dotenv
import os  # provides ways to access the Operating System and allows us to read the environment variables

"""

file to make connection to NEON database

"""


def connection():
    load_dotenv()

    USERNAME = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    DATABASE = os.getenv("DATABASE")

    conn = psycopg2.connect(
        database=DATABASE, host=HOST, user=USERNAME, password=PASSWORD
    )

    return conn
