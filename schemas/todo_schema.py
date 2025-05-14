from pydantic import BaseModel
from datetime import date,datetime
 
class TodoInput(BaseModel):
    title: str
    description: str|None = None
    status: bool = False
    due_date: date|None = None
 
class TodoInDB(TodoInput):
    id: int
    created_at: datetime
    updated_at: datetime
 
    class Config: # for serializer purpose
        orm_mode = True
 
class TodoOutput(TodoInDB):
    pass