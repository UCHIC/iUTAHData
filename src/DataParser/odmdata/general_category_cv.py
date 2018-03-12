from sqlalchemy import *

from base import Base


class GeneralCategoryCV(Base):
    __tablename__ = 'GeneralCategoryCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<GeneralCategoryCV('%s', '%s')>" % (self.term, self.definition)
