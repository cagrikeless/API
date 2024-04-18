from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, Double, CHAR, MetaData
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy_utils import database_exists, create_database 
from local_settings import postgresql as settings
from datetime import datetime

meta_data = MetaData()

def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

engine = get_engine(settings['pguser'],
          settings['pgpasswd'],
          settings['pghost'],
          settings['pgport'],
          settings['pgdb'])


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class users(Base):
    __tablename__ = 'app_users'

    user_id = Column(Integer, primary_key=True,autoincrement=1)
    email = Column(String(100))
    password = Column(String(40))
    created_on = Column(DateTime(),default=datetime.now)
    last_logged_on = Column(DateTime())


class application_boards(Base):
    __tablename__ = 'app_boards'

    board_id = Column(Integer,primary_key=True)
    board_name = Column(String(4000))

class application_board_users(Base):
    __tablename__ = 'app_board_users'

    board_line_id = Column(Integer,primary_key=True,autoincrement=1)
    board_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)


class application_timesheet_lines(Base):
    __tablename__ = 'app_timesheet_lines'

    timesheet_line_id = Column(Integer, primary_key=True)
    owner_id = Column(Integer)
    description = Column(String(4000))
    entry_date = Column(DateTime())
    effort = Column(Integer)    # Hours
    last_update_date = Column(DateTime())


class application_tasks(Base):
    __tablename__ = 'app_tasks'

    task_id = Column(Integer, primary_key=True)
    title = Column(String(4000))
    description = Column(String(4000))
    owner_id = Column(Integer)
    status = Column(String(40)) # Not Started, In Progress, Completed


Base.metadata.create_all(engine)