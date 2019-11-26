from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
import base64

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# connects to db location (location not none rn)
engine = create_engine('sqlite:///:memory:', echo=True)
# declared mapping
Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hash = Column(String)
    important = Column(Boolean)

    def __repr__(self):
        return '<ID: {}, Username: {}, Password: {}, important: {}>'.format(
            self.id,
            self.username,
            self.password_hash,
            self.important
        )


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
