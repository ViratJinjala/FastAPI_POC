from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repository.user_repository import UserRepository
from schemas.user_schema import UserInput

class UserService:
    def __init__(self, db:Session):
        self.repository = UserRepository(db)
        
    def create(self,userin:UserInput):
        if self.repository.get_by_email(userin.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )
        print(userin)
        return self.repository.create(userin)
        