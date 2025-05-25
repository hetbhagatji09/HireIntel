from sqlalchemy import Column, Integer, String
from app.database import Base  # Assuming you've declared a Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True, index=True)
    job_role = Column(String, nullable=False)
    job_description=Column(String, nullable=False)