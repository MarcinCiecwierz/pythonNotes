from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.note import Note

class NoteRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Note]:
        stmt = select(Note)
        return list(self.db.scalars(stmt))
    
    def get_one_note(self, note_id: int) -> Note | None:
        stmt = select(Note).where(Note.id == note_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def delete_one_note(self, note_id: int) -> bool:
        note = self.get_one_note(note_id)
        if not note:
            return False
        self.db.delete(note)
        self.db.commit()
        return True
    
    def create_note(self, title: str, content: str, tags: str) -> Note:
        note = Note(title=title, content=content, tags=tags)
        self.db.add(note)
        self.db.commit()
        self.db.refresh(note)
        return note
        
    