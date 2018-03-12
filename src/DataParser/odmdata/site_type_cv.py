from sqlalchemy import *

from base import Base


class SiteTypeCV(Base):
    __tablename__ = 'SiteTypeCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<SiteTypeCV('%s', '%s')>" % (self.term, self.definition)
