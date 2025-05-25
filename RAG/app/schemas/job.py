
from pydantic import BaseModel

class JobBase(BaseModel):
    job_role: str
    job_description: str

class JobCreate(JobBase):
    pass

class JobOut(JobBase):
    job_id: int

    class Config:
        orm_mode = True
