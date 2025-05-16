from config.database import engine, Base

def create_table():
    ''' Creates all tables in the database. '''
    Base.metadata.create_all(engine)