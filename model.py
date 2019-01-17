from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True)
    actioname = Column(String)
    description = Column(String)
    actype = Column(String)
    def __repr__(self):
       return ("action Name: {}\n"
               "description: {} \n"
               "act type: {}").format(
                    self.actioname , self.description , self.actype)


