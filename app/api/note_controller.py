from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.note_repository import NoteRepository
from app.schemas.note_add_schema import NoteAddSchema

router = APIRouter(prefix="/api/notes", tags=["notes"])

@router.get("/")
def get_notes(id: int | None = None, db: Session = Depends(get_db)):
    repo = NoteRepository(db)
    if id:
        return repo.get_one_note(id)
    else:
        return repo.get_all()
    
@router.post("/add")
def add_note(schema: NoteAddSchema, db: Session = Depends(get_db)):
    repo = NoteRepository(db)
    return repo.create_note(title=schema.title, content=schema.content, tags=schema.tags)

@router.delete("/{id}")
def delete_note(id: int, db: Session = Depends(get_db)):
    repo = NoteRepository(db)
    return repo.delete_one_note(id)