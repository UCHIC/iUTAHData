from sqlalchemy import *

from base import Base


class Unit(Base):
    __tablename__ = 'Units'

    id = Column('UnitsID', Integer, primary_key=True)
    name = Column('UnitsName', String(255))
    type = Column('UnitsType', String(255))
    abbreviation = Column('UnitsAbbreviation', String(255, convert_unicode=True))

    def __repr__(self):
        return "<Unit('%s', '%s', '%s')>" % (self.id, self.name, self.type)
