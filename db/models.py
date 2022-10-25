from sqlalchemy import Column, Integer, String, Identity
from db.database import Base

class Job_openings(Base):
    __tablename__ = 'job_openings'
    job_id = Column(Integer , Identity(start=2001, cycle=True), primary_key=True)
    title = Column(String(100))
    department = Column(String(100))
    experience = Column(String(100))
    location = Column(String(100))
    job_type = Column(String(100))
    responsibilities = Column(String)
    requirements = Column(String)


class Applications(Base):
    __tablename__ = 'applications'
    app_id = Column(Integer , Identity(start=3001, cycle=True), primary_key=True)
    name = Column(String(100))
    experience = Column(String(100))
    job_id = Column(String(100))
    current_org = Column(String(100))
    current_title = Column(String(100))
    university = Column(String(100))
    cv = Column(String(200))
    status = Column(String(100))
    email = Column(String)
    