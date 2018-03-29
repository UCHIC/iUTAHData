from sqlalchemy import *

from base import Base


class ISOMetadata(Base):
    __tablename__ = 'ISOMetadata'

    id = Column('MetadataID', Integer, primary_key=True)
    topic_category = Column('TopicCategory', String(255), nullable=False)
    title = Column('Title', String(255), nullable=False)
    abstract = Column('Abstract', String(255), nullable=False)
    profile_version = Column('ProfileVersion', String(255), nullable=False)
    metadata_link = Column('MetadataLink', String(255))

    def __repr__(self):
        return "<ISOMetadata('%s', '%s', '%s')>" % (self.id, self.topic_category, self.title)
