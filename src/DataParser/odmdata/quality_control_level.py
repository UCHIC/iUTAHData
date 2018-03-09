from sqlalchemy import *

from base import Base


class QualityControlLevel(Base):
    __tablename__ = 'QualityControlLevels'

    id = Column('QualityControlLevelID', Integer, primary_key=True)
    code = Column('QualityControlLevelCode', String(255), nullable=False)
    definition = Column('Definition', String(255), nullable=False)
    explanation = Column('Explanation', String(255), nullable=False)

    def __repr__(self):
        return "<QualityControlLevel('%s', '%s', '%s', '%s')>" % (self.id, self.code, self.definition, self.explanation)
