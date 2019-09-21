from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from flask_login import UserMixin


Base = declarative_base()

class User(Base,UserMixin):
	__tablename__='user'

	id=Column(Integer,primary_key=True)
	name=Column(String(30),nullable=False,unique=True)
	email=Column(String(40),nullable=False,unique=True)
	password=Column(String(40),nullable=False,unique=True)


engine=create_engine('sqlite:///register.db')
Base.metadata.create_all(engine)
print("DB is Created")