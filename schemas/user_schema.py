from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID

class UserInput(BaseModel):
    email: EmailStr
    username: str
    password: str  
    first_name: str
    last_name: str | None = None
    # is_admin: bool = False

class UserInDB(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    first_name: str
    last_name: str | None = None
    is_admin: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserProfile(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str | None = None

    class Config:
        orm_mode = True

class UserOutput(UserInDB):
    class Config:
        orm_mode = True
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str