import sqlite3


DB_NAME = "test.db"


def create_connection(db_file):
    """ Handles errors during connection """
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as err:
        print(err)

    return conn


def create_db() -> None:
    conn = create_connection(DB_NAME)

    # cursor Object that allows it to perform SQL commands
    db = conn.cursor()

    db.execute(
        """CREATE TABLE Accounts
                (
                    id INT PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password_hash TEXT NOT NULL,
                    important INT
                )
               """
    )

    conn.commit()
    conn.close()
