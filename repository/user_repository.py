from uuid import UUID
from models.user_model import User
from schemas.user_schema import UserInput
from utils.security import hash_password


class UserRepository:
    def __init__(self, db):
        self.db = db

    def create(self, userin: UserInput):
        user = User(
            email=userin.email,
            username=userin.username,
            password=hash_password(userin.password),
            first_name=userin.first_name,
            last_name=userin.last_name,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
    
    def get_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def get_all_users(self):
        return self.db.query(User).all()
    
    def get_by_id(self, user_id: UUID):
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user_id: UUID, userin: UserInput):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        for key, value in userin.model_dump(exclude_unset=True).items():
            if key == "password":
                setattr(user, "password", hash_password(value))
            else:
                setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id: UUID):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        self.db.delete(user)
        self.db.commit()
        return user