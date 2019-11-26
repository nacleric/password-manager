from model import Account
# import base64


def list_passwords() -> None:
    pass


def new_account() -> None:
    pass


def main() -> None:
    ''' main loop '''
    foo = input('(1)list passwords\n(2)input new account info\n(3)update acc')
    while True:
        if foo == 1:
            list_passwords()
        elif foo == 2:
            new_account()
        print('yeet')


if __name__ == '__main__':
    main()
