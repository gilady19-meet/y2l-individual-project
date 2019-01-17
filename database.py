from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def function(parameter):
    pass

def add_action_to_database(actioname , description , actype):
        acitiviy_object = Activity(
        actioname=actioname,
        description=description,
        actype=actype)
        session.add(acitiviy_object)
        session.commit()

def get_all_activities():
    actions = session.query(Activity).all()
    return actions