from sqlalchemy import *

from base import Base


class TopicCategoryCV(Base):
    __tablename__ = 'TopicCategoryCV'

    term = Column('Term', String(255), primary_key=True)
    definition = Column('Definition', String(255))

    def __repr__(self):
        return "<TopicCategoryCV('%s', '%s')>" % (self.term, self.definition)
