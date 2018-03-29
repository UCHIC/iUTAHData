from sqlalchemy import *

from base import Base


class SampleTypeCV(Base):
    __tablename__ = 'SampleTypeCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<SampleTypeCV('%s', '%s')>" % (self.term, self.definition)
