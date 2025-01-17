from sqlalchemy import *

from base import Base


class SpatialReference(Base):
    __tablename__ = 'SpatialReferences'

    id = Column('SpatialReferenceID', Integer, primary_key=True)
    srs_id = Column('SRSID', Integer)
    srs_name = Column('SRSName', String(255))
    is_geographic = Column('IsGeographic', Boolean)
    notes = Column('Notes', String(255))

    def __repr__(self):
        return "<SpatialReference('%s', '%s')>" % (self.id, self.srs_name)
