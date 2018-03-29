from sqlalchemy import *

from base import Base


class VariableNameCV(Base):
    __tablename__ = 'VariableNameCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<VariableNameCV('%s', '%s')>" % (self.term, self.definition)
