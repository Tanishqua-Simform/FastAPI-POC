from config.database import engine, Base

def create_table():
    Base.metadata.create_all(engine)