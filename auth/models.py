from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Sequence


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))

    def __repr__(self):
        return f"<User username={self.username}, email={self.email}>"


engine = create_engine("sqlite:///data.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
