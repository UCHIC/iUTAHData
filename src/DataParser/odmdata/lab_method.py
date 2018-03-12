from sqlalchemy import *

from base import Base


class LabMethod(Base):
    __tablename__ = 'LabMethods'

    id = Column('LabMethodID', Integer, primary_key=True)
    name = Column('LabName', String(255), nullable=False)
    organization = Column('LabOrganization', String(255), nullable=False)
    method_name = Column('LabMethodName', String(255), nullable=False)
    method_description = Column('LabMethodDescription', String(255), nullable=False)
    method_link = Column('LabMethodLink', String(255))

    def __repr__(self):
        return "<LabMethod('%s', '%s', '%s', '%s')>" % (self.id, self.name, self.organization, self.method_name)
