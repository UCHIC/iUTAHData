# Declare a mapped class
from sqlalchemy import *
from sqlalchemy.orm import relationship

from base import Base
from spatial_reference import SpatialReference


class Site(Base):
    __tablename__ = 'Sites'

    id = Column('SiteID', Integer, primary_key=True)
    code = Column('SiteCode', String)
    name = Column('SiteName', String)
    latitude = Column('Latitude', Float)
    longitude = Column('Longitude', Float)
    lat_long_datum_id = Column('LatLongDatumID', Integer, ForeignKey('SpatialReferences.SpatialReferenceID'))
    elevation_m = Column('Elevation_m', Float)
    vertical_datum = Column('VerticalDatum', String)
    local_x = Column('LocalX', Float)
    local_y = Column('LocalY', Float)
    local_projection_id = Column('LocalProjectionID', Integer, ForeignKey('SpatialReferences.SpatialReferenceID'))
    pos_accuracy_m = Column('PosAccuracy_m', Float)
    state = Column('State', String)
    county = Column('County', String)
    comments = Column('Comments', String)

    type = Column('SiteType', String)

    # relationships
    spatial_ref = relationship(SpatialReference, primaryjoin=("SpatialReference.id==Site.lat_long_datum_id"), lazy='subquery')
    local_spatial_ref = relationship(SpatialReference, primaryjoin=("SpatialReference.id==Site.local_projection_id"), lazy='subquery')

    def __init__(self, site_code, site_name):
        self.code = site_code
        self.name = site_name

    def get_site_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "lat_long_datum": self.spatial_ref.srs_name,
            "elevation": self.elevation_m,
            "local_x": self.local_x,
            "local_y": self.local_y,
            "local_projection": self.local_spatial_ref.srs_name if self.local_spatial_ref else 'None',
            "pos_accuracy": self.pos_accuracy_m,
            "state": self.state,
            "county": self.county,
            "comments": self.comments,
            "type": self.type
        }



    def __repr__(self):
        return "<Site('%s', '%s')>" % (self.code, self.name)
