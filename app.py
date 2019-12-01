from tkinter import Tk  # need this to be able to copy to system clipboard lul
from cryptography.fernet import Fernet
from typing import List, Tuple
from migrate import create_connection, create_db, DB_NAME
import time
import os
import sys


file = DB_NAME


def file_list() -> List:
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    return files


def list_passwords(db_file: str) -> Tuple:
    """ Lists out all account info """
    conn = create_connection(db_file)
    db = conn.cursor()
    db.execute("SELECT * FROM Accounts")
    tupl_of_accounts = db.fetchall()
    for index, acc in enumerate(tupl_of_accounts):
        print(f"{index}| {acc}")

    index = int(input("Select: "))
    if index == "e":
        sys.exit()

    # while loop might not account for all cases
    while index < 0 or index >= len(tupl_of_accounts):
        index = int(input("Select again"))
        if index == "e":
            sys.exit()

    return tupl_of_accounts[index]


# might need somethign like this: password_hash = f.decrypt(password_bstring).decode()
def select_password(acc: Tuple) -> None:
    """ Pastes to system clipboard """
    # TODO: decrypts
    pw = acc[2]
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(pw)  # copy string to clipboard
    r.update()  # now it stays on the clipboard after the window is closed
    print("Copied to clipboard")


def new_account(db_file: str, pin: str) -> None:
    # TODO: encrypts passwords
    conn = create_connection(db_file)
    db = conn.cursor()
    # id_num = input('')
    username = input("Enter username: ")
    password = input("Enter password: ")

    # f is a Fernet object
    f = Fernet(pin)
    # fernet encrypt method only takes in byte strings
    password_bstring = f.encrypt(str.encode(password))
    # converts back into string to be inserted into sql statement
    password_hash = password_bstring.decode()
    msg = input("Is this important? (Y/n): ")
    if msg.lower() == "y":
        important = 1
    elif msg.lower() == "n":
        important = 0
    else:
        important = 0

    # Don't use text formatting, pass in a tuple
    sql_statement = """INSERT INTO Accounts (username,password_hash,important)
                        VALUES ((?),(?),(?))"""
    db.execute(sql_statement, (username, password_hash, important))
    conn.commit()
    conn.close()


# Do this later
def update_account(db_file: str) -> None:
    pass


def main() -> None:
    if file not in file_list():
        create_db()

    pin = input(
        "NOTE: This Pin is needed to de-crypt you're passwords.\n"
        "Don't write it down, make sure it's something you can "
        "remember\n"
        "Enter you're pin: "
    )

    menu = (
        "--------------------------\n"
        "(1)List passwords\n"
        "(2)Input new account info\n"
        "(3)Update acc\n"
        "(e)Exit program\n"
        "(!h)Help\n"
    )
    print(menu)

    """ Event loop """
    while True:
        choice = input("Command: ")
        print("--------------------------\n")

        if choice == "1":
            # print(list_passwords(file))
            select_password(list_passwords(file))
        elif choice == "2":
            new_account(file, pin)
        elif choice == "3":
            update_account(file)
        elif choice == "e":
            sys.exit("Program closed")
        elif choice == "!h":
            print(menu)
        else:
            print("Not A Valid Command")
            time.sleep(0.5)


if __name__ == "__main__":
    main()
