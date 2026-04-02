from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal, Base
from app.models import note
from app.api.note_controller import router as notes_router

app = FastAPI()

app.include_router(notes_router)

Base.metadata.create_all(bind=engine)