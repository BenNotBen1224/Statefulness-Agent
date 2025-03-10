from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Memory(Base):
    __tablename__ = 'memories'
    
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    type = Column(String(50))  # e.g., 'interaction', 'learning', 'decision'
    content = Column(Text)
    context = Column(Text)
    
class Identity(Base):
    __tablename__ = 'identity'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    traits = Column(Text)
    preferences = Column(Text)
    learned_behaviors = Column(Text)

def init_sql_database():
    engine = create_engine('sqlite:///agent_memory.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session() 