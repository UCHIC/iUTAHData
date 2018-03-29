from sqlalchemy import *

from base import Base


class DataTypeCV(Base):
    __tablename__ = 'DataTypeCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<DataTypeCV('%s', '%s')>" % (self.term, self.definition)
