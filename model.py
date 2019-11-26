from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# connects to db location (location not none rn)
engine = create_engine('sqlite:///text.db', echo=True)

# declared mapping
Base = declarative_base()

'''
    The ORM’s “handle” to the database is the Session. When we first set up the
    application, at the same level as our create_engine() statement, we define
    a Session class which will serve as a factory for new Session objects:
'''
Session = sessionmaker(bind=engine)


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
