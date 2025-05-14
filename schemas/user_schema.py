from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID

class UserInput(BaseModel):
    
    email : str
    password : str
    first_name : str
    last_name : str | None = None
    is_admin : bool
    
class UserInDB(UserInput):
    id: UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True
        
class UserOutput(UserInDB):
    password : str = Field(exclude=True)
    
    class Config:
        orm_mode = True
        form_attributes = True
    
class UserLogin(BaseModel):
    email : str
    password : str
    