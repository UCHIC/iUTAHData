from sqlalchemy import *

from base import Base


class SampleMediumCV(Base):
    __tablename__ = 'SampleMediumCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<SampleMedium('%s', '%s')>" % (self.term, self.definition)
