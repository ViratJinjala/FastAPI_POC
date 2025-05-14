



from models.user_model import User
from schemas.user_schema import UserInput, UserOutput
from utils.security import hash_password


class UserRepository:
    def __init__(self, db):
        self.db = db
        
    def create(self,userin: UserInput):
        user = User(
            **userin.model_dump(exclude={"password"}),
            password= hash_password(userin.password)
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_email(self, email: str):
        user = self.db.query(User).filter(User.email == email).first()
        if user:
            return UserOutput.model_validate(user)
        return None
    