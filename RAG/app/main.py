from fastapi import FastAPI
from app.routers.job import router as resume_router
from app.database import Base, engine
from app.models import job  # this forces the Job class to load

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(resume_router)



