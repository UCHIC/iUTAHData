from sqlalchemy import *

from base import Base


class ValueTypeCV(Base):
    __tablename__ = 'ValueTypeCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<ValueTypeCV('%s', '%s')>" % (self.term, self.definition)
