from sqlalchemy import *

from base import Base


class Method(Base):
    __tablename__ = 'Methods'

    id = Column('MethodID', Integer, primary_key=True)
    description = Column('MethodDescription', String(255), nullable=False)
    link = Column('MethodLink', String(255))

    def __repr__(self):
        return "<Method('%s', '%s', '%s')>" % (self.id, self.description, self.link)
