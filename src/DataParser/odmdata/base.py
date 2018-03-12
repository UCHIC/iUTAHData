from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


def create_database(engine, db_name):
    engine.execute("CREATE DATABASE %s" % db_name)


def create_tables(engine):
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print(e)
