from pydantic import BaseModel

class NoteAddSchema(BaseModel):
    title: str
    content: str
    tags: str