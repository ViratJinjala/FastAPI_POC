from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repository.user_repository import UserRepository
from schemas.user_schema import UserInput, UserOutput

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
        
    def get_all_user(self):
        users = self.repository.get_all_users()
        return [UserOutput.model_validate(user) for user in users]
    
    def update_user(self,user_id:UUID,userin:UserInput):
        user=self.repository.update_user(user_id,userin)
        return UserOutput.model_validate(user)
    
    def delete_user(self,user_id:UUID):
        return self.repository.delete_user(user_id)