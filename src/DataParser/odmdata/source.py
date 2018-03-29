from sqlalchemy import *
from sqlalchemy.orm import relationship

from base import Base
from iso_metadata import ISOMetadata


class Source(Base):
    __tablename__ = 'Sources'

    id = Column('SourceID', Integer, primary_key=True)
    organization = Column('Organization', String(255), nullable=False)
    description = Column('SourceDescription', String(255), nullable=False)
    link = Column('SourceLink', String(255))
    contact_name = Column('ContactName', String(255), nullable=False)
    phone = Column('Phone', String(255), nullable=False)
    email = Column('Email', String(255), nullable=False)
    address = Column('Address', String(255), nullable=False)
    city = Column('City', String(255), nullable=False)
    state = Column('State', String(255), nullable=False)
    zip_code = Column('ZipCode', String(255), nullable=False)
    citation = Column('Citation', String(255), nullable=False)
    iso_metadata_id = Column('MetadataID', Integer, ForeignKey('ISOMetadata.MetadataID'), nullable=False)

    # relationships
    iso_metadata = relationship(ISOMetadata)

    def __repr__(self):
        return "<Source('%s', '%s', '%s')>" % (self.id, self.organization, self.description)
