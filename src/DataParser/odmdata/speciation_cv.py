from sqlalchemy import *

from base import Base


class SpeciationCV(Base):
    __tablename__ = 'SpeciationCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<SpeciationCV('%s', '%s')>" % (self.term, self.definition)
