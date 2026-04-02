from database import SessionLocal, engine, Base
from models.note import Note
from models import note

Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    try:
        if db.query(Note).count() > 0:
            print(f"No need to seed")
            return
        notes = [
            Note(
                title="Pierwsza notatka",
                content="To jest treść pierwszej notatki.",
                tags="python,fastapi"
            ),
            Note(
                title="sqlalchemy",
                content="this is sqlalchemy.",
                tags="sqlalchemy"
            ),
            Note(
                title="pancakge",
                content="panckage recepie.",
                tags="dinner,desert"
            ),
        ] 
        db.add_all(notes)
        db.commit()
        print(f"Added {len(notes)} notes")
    finally:
        db.close()

if __name__ == "__main__":
    seed()