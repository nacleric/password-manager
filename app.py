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
    ''' Lists out all account info '''
    conn = create_connection(db_file)
    db = conn.cursor()
    db.execute("SELECT * FROM Accounts")
    tupl_of_accounts = db.fetchall()
    for index, acc in enumerate(tupl_of_accounts):
        print(f'{index}| {acc}')

    # Maybe use walrus operator?
    index = int(input('Select: '))
    # while loop might not account for all cases
    while index < 0 or index >= len(tupl_of_accounts):
        index = input('Select again')

    return tupl_of_accounts[index]


def select_password() -> None:
    ''' Pastes to system keyboard '''
    pass


def new_account(db_file: str, pin: str) -> None:
    conn = create_connection(db_file)
    db = conn.cursor()
    # id_num = input('')
    username = input('Enter username: ')
    # encode this
    password = input('Enter password: ')
    password_hash = password
    important = input('Is this important? (Y/n): ')

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

    pin = input('NOTE: This Pin is needed to de-crypt you\'re passwords.\n'
                'Don\'t write it down, make sure it\'s something you can '
                'remember\n'
                'Enter you\'re pin: ')
    menu = (
            '--------------------------\n'
            '(1)List passwords\n'
            '(2)Input new account info\n'
            '(3)Update acc\n'
            '(e)Exit program\n'
            '(!h)Help\n'
           )
    print(menu)

    ''' Event loop '''
    while True:
        choice = input('Command: ')
        print('--------------------------\n')

        if choice == '1':
            print(list_passwords(file))
        elif choice == '2':
            new_account(file, pin)
        elif choice == '3':
            update_account(file)
        elif choice == 'e':
            sys.exit('Program closed')
        elif choice == '!h':
            print(menu)
        else:
            print('Not A Valid Command')
            time.sleep(.5)


if __name__ == '__main__':
    main()
