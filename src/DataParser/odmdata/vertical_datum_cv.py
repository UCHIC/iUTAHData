from sqlalchemy import *

from base import Base


class VerticalDatumCV(Base):
    __tablename__ = 'VerticalDatumCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<VerticalDatumCV('%s', '%s')>" % (self.term, self.definition)
