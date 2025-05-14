from config.database import Base, engine

def create_table():
    """
    Creates all the database tables
    """
    Base.metadata.create_all(bind=engine)