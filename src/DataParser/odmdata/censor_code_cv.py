from sqlalchemy import *

from base import Base


class CensorCodeCV(Base):
    __tablename__ = 'CensorCodeCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<CensorCodeCV('%s', '%s')>" % (self.term, self.definition)
