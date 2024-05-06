import psycopg2
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
HOST = 'localhost'
PORT = 5432
DATABASE = 'satesto'
USER = 'postgres'
PASSWORD = 'XX132Files'

database_string = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(database_string)

Base = declarative_base()

class Test(Base):
    __tablename__ = "testtable"
    test_id = Column('test_id', Integer, primary_key=True, autoincrement=True)
    full_name = Column('full_name', String)
    id_number = Column('id_number', String, unique=True)

Base.metadata.create_all(engine)