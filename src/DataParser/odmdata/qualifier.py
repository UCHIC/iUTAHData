from sqlalchemy import *

from base import Base


class Qualifier(Base):
    __tablename__ = 'Qualifiers'

    id = Column('QualifierID', Integer, primary_key=True)
    code = Column('QualifierCode', String(255), nullable=False)
    description = Column('QualifierDescription', String(255), nullable=False)

    def __repr__(self):
        return "<Qualifier('%s', '%s', '%s')>" % (self.id, self.code, self.description)
